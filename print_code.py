import os

def display_repo_tree(startpath, output_file):
    """
    สร้างโครงสร้างแบบ tree ของ repository โดยไม่รวมบางไดเรกทอรีที่ระบุ
    และเขียนลงในไฟล์ output พร้อมทั้งแสดงเนื้อหาของไฟล์นามสกุลที่กำหนด (.py, .html, .css, .js)
    """
    # ไดเรกทอรีที่ต้องการข้าม (ไม่แสดงใน tree)
    EXCLUDED_DIRS = {'.env', '.git', '__pycache__', '.venv', 'env', 'node_modules'}
    
    # นามสกุลไฟล์ที่ต้องการแสดงเนื้อหา
    INCLUDED_EXTENSIONS = ('.cs','.py', '.html', '.css', '.js', '.vue')

    def tree_symbols(level, is_last):
        """สร้างสัญลักษณ์สำหรับโครงสร้าง tree"""
        if level == 0:
            return ""
        prefix = "".join("    " if l else "│   " for l in is_last[:-1])
        connector = "└── " if is_last[-1] else "├── "
        return prefix + connector

    def should_include_item(path):
        """
        ตรวจสอบว่าไฟล์หรือโฟลเดอร์นี้ควรจะถูกรวมอยู่ใน tree หรือไม่
        (เปลี่ยนชื่อจาก is_python_repo_item)
        """
        basename = os.path.basename(path)

        if os.path.isdir(path) and basename in EXCLUDED_DIRS:
             return False 

        if os.path.isdir(path):
             return True # รวมไดเรกทอรีทั้งหมดที่ไม่ได้อยู่ใน EXCLUDED_DIRS

        # รวมไฟล์ config ที่สำคัญ และไฟล์ที่มีนามสกุลตามที่กำหนด
        return basename in {
            'requirements.txt', 'Pipfile', 'README.md', 'README.rst', 
            '.gitignore', 'setup.py', 'pyproject.toml', 'package.json'
        } or path.endswith(INCLUDED_EXTENSIONS)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(os.path.basename(startpath) + '\n')

        def walk_dir(path, level=0, is_last_list=[]):
            """ฟังก์ชัน Recursive สำหรับ duyệtไดเรกทอรีและเขียนข้อมูลลงไฟล์"""
            try:
                # คัดกรองรายการในไดเรกทอรี
                entries = sorted([
                    entry for entry in os.listdir(path)
                    if should_include_item(os.path.join(path, entry))
                ])
            except OSError as e:
                out_file.write(f"{tree_symbols(level, is_last_list + [True])}[Error accessing: {os.path.basename(path)} - {e}]\n")
                return

            for i, entry in enumerate(entries):
                full_path = os.path.join(path, entry)
                is_current_last = (i == len(entries) - 1)
                current_is_last_list = is_last_list + [is_current_last]

                out_file.write(tree_symbols(level + 1, current_is_last_list) + entry + '\n')

                if os.path.isdir(full_path):
                    walk_dir(full_path, level + 1, current_is_last_list)
                # **จุดที่แก้ไข:** ตรวจสอบนามสกุลไฟล์จาก INCLUDED_EXTENSIONS
                elif os.path.isfile(full_path) and entry.endswith(INCLUDED_EXTENSIONS):
                    # แสดงเนื้อหาของไฟล์
                    try:
                        content_prefix = "".join("    " if l else "│   " for l in current_is_last_list) + "    "
                        out_file.write(f"{content_prefix}# Contents of {entry}:\n")
                        with open(full_path, 'r', encoding='utf-8') as f:
                            for line in f:
                                out_file.write(f"{content_prefix}{line.rstrip()}\n")
                            out_file.write('\n') # เว้นบรรทัดหลังจบไฟล์
                    except Exception as e:
                        out_file.write(f"{content_prefix}[Error reading file: {e}]\n")

        # เริ่มต้นการทำงาน
        walk_dir(startpath)

# --- วิธีการใช้งาน ---
if __name__ == "__main__":
    # ระบุ path ของโปรเจกต์ของคุณ
    repo_path = './'  # './' หมายถึงไดเรกทอรีปัจจุบัน
    output_filename = 'output_tree_full.txt'

    if os.path.isdir(repo_path):
        print(f"Generating repository tree for: {os.path.abspath(repo_path)}")
        display_repo_tree(repo_path, output_filename)
        print(f"Repository tree saved to: {output_filename}")
    else:
        print(f"Error: Directory not found at {repo_path}")