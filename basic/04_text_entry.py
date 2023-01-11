from tkinter import *  # pylint: disable=wildcard-import, unused-wildcard-import

root = Tk()
root.geometry("640x480")
root.title("Nado GUI")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)  # 줄바꿈 안됨
e.pack()
e.insert(0, "한 줄만 입력해요")
# e.insert(END, "한 줄만 입력해요")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 첫번째 줄, 0: 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
