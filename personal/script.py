import tkinter as tk

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operations = ["+", "-", "x", "÷"]

def pos_or_neg(num):
    if num.startswith("-"):
        return False
    else: return True

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.num1 = ""
        self.num2 = ""
        self.operation = ""
        self.stage = 1 #if 1, then typing num1, if 2, then typing num2
        self.create_widgets()

        #bring window to front and focus
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()

    def setup_window(self):
        self.root.title("Calculator")

    def calculate(self):
        if self.num1.endswith("."):
            self.num1 = self.num1[:-1]
        if self.num2.endswith("."):
            self.num2 = self.num2[:-1]

        if "%" in self.num1:
            print("% found in num1, attempting to format")
            self.num1 = self.num1.replace("%", "")
            self.num1 = float(self.num1) / 100
        if "%" in self.num2:
            print("% found in num2, attempting to format")
            self.num2 = self.num2.replace("%", "")
            self.num2 = float(self.num2) / 100

        if self.num1 == "-":
            self.num1 = "-1"
        if self.num2 == "-":
            self.num2 = "-1"

        float1 = float(self.num1)
        float2 = float(self.num2)
        result = ""
        div_zero_error = False
        if self.operation == "+": result = float1 + float2
        elif self.operation == "-": result = float1 - float2
        elif self.operation == "x": result = float1 * float2
        elif self.operation == "÷":
            if float2 != 0: result = float1 / float2
            else:
                print("Can't divide by zero, nothing happened.")
                div_zero_error = True
        else: print("Invalid operation")
        if not div_zero_error:
            if result.is_integer(): result = int(result)
            result = str(result)
            self.num1 = result
            self.operation = ""
            self.num2 = ""
            self.stage = 1

    def staging_error(self):
        print(f"Something went wrong with staging, current in stage: {self.stage}")

    def button_clicked(self, value):
        if value in numbers:
            if self.stage == 1: self.num1 += str(value)
            elif self.stage == 2: self.num2 += str(value)
            else: self.staging_error()

        elif value in operations:
            if self.stage == 1:
                if self.num1 != "":
                    self.operation = value
                    self.stage = 2
            elif self.stage == 2: print("Input operation, nothing happened")
            else: self.staging_error()

        elif value == "<x":
            if self.stage == 1:
                if len(self.num1) < 1:
                    print("Nothing in entry, nothing was done.")
                else: self.num1 = self.num1[:-1]

            elif self.stage == 2:
                if len(self.num2) < 1:
                    print("Nothing in num2, deleting from operation.")
                    self.operation = ""
                    self.stage = 1
                else: self.num2 = self.num2[:-1]

            else: self.staging_error()

        elif value == "AC":
            self.num1 = ""
            self.operation = ""
            self.num2 = ""
            self.stage = 1

        elif value == "%":
            if self.stage == 1:
                if "%" not in self.num1: self.num1 += "%"
            elif self.stage == 2:
                if "%" not in self.num2: self.num2 += "%"
            else: self.staging_error()

        elif value == ".":
            if self.stage == 1:
                if "." not in self.num1: self.num1 += "."
            elif self.stage == 2:
                if "." not in self.num2: self.num2 += "."
            else: self.staging_error()

        elif value == "+/-":
            if self.stage == 1:
                if pos_or_neg(self.num1):
                    self.num1 = "-" + self.num1
                else:
                    self.num1 = self.num1[1:]
            elif self.stage == 2:
                if pos_or_neg(self.num2):
                    self.num2 = "-" + self.num2
                else:
                    self.num2 = self.num2[1:]
            else: self.staging_error()

        elif value == "=":
            if self.num1 != "" and self.operation != "" and self.num2 != "": self.calculate()
        else: print("Input error")

        self.display_label.config(text=self.num1 + self.operation + self.num2)

        #debugging
        print("--------------")
        print(f"Num1: {self.num1}")
        print(f"Operation: {self.operation}")
        print(f"Num2: {self.num2}")
        print(f"Stage: {self.stage}")

    def create_widgets(self):
        self.display_label = tk.Label(self.root, bg="white", fg="black", height=2, width=24)
        self.display_label.grid(column=1, row=1, columnspan=4)

        buttons = ["<x", "AC", "%", "÷", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]

        column = 0
        row = 2
        for i in buttons:
            button = tk.Button(
                self.root,
                text = i,
                command = lambda n = i: self.button_clicked(n),
                height = 2,
                width = 2,
            )
            column += 1
            if column == 5:
                row += 1
                column = 1
            button.grid(column=column, row=row)

    def run(self): self.root.mainloop()

if __name__ == '__main__': Calculator().run()