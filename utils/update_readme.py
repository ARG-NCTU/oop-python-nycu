import pandas as pd

def read_results(file_path="utils/pytest_results.txt"):
    """
    Read pytest results from a text file and return lines containing a status.
    """
    with open(file_path, "r") as f:
        return [line.strip() for line in f if ": " in line]

def read_commit_counts(file_path="utils/commit_counts.xlsx"):
    # Read Excel file with commit counts per group
    df = pd.read_excel(file_path)
    return df

def generate_markdown_table(results, df_counts):
    # Build status map from pytest results using group numbers
    import re
    status_map = {}
    for line in results:
        grp_raw, status = line.split(": ")
        m = re.search(r"\d+", grp_raw)
        if m:
            status_map[m.group()] = status

    # Prepare table header based on DataFrame columns
    cols = df_counts.columns.tolist()
    header = ["Status"] + cols
    sep = ["------"] * len(header)
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]

    # Populate rows
    for _, row in df_counts.iterrows():
        # Extract group number for lookup in status_map
        import re
        grp_raw = str(row.get("Group", ""))
        m = re.search(r"\d+", grp_raw)
        key = m.group() if m else None
        status = status_map.get(key, "unknown")
        emoji = "✅" if status == "success" else "❌"
        cells = [emoji] + [
            str(row.get(col, "")) if not pd.isna(row.get(col, "")) else ""
            for col in cols
        ]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)

def replace_section(content, marker, replacement):
    start = f"<!--START_SECTION:{marker}-->"
    end = f"<!--END_SECTION:{marker}-->"
    s_idx = content.find(start)
    e_idx = content.find(end)
    return content[:s_idx + len(start)] + "\n" + replacement + "\n" + content[e_idx:]

results = read_results()
df_counts = read_commit_counts()
table = generate_markdown_table(results, df_counts)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

updated = replace_section(content, "pytest", table)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
