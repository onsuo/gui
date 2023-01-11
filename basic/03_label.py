from tkinter import *  # pylint: disable=wildcard-import, unused-wildcard-import

root = Tk()
root.geometry("640x480")
root.title("Nado GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.configure(text="또 만나요")

    global photo2  # garbage collection 으로 인해 지워질 수 있어 전역변수로 선언
    photo2 = PhotoImage(file="img2.png")
    label2.configure(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
