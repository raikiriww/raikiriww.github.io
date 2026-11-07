import os
import re

def find_and_replace_in_file_v4(file_path, patterns_replacements):
    modified = False
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read().strip()
    
    # 特殊情况：如果文件只有一行，并且这一行是以 ".html" 结尾的字符串
    if file_contents.endswith('.html') and '\n' not in file_contents:
        new_contents = f'<meta http-equiv="refresh" content="0;url={file_contents}" />'
        modified = True
    else:
        for pattern, replacement in patterns_replacements.items():
            # 使用正则表达式查找所有匹配项
            new_contents, num_replacements = re.subn(pattern, replacement, file_contents)
            
            # 如果有替换发生，更新文件内容
            if num_replacements > 0:
                file_contents = new_contents
                modified = True

    # 如果有任何修改，写回文件
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_contents)
        return True
    return False

# 定义正则表达式和替换字符串的映射
patterns_replacements_with_meta = {
    r'\"/(?!/)': '"/coolshell/',
    r'(?<!/coolshell/)wp-content/': 'coolshell/wp-content/'
}

# 获取当前工作目录
current_directory = os.getcwd()

# 用于存储已修改的文件列表
modified_files_with_meta = []

# 遍历当前目录及其所有子目录
for root, dirs, files in os.walk(current_directory):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            # 在文件中查找和替换字符串
            if find_and_replace_in_file_v4(file_path, patterns_replacements_with_meta):
                modified_files_with_meta.append(file_path)

# 显示已修改的文件列表（在实际环境中运行时用于检查）
# print("Modified files:", modified_files_with_meta)

# 定义要查找的文件和其相对路径
target_file = "style.css"
relative_path = os.path.join("wp-content", "themes", "MyNisarg")

# 在当前目录下查找目标文件
target_file_path = os.path.join(current_directory, relative_path, target_file)

# 检查文件是否存在
file_exists = os.path.exists(target_file_path)

# 如果文件存在，进行字符串替换
if file_exists:
    # 定义正则表达式和替换字符串
    css_pattern_replacement = {r'\(/coolshell_logo\.png\)': r'(/coolshell/coolshell_logo.png)'}
    
    # 在文件中查找和替换字符串
    find_and_replace_in_file_v4(target_file_path, css_pattern_replacement)
