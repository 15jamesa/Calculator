from appJar import gui

numberstore = ""

# Result of button pressed
def press(btn):
    calc.setLabel("Screen", btn)
    press.button = int(btn)
    calc.setLabel("Screen", press.button)
    global numberstore
    numberstore = int(str(numberstore) + str(press.button))
    press.button = numberstore
    calc.setLabel("Screen", press.button)

# Result of operation button being pressed
def op(sign):
    calc.setLabel("Screen", sign)
    op.operation = sign
    global numberstore
    numberstore = ""
    if op.operation != "x^2":
        num1 = press.button
        store1(num1)


# Result of equals being pressed
def pressLast(equal):
    try:
        op.operation
    except AttributeError:
        calc.setLabel("Screen", "Error: Please enter a valid operation \nSelect 'Clear' to continue")
        calc.setFg("Red", "Screen")
    #operation = op.operation
    num2 = int(press.button)
    if op.operation == "x^2":
        op.result = num2 * num2
    else:
        global numberstore
        numberstore = ""
        if op.operation == "+":
            num1 = int(store1.num1)
            op.result = num1 + num2
        elif op.operation == "-":
            num1 = int(store1.num1)
            op.result = num1 - num2
        elif op.operation == "X":
            num1 = int(store1.num1)
            op.result = num1 * num2
        else:
            pass
    press(op.result)


# Store of button presses
def store1(num1):
    store1.num1 = num1


# Result of "clear" being pressed
def clear(btn):
    calc.setLabel("Screen", "")
    calc.setFg("Black", "Screen")
    global numberstore
    numberstore = ""
    store1.num1 = ""
    op.operation = ""
    op.result = ""
    del store1.num1
    del op.operation
    del op.result


# Calculator Layout
calc = gui("Calculator", "300x450")
calc.setStretch("both")
calc.setSticky("nesw")

# Calculator Screen
calc.addLabel("Screen", "", 0, 0, 4, 1)
calc.setLabelBg("Screen", "white")

# Calculator Buttons
calc.addButton("1", press, 1, 0)
calc.addButton("2", press, 1, 1)
calc.addButton("3", press, 1, 2)
calc.addButton("4", press, 2, 0)
calc.addButton("5", press, 2, 1)
calc.addButton("6", press, 2, 2)
calc.addButton("7", press, 3, 0)
calc.addButton("8", press, 3, 1)
calc.addButton("9", press, 3, 2)
calc.addButton("0", press, 4, 1)
calc.addButton("+", op, 1, 3)
calc.addButton("-", op, 2, 3)
calc.addButton("x^2", op, 3, 3)
calc.addButton("X", op, 4, 3)
calc.addButton("=", pressLast, 5, 0, 4)
calc.addButton("Clear", clear, 6, 0, 4)

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
calc.setButtonBg("X", "LightSkyBlue")
calc.setButtonBg("=", "CornflowerBlue")
calc.setButtonBg("Clear", "LightBlue")

calc.go()
