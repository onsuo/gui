import tkinter as tk  # pylint: disable=wildcard-import, unused-wildcard-import

root = tk.Tk()
root.title("Nado GUI")
root.geometry("640x480")

# btn1 = tk.Button(root, text="버튼1")
# btn2 = tk.Button(root, text="버튼2")

# # btn1.pack(side="left")
# # btn2.pack(side="left")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 맨 윗줄
btn_f16 = tk.Button(root, text="F16", width=5, height=2)  # width, height: 글자 단위
btn_f17 = tk.Button(root, text="F17", width=5, height=2)
btn_f18 = tk.Button(root, text="F18", width=5, height=2)
btn_f19 = tk.Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky="NEWS", padx=3, pady=3)
# btn_f16.place(x=0, y=0, width=50, height=50)  # width, height: 길이 단위
btn_f17.grid(row=0, column=1, sticky="NEWS", padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky="NEWS", padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky="NEWS", padx=3, pady=3)

# clear 줄
btn_clear = tk.Button(root, text="clear", width=5, height=2)
btn_equal = tk.Button(root, text="=", width=5, height=2)
btn_div = tk.Button(root, text="/", width=5, height=2)
btn_mul = tk.Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky="NEWS", padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky="NEWS", padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky="NEWS", padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky="NEWS", padx=3, pady=3)

# 7 시작 줄
btn_7 = tk.Button(root, text="7", width=5, height=2)
btn_8 = tk.Button(root, text="8", width=5, height=2)
btn_9 = tk.Button(root, text="9", width=5, height=2)
btn_sub = tk.Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky="NEWS", padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky="NEWS", padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky="NEWS", padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky="NEWS", padx=3, pady=3)

# 4 시작 줄
btn_4 = tk.Button(root, text="4", width=5, height=2)
btn_5 = tk.Button(root, text="5", width=5, height=2)
btn_6 = tk.Button(root, text="6", width=5, height=2)
btn_add = tk.Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky="NEWS", padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky="NEWS", padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky="NEWS", padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky="NEWS", padx=3, pady=3)

# 1 시작 줄
btn_1 = tk.Button(root, text="1", width=5, height=2)
btn_2 = tk.Button(root, text="2", width=5, height=2)
btn_3 = tk.Button(root, text="3", width=5, height=2)
btn_enter = tk.Button(root, text="enter", width=5, height=2)  # 세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky="NEWS", padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky="NEWS", padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky="NEWS", padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky="NEWS", padx=3, pady=3)  # 현재 위치로부터 아래쪽으로 몇 줄을 더함

# 0 시작 줄
btn_0 = tk.Button(root, text="0", width=5, height=2)  # 가로로 합쳐짐
btn_point = tk.Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky="NEWS", padx=3, pady=3)  # 현재 위치로부터 오른쪽으로 몇 칸을 더함
btn_point.grid(row=5, column=2, sticky="NEWS", padx=3, pady=3)

root.mainloop()
