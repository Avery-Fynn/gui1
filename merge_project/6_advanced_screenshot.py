from PIL import ImageGrab
import time
import keyboard


def screenshot():
    # 2020년 6월 1 일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("img{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # f9 누르면 스크린샷 저장

keyboard.wait("esc")  # 사용자가 esc 누를때까지 프로그램 수행
