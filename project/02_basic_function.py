import tkinter as tk  # __all__
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox
from tkinter import ttk

root = tk.Tk()
# root.resizable(False, False)
root.title("Image Merger")


# 파일 추가
def add_file():
    files = fd.askopenfilenames(
        title="이미지 파일을 선택하세요",
        filetypes=(
            ("PNG 파일", "*.png"),
            ("모든 파일", "*.*"),
        ),
        initialdir=r"C:\Dev",  # 최초에 사용자가 지정한 경로를 보여줌
    )
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(tk.END, file)


# 선택 삭제
def del_file():
    for idx in reversed(list_file.curselection()):
        list_file.delete(idx)


# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = fd.askdirectory()
    if folder_selected == "":  # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, tk.END)
    txt_dest_path.insert(0, folder_selected)


# 시작
def start():
    # 각 옵션들 값을 확인
    print("가로 넓이:", cmb_width.get())
    print("간격:", cmb_space.get())
    print("파일 포맷:", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return


# 파일 프레임 (파일 추가, 선택 삭제)
frame_file = tk.Frame(root)
frame_file.pack(fill="x", padx=5, pady=5)  # 간격 띄우기

btn_add_file = tk.Button(frame_file, text="파일 추가", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = tk.Button(frame_file, text="선택 삭제", padx=5, pady=5, width=12, command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
frame_list = tk.Frame(root)
frame_list.pack(fill="both", padx=5, pady=5)

scrlbar = tk.Scrollbar(frame_list)
scrlbar.pack(side="right", fill="y")

list_file = tk.Listbox(frame_list, selectmode="extended", height=15, yscrollcommand=scrlbar.set)
list_file.pack(side="left", fill="both", expand=True)

scrlbar.config(command=list_file.yview)

# 저장 경로 프레임
frame_path = tk.LabelFrame(root, text="저장 경로")
frame_path.pack(fill="x", ipady=5, padx=5, pady=5)

txt_dest_path = tk.Entry(frame_path)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=3, padx=5, pady=5)  # 높이 변경

btn_dest_path = tk.Button(frame_path, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = tk.LabelFrame(root, text="옵션")
frame_option.pack(ipady=5, padx=5, pady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = tk.Label(frame_option, text="가로 넓이", width=10)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=7)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블
lbl_space = tk.Label(frame_option, text="간격", width=10)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=7)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = tk.Label(frame_option, text="파일 포맷", width=10)
lbl_format.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=7)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Progress Bar
frame_prog = tk.LabelFrame(root, text="진행 상황")
frame_prog.pack(fill="x", ipady=5, padx=5, pady=5)

p_var = tk.DoubleVar()
prog_bar = ttk.Progressbar(frame_prog, maximum=100, variable=p_var)
prog_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
frame_run = tk.Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = tk.Button(frame_run, text="시작", padx=5, pady=5, width=12, command=start)
btn_close = tk.Button(frame_run, text="닫기", padx=5, pady=5, width=12)

btn_close.pack(side="right", padx=5, pady=5)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()
