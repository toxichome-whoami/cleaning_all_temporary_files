import pyautogui
import time


def run_command(command):
    time.sleep(1)
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.typewrite(command)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.5)


def delete_files_permanently():
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.1)
    pyautogui.hotkey("shift", "delete")
    time.sleep(1.5)


def press_try_again():
    pyautogui.press("up")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(2.1)


def press_skip():
    pyautogui.press("up")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.press("down")
    time.sleep(0.1)
    pyautogui.press("right")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(2.1)


def close_window():
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.5)


def main():
    for directory in ["%temp%", "temp"]:
        run_command(directory)
        delete_files_permanently()
        press_try_again()
        press_skip()
        close_window()

    run_command("cleanmgr")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)


if __name__ == "__main__":
    main()

