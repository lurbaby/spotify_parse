import pyautogui
import time

def print_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()  # Отримуємо поточні координати курсора
            print(f"Координати курсора: X={x} Y={y}")
            time.sleep(3)  # Затримка в 1 секунду між виводами координат
    except KeyboardInterrupt:
        print("\nПрограма завершена.")

print_mouse_position()
