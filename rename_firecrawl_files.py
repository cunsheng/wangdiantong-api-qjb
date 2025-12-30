import os

target_dir = 'Firecrawl'
prefix = 'open.wangdian.cn_qjb_open_apidoc_doc_path='

# 确保目标目录存在
if not os.path.exists(target_dir):
    print(f"Directory '{target_dir}' not found.")
    exit(1)

count = 0
for filename in os.listdir(target_dir):
    # 只处理包含特定前缀的文件
    if prefix in filename:
        new_filename = filename.replace(prefix, '')
        old_path = os.path.join(target_dir, filename)
        new_path = os.path.join(target_dir, new_filename)

        # 简单的安全检查，防止覆盖同名文件
        if os.path.exists(new_path):
            print(f"[Skip] Target already exists: {new_filename} (from {filename})")
            continue

        try:
            os.rename(old_path, new_path)
            print(f"[Renamed] {filename} -> {new_filename}")
            count += 1
        except Exception as e:
            print(f"[Error] Failed to rename {filename}: {e}")

print(f"\nProcessing complete. Total files renamed: {count}")
