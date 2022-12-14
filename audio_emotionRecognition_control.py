import tkinter as tk


def take_audio():
    print("aaa")


def pinpu():
    print("频谱")


def boxingtu():
    print("波形图")


def result():
    print("情感结果")


root = tk.Tk()
# 标题
root.title("音频分析")
# 大小
root.minsize(600, 400)
# 开始按钮
luyin = tk.Button(root, text='录音', height=30, width=20, command=take_audio())
pinpu = tk.Button(root, text='生成频谱', height=30, width=20, command=pinpu())
boxingtu = tk.Button(root, text='波形图', height=30, width=20, command=boxingtu())
result = tk.Button(root, text='生成结果', height=30, width=20, command=result())

luyin.pack(side=tk.LEFT)
pinpu.pack(side=tk.LEFT)
boxingtu.pack(side=tk.RIGHT)
result.pack(side=tk.BOTTOM)

root.mainloop()
