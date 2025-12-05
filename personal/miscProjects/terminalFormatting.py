import time

def animated_print(text):

    for char in text:
        print(char, end = '', flush = True)
        time.sleep(0.075)
    print()

def color_text(text, color):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"

def rgb_text(text, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def bold_text(text):
    return f"\033[1m{text}\033[0m"

def underline_text(text):
    return f"\033[4m{text}\033[0m"

def highlight_text(text):
    return f"\033[43m{text}\033[0m"  # Yellow background

def bow_text(text):
    return f"\033[3m{text}\033[0m"  # Italic text

def clear_screen():
    print("\033[2J\033[H", end='')  # Clear screen and move cursor to home position

def move_cursor(x, y):
    print(f"\033[{y};{x}H", end='')  # Move cursor to (x, y)

def progress_bar(percentage, width=50):
    filled = int(width * percentage / 100)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {percentage}%"

def reset_formatting():
    print("\033[0m", end='')  # Reset all formatting

def justify_text(text, alignment, width=80):
    if alignment == "left":
        print(text.ljust(width))
    elif alignment == "right":
        print(text.rjust(width))
    elif alignment == "center":
        print(text.center(width))
    else:
        print(text)

def test_formatting():
    clear_screen()
    animated_print("This is an animated print!")
    print(color_text("This is red text.", "red"))
    print(rgb_text("This is custom RGB text.", 128, 0, 128))
    print(bold_text("This is bold text."))
    print(underline_text("This is underlined text."))
    print(highlight_text("This is highlighted text."))
    print(bow_text("This is italic (bow) text."))
    move_cursor(10, 10)
    print("Moved cursor to (10,10)")
    print(progress_bar(75))
    reset_formatting()
    justify_text("This text is left aligned.", "left")
    justify_text("This text is right aligned.", "right")
    justify_text("This text is center aligned.", "center")

if __name__ == '__main__':
    test_formatting()
    for i in range(10):
        print(progress_bar(i * 10) + "\r", end='')
        time.sleep(0.5)
    print(progress_bar(100))
