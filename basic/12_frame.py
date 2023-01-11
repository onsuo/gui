import tkinter as tk  # pylint: disable=wildcard-import, unused-wildcard-import

root = tk.Tk()
root.title("Nado GUI")
root.geometry("640x480")

tk.Label(root, text="메뉴를 선택해주세요").pack(side="top")

tk.Button(root, text="주문하기").pack(side="bottom")

# 메뉴 프레임
frame_burger = tk.Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

tk.Button(frame_burger, text="햄버거").pack()
tk.Button(frame_burger, text="치즈버거").pack()
tk.Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = tk.LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

tk.Button(frame_drink, text="콜라").pack()
tk.Button(frame_drink, text="사이다").pack()

root.mainloop()
