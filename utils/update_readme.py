def read_results(file_path="pytest_results.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if ": " in line]

def generate_markdown_table(results):
    lines = ["| Group | Status  |", "|-------|---------|"]
    for line in results:
        group, status = line.split(": ")
        emoji = "✅" if status == "success" else "❌"
        lines.append(f"| {group} | {emoji} {status} |")
    return "\n".join(lines)

def replace_section(content, marker, replacement):
    start = f"<!--START_SECTION:{marker}-->"
    end = f"<!--END_SECTION:{marker}-->"
    s_idx = content.find(start)
    e_idx = content.find(end)
    return content[:s_idx + len(start)] + "\n" + replacement + "\n" + content[e_idx:]

results = read_results()
table = generate_markdown_table(results)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated = replace_section(content, "pytest", table)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
