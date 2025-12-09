import tkinter as tk
from idlelib.configdialog import font_sample_text

from terminalFormatting import color_text as color
from terminalFormatting import clear_screen as cs

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
        self.scientific_calculator = False
        self.scientific_calculator_2nd = False

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
            print(color("% found in num1, attempting to format", "red"))
            self.num1 = self.num1.replace("%", "")
            self.num1 = float(self.num1) / 100
        if "%" in self.num2:
            print(color("% found in num2, attempting to format", "red"))
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
                print(color("Can't divide by zero, nothing happened.", "red"))
                div_zero_error = True
        else: print(color("Invalid operation"), "red")
        if not div_zero_error:
            if result.is_integer(): result = int(result)
            result = str(result)
            self.num1 = result
            self.operation = ""
            self.num2 = ""
            self.stage = 1

    def staging_error(self):
        print(color(f"Something went wrong with staging, current in stage: {self.stage}", "red"))

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
            elif self.stage == 2: print(color("Input operation, nothing happened", "red"))
            else: self.staging_error()

        elif value == "⌫":
            if self.stage == 1:
                if len(self.num1) < 1:
                    print(color("Nothing in entry, nothing was done.", "red"))
                else: self.num1 = self.num1[:-1]

            elif self.stage == 2:
                if len(self.num2) < 1:
                    print(color("Nothing in num2, deleting from operation.", "red"))
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

        elif value == "Mode":
            if self.scientific_calculator:
                self.scientific_calculator = False
            else:
                self.scientific_calculator = True
            self.create_widgets()

        else: print(color(f"Input error: {value}", "red"))

        self.display_label.config(text=self.num1 + self.operation + self.num2)

        #debugging
        cs()
        print(f"Num1: {self.num1}")
        print(f"Operation: {self.operation}")
        print(f"Num2: {self.num2}")
        print(f"Stage: {self.stage}")
        print(f"Scientific Calculator: {self.scientific_calculator}")

    def create_widgets(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Button, tk.Label)):
                widget.destroy()

        buttons = ["⌫", "AC", "%", "÷", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]
        scientific_buttons = ["(", ")", "mc", "m+", "m-", "mr", "2nd", "x²", "x³", "xʸ", "eˣ", "10ˣ", "1/x", "√x", "∛x", "ʸ√x", "ln", "log₁₀", "x!", "sin", "cos", "tan", "e", "EE", "Rand", "sinh", "cosh", "tanh", "π", "Rad"]
        scientific_buttons_2nd = ["(", ")", "mc", "m+", "m-", "mr", "2nd", "x²", "x³", "xʸ", "yˣ", "2ˣ", "1/x", "√x", "∛x", "ʸ√x", "logy", "log2", "x!", "sin⁻¹", "con⁻¹", "tan⁻¹", "e", "EE", "Rand", "sinh⁻¹", "cosh⁻¹", "tanh⁻¹", "π", "Rad"]
        column = 0
        row = 2

        if self.scientific_calculator:
            for i in scientific_buttons:
                button = tk.Button(
                    self.root,
                    text = i,
                    command = lambda n = i: self.button_clicked(n),
                    font=("Courier", 15),
                    height = 2,
                    width = 2,
                )
                column += 1
                if column == 7:
                    row += 1
                    column = 1
                button.grid(column=column, row=row)

        column = 6
        row = 2
        for i in buttons:
            button = tk.Button(
                self.root,
                text = i,
                command = lambda n = i: self.button_clicked(n),
                font = ("Courier", 15),
                height = 2,
                width = 2,
            )
            column += 1
            if column == 11:
                row += 1
                column = 7
            button.grid(column=column, row=row)

        self.display_label = tk.Label(self.root, bg="white", fg="black", height=2, width=53 if self.scientific_calculator else 17)
        self.display_label.grid(column=1 if self.scientific_calculator else 7, row=1, columnspan=9 if self.scientific_calculator else 3)

        button = tk.Button(
            self.root,
            text = "Mode",
            command = lambda: self.button_clicked("Mode"),
            height = 2,
            width = 2,
            font=("Courier", 15),
        )
        button.grid(column = 10, row=1)


    def run(self): self.root.mainloop()

"""class ScientificCalculator:
    def __init__(self, root, num1, operation, num2, stage):
        self.root = root
        self.num1 = num1
        self.operation = operation
        self.num2 = num2
        self.stage = stage
        
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.focus_force()"""




if __name__ == '__main__': Calculator().run()