import tkinter as tk

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operations = ["+", "-", "*", "/"]

def pos_or_neg(num):
    if float(num) < 0:
        return False
    else: return True

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.display = ""
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        self.stage = 1 #if 1, then typing num1, if 2, then typing operation, if 3, then typing num2
        self.create_widgets()

    def setup_window(self):
        self.root.title("Calculator")
        self.root.geometry("300x400")

    def calculate(self):
        float1 = float(self.num1)
        float2 = float(self.num2)
        if self.operation == "+":
            self.display = float1 + float2
        if self.operation == "-":
            self.display = float1 - float2
        if self.operation == "*":
            self.display = float1 * float2
        if self.operation == "/":
            self.display = float1 / float2

        self.display_label.config(text=self.display)

    def staging_error(self):
        print(f"Something went wrong with staging, current in stage: {self.stage}")

    def button_clicked(self, value):

        if value in numbers:
            if self.stage == 1:
                self.display += str(value)
                self.num1 += str(value)

            elif self.stage == 2:
                print("Number inputted into operation, nothing was done.")

            elif self.stage == 3:
                self.display += str(value)
                self.num2 += str(value)
            else: self.staging_error()

        elif value in operations:
            if self.stage == 2:
                self.display += value
                self.operation = value
                self.stage = 3
            else: self.staging_error()

        elif value == "DELETE":
            if len(self.display) < 1: print("Nothing in entry, nothing was done. ")
            else: self.display = self.display[:-1] #delete from overall display

            if self.stage == 1:
                if len(self.num1) < 1:
                    print("Nothing in entry, nothing was done.")
                else: self.num1 = self.num1[:-1]

            elif self.stage == 2:
                if len(self.operation) < 1:
                    print("Nothing in operation, deleting from num1.")
                    self.num1 = self.num1[:-1]
                else: self.operation = self.operation[:-1]

            elif self.stage == 3:
                if len(self.num2) < 1:
                    print("Nothing in num2, deleting from operation.")
                    self.operation = self.operation[:-1]
                else: self.num2 = self.num2[:-1]

            else: self.staging_error()

        elif value == "AC":
            self.display = ""
            self.num1 = ""
            self.operation = ""
            self.num2 = ""
            self.stage = 1

        elif value == "%":
            if self.stage == 1:
                self.display += "%"
                self.num1 /= 100

            elif self.stage == 2:
                print("Number modifier inputted into operation, nothing was done.")

            elif self.stage == 3:
                self.display += "%"
                self.num2 /= 100

            else: self.staging_error()

        elif value == ".":
            if self.stage == 1:
                self.display += "."
                self.num1 += "."

            elif self.stage == 2:
                print("Number modifier inputted into operation, nothing was done.")

            elif self.stage == 3:
                self.display += "."
                self.num2 += "."

            else: self.staging_error()

        elif value == "+/-":
            if self.stage == 1:
                if pos_or_neg(self.num1):
                    self.display




        elif value == "=":
            self.calculate()

        self.display_label.config(text=self.display)

        #debugging
        print("--------------")
        print(self.display)
        print(self.num1)
        print(self.operation)
        print(self.num2)

    def create_widgets(self):
        #display label
        self.display_label = tk.Label(
            self.root,
            text=self.display,
            bg="gray",
            fg="black",
            font=("Arial", 12),
            width=20,
            height=2,
        )
        self.display_label.grid(column=2, row=0, columnspan=2)

        #number buttons
        starting_column = 1
        column = starting_column + 3
        starting_row = 3
        row = starting_row
        for i in range(10):
            button = tk.Button(
                self.root,
                text=str(9 - i),
                command=lambda num=9 - i: self.button_clicked(num),
            )
            column -= 1
            if column == 0:
                row += 1
                if row == starting_row + 3:
                    column = 2
                else:
                    column = 3
            button.grid(row=row, column=column)

        #operator buttons
        addition = tk.Button(
            self.root,
            text="+",
            command=lambda: self.button_clicked("+"),
        )
        addition.grid(row=starting_row + 2, column=starting_column + 3)

        subtraction = tk.Button(
            self.root,
            text="-",
            command=lambda: self.button_clicked("-"),
        )
        subtraction.grid(row=starting_row + 1, column=starting_column + 3)

        multiplication = tk.Button(
            self.root,
            text="x",
            command=lambda: self.button_clicked("*"),
        )
        multiplication.grid(row=starting_row, column=starting_column + 3)

        division = tk.Button(
            self.root,
            text="÷",
            command=lambda: self.button_clicked("/"),
        )
        division.grid(row=starting_row - 1, column=starting_column + 3)

        equal = tk.Button(
            self.root,
            text="=",
            command=lambda: self.button_clicked("="),
        )
        equal.grid(row=starting_row + 3, column=starting_column + 3)

        percent = tk.Button(
            self.root,
            text="%",
            command=lambda: self.button_clicked("%"),
        )
        percent.grid(row=starting_row - 1, column=starting_column + 2)

        ac = tk.Button(
            self.root,
            text="AC",
            command=lambda: self.button_clicked("AC"),
        )
        ac.grid(row=starting_row - 1, column=starting_column + 1)

        delete = tk.Button(
            self.root,
            text="<x",
            command=lambda: self.button_clicked("DELETE"),
        )
        delete.grid(row=starting_row - 1, column=starting_column)

        decimal = tk.Button(
            self.root,
            text=".",
            command=lambda: self.button_clicked("."),
        )
        decimal.grid(row=starting_row + 3, column=starting_column + 2)

        posNeg = tk.Button(
            self.root,
            text="+/-",
            command=lambda: self.button_clicked("+/-"),
        )
        posNeg.grid(row=starting_row + 3, column=starting_column)


    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = Calculator()
    app.run()