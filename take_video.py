import tkinter as tk


def video_motio_recognition():
    # 拍视频逻辑
    print("aaa")


root = tk.Tk()
# 标题
root.title("Video Motio Recognition")
# 大小
root.minsize(800, 1000)
# 开始按钮
start = tk.Button(root, text='Start', command=video_motio_recognition())
start.pack()
root.mainloop()
