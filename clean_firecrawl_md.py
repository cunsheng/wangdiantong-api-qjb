import os
import re
from tqdm import tqdm

def clean_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if len(lines) < 4:
        return

    # 1. 保留 YAML Front Matter (前4行)
    header = lines[:4]
    content = lines[4:]

    # 寻找切分点
    start_idx = -1
    end_idx = -1

    # 查找 "当前位置： API文档"
    for i, line in enumerate(content):
        if "当前位置： API文档" in line:
            start_idx = i
            break

    # 查找 "常用工具"
    for i, line in enumerate(content):
        if "常用工具" in line:
            end_idx = i
            break

    # 确定内容截取范围
    if start_idx != -1:
        # 删除 “当前位置” 及其之前的内容
        slice_start = start_idx + 1
    else:
        slice_start = 0

    if end_idx != -1:
        # 删除 “常用工具” 及其之后的内容
        if end_idx > slice_start:
            slice_end = end_idx
        else:
            slice_end = len(content)
    else:
        slice_end = len(content)

    body_lines = content[slice_start:slice_end]
    body_text = "".join(body_lines)

    # --- 清理规则 ---

    # 1. 删除包含 "¥标准" 的整行
    body_text = re.sub(r'^.*¥标准.*$\n?', '', body_text, flags=re.MULTILINE)

    # 2. 删除连续的数字行号垃圾数据 (如 "1<br>2<br>3...")
    # body_text = re.sub(r'(\d+<br>)+\d+', '', body_text)

    # 3. 预处理：分离标题和紧接的内容
    # 例如： "**3.请求参数说明** 3.1 请求地址" -> "**3.请求参数说明**\n3.1 请求地址"
    body_text = re.sub(r'(3\.请求参数说明)\s*(3\.1\s*请求地址)', r'\1\n\2', body_text)

    # 4. 删除 "3.1 请求地址" 块
    pattern_3_1 = r'(3\.1\s*请求地址[\s\S]*?)(?=\n.*?3\.2|\n.*?3\.3|\n.*?3\.\s*业务请求参数|\n.*?4\.)'
    body_text = re.sub(pattern_3_1, '', body_text, flags=re.MULTILINE)

    # 5. 清理多余空行
    body_text = re.sub(r'\n{3,}', '\n\n', body_text)

    # 组合结果
    new_content = "".join(header) + body_text.strip() + "\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    target_dir = 'Firecrawl'
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} not found.")
        return

    files = [f for f in os.listdir(target_dir) if f.endswith('.md')]

    print(f"Processing {len(files)} files...")
    for filename in tqdm(files):
        file_path = os.path.join(target_dir, filename)
        clean_md_file(file_path)

    print("Done.")

if __name__ == '__main__':
    main()

