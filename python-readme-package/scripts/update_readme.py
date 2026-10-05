from pathlib import Path
import re

CHALLENGES = [
    (1, "Personal Profile and Expense Calculator", "Foundation"),
    (2, "Smart Shopping Bill Generator", "Intermediate"),
    (3, "Student Performance Report Generator", "Advanced"),
    (4, "Username and Email Analyzer", "Foundation"),
    (5, "Text-Based Feedback Analyzer", "Intermediate"),
    (6, "Simple Username and Password Validator", "Advanced"),
    (7, "Advanced Two-Number Calculator", "Foundation"),
    (8, "College Admission Eligibility System", "Intermediate"),
    (9, "Personal Loan Eligibility and EMI Estimator", "Advanced"),
    (10, "Custom Multiplication Table Generator", "Foundation"),
    (11, "Number Pattern and Sequence Explorer", "Intermediate"),
    (12, "Number Guessing Game with Score Tracking", "Advanced"),
    (13, "Student Marks Management System", "Foundation"),
    (14, "Inventory and Stock Management System", "Intermediate"),
    (15, "College Event Registration and Attendance Tracker", "Advanced"),
    (16, "Reusable Utility Toolkit", "Foundation"),
    (17, "Personal Finance Calculator with Functions", "Intermediate"),
    (18, "Console-Based Exam Preparation and Quiz Application", "Advanced"),
]

def exists(n: int) -> bool:
    return Path(f"q{n}.py").is_file()

statuses = {n: exists(n) for n, _, _ in CHALLENGES}
completed = sum(statuses.values())
total = len(CHALLENGES)
percent = round(completed / total * 100)

bar_length = 24
filled = round(bar_length * completed / total)
bar = "█" * filled + "░" * (bar_length - filled)

stage_groups = [
    ("🟢 Stage 1 — Get Comfortable", [1, 4, 7, 10, 13, 16]),
    ("🟡 Stage 2 — Combine Concepts", [2, 5, 8, 11, 14, 17]),
    ("🔴 Stage 3 — Challenge Yourself", [3, 6, 9, 12, 15, 18]),
]

lines = []
lines.append(f"### {completed}/{total} challenges completed · {percent}%")
lines.append("")
lines.append(f"`{bar}` **{percent}%**")
lines.append("")
lines.append("| # | Challenge | Level | Status |")
lines.append("|---:|---|---|---|")

for n, title, level in CHALLENGES:
    if statuses[n]:
        status = f"✅ [Completed](./q{n}.py)"
    else:
        status = "⬜ Not started"
    lines.append(f"| {n} | [{title}](./q{n}.py) | {level} | {status} |")

lines.append("")
for stage_name, nums in stage_groups:
    done = sum(statuses[n] for n in nums)
    lines.append(f"- **{stage_name}:** {done}/{len(nums)}")

lines.append("")
lines.append(f"> Last dashboard update: `{__import__('datetime').datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}`")

dashboard = "\n".join(lines)

path = Path("README.md")
content = path.read_text(encoding="utf-8")

pattern = re.compile(
    r"(<!-- PRACTICE-DASHBOARD:START -->).*?(<!-- PRACTICE-DASHBOARD:END -->)",
    re.DOTALL,
)

replacement = r"\1\n" + dashboard + r"\n\2"
updated, count = pattern.subn(replacement, content, count=1)

if count != 1:
    raise SystemExit("README dashboard markers were not found.")

path.write_text(updated, encoding="utf-8")
print(f"Updated README: {completed}/{total} challenges completed ({percent}%).")
