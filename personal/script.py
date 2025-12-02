import tkinter as tk

def number_clicked():

    """
    number_clicked
    """

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")


display = ""
text = tk.Label(
    root,
    text=display,
    bg="white",
    fg="black",
    font=("Arial", 12),
    width=20,
    height=20

)

column = 0
startingRow = 2
row = startingRow
for i in range(10):
    button = tk.Button(
        root,
        name="0" if i == 9 else str(i + 1),
        text= "0" if i == 9 else str(i + 1),
        command = number_clicked

    )
    column += 1
    if column == 4:
        row += 1
        if row == 4: column = 2
        else: column = 1
    button.grid(row=row, column=column)

root.mainloop()