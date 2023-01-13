import os
import tkinter as tk  # __all__
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox
from tkinter import ttk

from PIL import Image

root = tk.Tk()
root.resizable(False, False)
root.title("Image Merger")


def add_file():
    """파일 추가"""
    files = fd.askopenfilenames(
        title="이미지 파일을 선택하세요",
        filetypes=(
            ("PNG 파일", "*.png"),
            ("모든 파일", "*.*"),
        ),
        initialdir=r"C:\Dev\gui",  # 최초에 보여줄 경로
    )
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(tk.END, file)


def del_file():
    """선택 파일 삭제"""
    for idx in reversed(list_file.curselection()):
        list_file.delete(idx)


def browse_dest_path():
    """저장 경로 (폴더)"""
    folder_selected = fd.askdirectory()
    if folder_selected == "":  # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0, tk.END)
    txt_dest_path.insert(0, folder_selected)


def get_options():
    """옵션 가져오기"""
    # 1. 가로 너비
    img_width = cmb_width.get()
    if img_width == "원본유지":
        img_width = -1  # -1 일때는 원본 기준으로
    else:
        img_width = int(img_width)

    # 2. 간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 20
    elif img_space == "보통":
        img_space = 40
    elif img_space == "넓게":
        img_space = 60
    else:  # 없음
        img_space = 0

    # 3. 포맷
    img_format = cmb_format.get().lower()

    return (img_width, img_space, img_format)


def merge_image():
    """이미지 통합"""
    try:
        # 옵션 불러오기
        (img_width, img_space, img_format) = get_options()

        # 이미지 불러오기
        images = [Image.open(x) for x in list_file.get(0, tk.END)]

        # [(width1, height1), (width2, height2), ...]
        image_sizes = [x.size for x in images]  # 원본 사이즈
        if img_width != -1:  # 가로 너비 변경
            image_sizes = [(int(img_width), int(img_width * x[1] / x[0])) for x in image_sizes]

        # 최대 너비, 전체 높이
        widths, heights = zip(*image_sizes)
        max_width, total_height = max(widths), sum(heights)
        if img_space > 0:
            total_height += img_space * (len(images) - 1)

        # 스케치북 준비
        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))  # 배경 흰색
        y_offset = 0  # y 위치

        for idx, img in enumerate(images):
            # 이미지 크기 조정
            img = img.resize(image_sizes[idx])

            # 이미지 삽입
            result_img.paste(img, (int((max_width - img.size[0]) / 2), y_offset))
            y_offset += img.size[1] + img_space  # height + 간격 만큼 더해줌

            # 진행도 반영
            p_var.set((idx + 1) / len(images) * 100)  # 실제 percent 정보를 계산
            prog_bar.update()

        # 지정 경로에 저장
        dest_path = os.path.join(txt_dest_path.get(), "merged_photo." + img_format)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")

    # 예외 처리
    except Exception as err:  # pylint: disable=broad-except
        msgbox.showerror("에러", err)


def start():
    """시작"""
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_image()


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

# 1. 가로 너비 옵션
# 가로 너비 레이블
lbl_width = tk.Label(frame_option, text="가로 너비", width=10)
lbl_width.pack(side="left", padx=5, pady=5)

# 가로 너비 콤보
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
btn_close = tk.Button(frame_run, text="닫기", padx=5, pady=5, width=12, command=root.quit)

btn_close.pack(side="right", padx=5, pady=5)
btn_start.pack(side="right", padx=5, pady=5)

root.mainloop()
