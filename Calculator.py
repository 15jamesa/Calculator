from appJar import gui

number_store = ""

# Result of button pressed
def press(btn):
    if btn == ".":
        calc.setLabel("Screen", (btn))
        press.button = btn
        calc.setLabel("Screen", press.button)
        global number_store
        number_store = (str(number_store) + str(press.button))
        press.button = number_store
        calc.setLabel("Screen", press.button)
    else:
        btn = float(btn)
        calc.setFg("Black", override=False)
        if (btn - int(btn)) == 0:
            calc.setLabel("Screen", int(btn))
            press.button = int(btn)
            calc.setLabel("Screen", int(press.button))
            number_store = (str(number_store) + str(press.button))
            press.button = number_store
            calc.setLabel("Screen", press.button)
        else:
            calc.setLabel("Screen", float(btn))
            press.button = float(btn)
            calc.setLabel("Screen", float(press.button))
            number_store = (str(number_store) + str(press.button))
            press.button = number_store
            calc.setLabel("Screen", press.button)


# Result of operation button being pressed
def op(sign):
    calc.setFg("Black", override=False)
    calc.setLabel("Screen", sign)
    op.operation = sign
    global number_store
    number_store = ""
    if op.operation != "x^2":
        num1 = press.button
        store1(num1)


# Result of equals being pressed
def press_last():
    try:
        op.operation
    except AttributeError:
        calc.setLabel("Screen", "Error: Please enter a valid Calculation")
        calc.setFg("Red", override=False)
    try:
        press.button
    except AttributeError:
        calc.setLabel("Screen", "Error: Please enter a valid Calculation")
        calc.setFg("Red", override=False)
    press_last.num2 = float(press.button)
    try:
        store1.num1
    except AttributeError:
        calc.setLabel("Screen", "Error: Please enter a valid Calculation")
        calc.setFg("Red", override=False)
    press_last.num2 = float(press.button)
    if op.operation == "x^2":
        press_last.num2 = float(press_last.num2)
        op.result = float(press_last.num2 * press_last.num2)
    else:
        global number_store
        number_store = ""
        if op.operation == "+":
            num1 = float(store1.num1)
            op.result = float(num1 + press_last.num2)
        elif op.operation == "-":
            num1 = float(store1.num1)
            op.result = float(num1 - press_last.num2)
        elif op.operation == "X":
            num1 = float(store1.num1)
            op.result = float(num1 * press_last.num2)
        elif op.operation == "/":
            num1 = float(store1.num1)
            if press_last.num2 == 0:
                calc.setLabel("Screen", "Error: You cannot divide a number by zero")
                calc.setFg("Red", override=False)
            else:
                op.result = float(num1 / press_last.num2)
        else:
            pass
    press(float(op.result))


# Store of button presses
def store1(num1):
    store1.num1 = float(num1)


# Result of "clear" being pressed
def clear():
    calc.setLabel("Screen", "")
    calc.setFg("Black", override=False)
    global number_store
    number_store = ""
    store1.num1 = ""
    op.operation = ""
    op.result = ""
    press_last.num2 = ""
    press.button = ""
    del press_last.num2
    del press.button
    del store1.num1
    del op.operation
    del op.result


#Empty function
def blank():
    pass


# Calculator Layout
calc = gui("Calculator", "300x450")
calc.setStretch("both")
calc.setSticky("nesw")

# Calculator Screen
calc.addLabel("Screen", "", 0, 0, 4, 1)
calc.setLabelBg("Screen", "white")
calc.addButton("", blank, 5, 0)
calc.setButtonBg("", "PaleTurquoise")
calc.setButtonState("", "disabled")

# Calculator Buttons
calc.addButton("1", press, 2, 0)
calc.addButton("2", press, 2, 1)
calc.addButton("3", press, 2, 2)
calc.addButton("4", press, 3, 0)
calc.addButton("5", press, 3, 1)
calc.addButton("6", press, 3, 2)
calc.addButton("7", press, 4, 0)
calc.addButton("8", press, 4, 1)
calc.addButton("9", press, 4, 2)
calc.addButton("0", press, 5, 1)
calc.addButton("+", op, 1, 3)
calc.addButton("-", op, 2, 3)
calc.addButton("/", op, 3, 3)
calc.addButton("x^2", op, 5, 3)
calc.addButton("X", op, 4, 3)
calc.addButton(".", press, 5, 2,)
calc.addButton("Clear", clear, 1, 0, 3)
calc.addButton("=", press_last, 6, 0, 4)

# Button Colours
calc.setButtonBg("0", "PaleTurquoise")
calc.setButtonBg("1", "PaleTurquoise")
calc.setButtonBg("2", "PaleTurquoise")
calc.setButtonBg("3", "PaleTurquoise")
calc.setButtonBg("4", "PaleTurquoise")
calc.setButtonBg("5", "PaleTurquoise")
calc.setButtonBg("6", "PaleTurquoise")
calc.setButtonBg("7", "PaleTurquoise")
calc.setButtonBg("8", "PaleTurquoise")
calc.setButtonBg("9", "PaleTurquoise")
calc.setButtonBg("+", "LightSkyBlue")
calc.setButtonBg("-", "LightSkyBlue")
calc.setButtonBg("x^2", "LightSkyBlue")
calc.setButtonBg("/", "LightSkyBlue")
calc.setButtonBg("X", "LightSkyBlue")
calc.setButtonBg("=", "CornflowerBlue")
calc.setButtonBg(".", "PaleTurquoise")
calc.setButtonBg("Clear", "LightBlue")

calc.go()
