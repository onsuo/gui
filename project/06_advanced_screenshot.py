import time

import keyboard
from PIL import ImageGrab


def screenshot():
    curr_time = time.strftime("%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save(f"image_{curr_time}.png")


keyboard.add_hotkey("F8", screenshot)  # 사용자가 F9 키를 누르면 스크린샷 저장

keyboard.wait("esc")  # 사용자가 esc 를 누를 때까지 프로그램 수행
