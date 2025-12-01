import tkinter as tk

def number_clicked():
    """
    number_clicked
    """

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

column = 1
row = 1
for i in range(10):
    button = tk.Button(
        root,
        text=str(i),
        command = number_clicked,
    )

    button.grid(row=i, column=0)
root.mainloop()