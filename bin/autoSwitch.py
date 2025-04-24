import sys
import os

# DESIGNER_DIR = "C:\Users\wj\AppData\Local\Programs\Python\Python38\Lib\site-packages\qt5_applications\Qt\bin"
# PYUIC_DIR = "C:\Users\wj\AppData\Local\Programs\Python\Python38\Scripts"
PYUIC_DIR = ""
OUT_DIR = ""

pyui_file = os.path.join(PYUIC_DIR,"pyuic5.exe")

# 构建命令
command = f"{pyui_file} -o hello.py hello.ui"
# 执行命令
result = os.system(command)

if result == 0:
    print("成功生成UI文件")
else:
    print("生成UI文件失败")

