import keyboard
import time

def main():
    print("Press 'q' to start.")
    keyboard.wait('q')

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while True:
        for number in numbers:
            keyboard.press_and_release(number)
            time.sleep(0.1)
            # Hold 'e' for 3 seconds
            keyboard.press('e')
            time.sleep(3)
            keyboard.release('e')
            time.sleep(32)
            # Hold 'e' for 3 seconds again
            keyboard.press('e')
            time.sleep(3)
            keyboard.release('e')
            time.sleep(2)

if __name__ == "__main__":
    main()
