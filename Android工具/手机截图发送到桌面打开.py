import os

win_desktop_path = r"C:\Users\xuebin\Desktop"
path = win_desktop_path


def screencap_android():
    os.system("adb shell screencap -p /sdcard/tmp.png")
    os.system(f"adb pull /sdcard/tmp.png {path}")
    # 这个start的意思是找寻能打开图片的应用打开此图片
    os.system(f"start {path}\\tmp.png")  # TODO 这个start命令可能只是windows下特有的，Mac上可能打不开


if __name__ == '__main__':
    screencap_android()
