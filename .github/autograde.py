import pytest
import sys
import os

class GraderPlugin:
    def __init__(self):
        self.results = {}

    def pytest_runtest_logreport(self, report):
        if report.when == 'call':
            test_name = report.nodeid
            self.results[test_name] = report.passed

def main():
    plugin = GraderPlugin()
    # 运行测试，拦截输出，避免满屏报错影响分数查看
    print("⏳ 正在运行自动测试，请稍候...\n")
    pytest.main(['tests/', '-q', '--tb=short'], plugins=[plugin])
    
    # 分数权重分配 (代码满分 100 分：前三题共 70 分，Bonus 30 分)
    weights = {
        'test_p1.py': 20.0,
        'test_p2.py': 20.0,
        'test_p3.py': 30.0,
        'test_bonus.py': 30.0  # 附加题 30 分
    }
    
    counts = {k: 0 for k in weights.keys()}
    passes = {k: 0 for k in weights.keys()}
    
    for nodeid, passed in plugin.results.items():
        for key in counts.keys():
            if key in nodeid:
                counts[key] += 1
                if passed:
                    passes[key] += 1
                    
    total_base_score = 0.0
    bonus_score = 0.0
    
    summary_lines = ["### 🤖 自动评分结果 (GitHub Actions)"]
    summary_lines.append("| 任务模块 | 测试通过率 | 得分 | 满分 |")
    summary_lines.append("| :--- | :---: | :---: | :---: |")
    
    for key, max_score in weights.items():
        if counts[key] > 0:
            score = (passes[key] / counts[key]) * max_score
        else:
            score = 0.0
            
        if key == 'test_bonus.py':
            bonus_score += score
            summary_lines.append(f"| Bonus (Van der Pol) | {passes[key]}/{counts[key]} | +{score:.1f} | +{max_score} |")
        else:
            total_base_score += score
            name = key.replace('test_', '').replace('.py', '').upper()
            summary_lines.append(f"| {name} | {passes[key]}/{counts[key]} | **{score:.1f}** | {max_score} |")

    summary_lines.append(f"\n**✅ 核心代码基础得分: {total_base_score:.1f} / 32.0**")
    summary_lines.append(f"**🚀 Bonus 挑战得分: +{bonus_score:.1f}**")
    summary_lines.append("\n> *注：此处仅计入「代码正确性」分数（占总分 40%）。剩余 60% 分数将由助教根据 `Report_Template.md` 中的物理分析、图表和 AI Review 记录进行人工评阅。*")
    
    summary_text = "\n".join(summary_lines)
    print("\n" + "="*50)
    print(summary_text)
    print("="*50 + "\n")
    
    # 写入 GitHub Actions 的 Step Summary，让学生在网页上直接看到 Markdown 表格
    summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary_file:
        with open(summary_file, 'a', encoding='utf-8') as f:
            f.write(summary_text + "\n")
            
    # 如果核心测试没全过，返回非 0 退出码让 Action 标红
    if total_base_score < 32.0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
