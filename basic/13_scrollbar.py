import tkinter as tk  # pylint: disable=wildcard-import, unused-wildcard-import

root = tk.Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox = tk.Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):  # 1 ~ 31 일
    listbox.insert(tk.END, str(i) + "일")  # 1일, 2일, ...
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
