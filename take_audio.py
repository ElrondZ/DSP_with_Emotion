import tkinter as tk


def take_audio():
    # 拍视频逻辑
    print("aaa")


root = tk.Tk()
# 标题
root.title("audio")
# 大小
root.minsize(800, 1000)
# 开始按钮
Start = tk.Button(root, text='Start', command=take_audio())
root.mainloop()
