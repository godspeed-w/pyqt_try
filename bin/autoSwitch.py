"""自动检查目录下的ui文件是否变化, 如果有变化就自动转换为py文件"""

import sys
import os
from pathlib import Path
import time

# DESIGNER_DIR = "C:\Users\wj\AppData\Local\Programs\Python\Python38\Lib\site-packages\qt5_applications\Qt\bin"
# PYUIC_DIR = "C:\Users\wj\AppData\Local\Programs\Python\Python38\Scripts"


def scanFiles(dir, regex):
    """扫描目录下的文件"""
    files = {}
    target_dir = Path(dir)
    for file_path in target_dir.rglob(regex):
        if file_path.is_file():
            file_stat = file_path.stat()
            updateTime = time.ctime(file_stat.st_mtime)
            files[file_path.__str__()] = updateTime
    return files


def doTransform(file_path, pyui_file):
    """执行转换"""
    # 构建命令
    directory = os.path.dirname(file_path)
    # 获取文件名
    filename = os.path.basename(file_path).split(".")[0]
    pyFile = os.path.join(directory, filename + "_ui.py")
    command = f'{pyui_file} -o "{pyFile}" "{file_path}"'
    # 执行命令
    result = os.system(command)
    local_time = time.localtime(time.time())
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    if result == 0:
        print(formatted_time, "成功生成py文件:", command)
    else:
        print(formatted_time, "生成py文件失败:", command)


if __name__ == "__main__":
    PYUI_DIR = "widgets"
    PYUIC_FILE = "pyuic5.exe"
    REGEX = "*.ui"
    # -----------------------------
    allFiles = scanFiles(PYUI_DIR, REGEX)
    print(allFiles.keys())
    print("开始扫描...")
    while True:
        time.sleep(1)
        tmpScanFiles = scanFiles(PYUI_DIR, REGEX)
        for k, v in tmpScanFiles.items():
            # 新增
            if k not in allFiles.keys():
                print("新增文件:", k)
                allFiles[k] = v
                doTransform(k, PYUIC_FILE)
            # 修改
            if k in allFiles.keys() and v != allFiles[k]:
                print("修改文件:", k)
                allFiles[k] = v
                doTransform(k, PYUIC_FILE)
