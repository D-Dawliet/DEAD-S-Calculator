# imports
import turtle
import math

# screen_definition
screen = turtle.Screen()
turtle.title("DEAD'S CALCULATOR")
turtle.bgcolor("black")
screen.setup(400, 630, 370, -100)

#Input variables
current_input = ""
symbols = ""
operation_1 = None
operation_2 = None

# number_buttons_co-ordinates
buttons_cd = [
    {"x": -50, "y": 50, "width": 100, "height": 50, "text": "2"},
    {"x": -170, "y": 50, "width": 100, "height": 50, "text": "1"},
    {"x": 70, "y": 50, "width": 100, "height": 50, "text": "3"},
    {"x": -50, "y": -20, "width": 100, "height": 50, "text": "5"},
    {"x": -50, "y": -90, "width": 100, "height": 50, "text": "8"},
    {"x": -170, "y": -20, "width": 100, "height": 50, "text": "4"},
    {"x": -170, "y": -90, "width": 100, "height": 50, "text": "7"},
    {"x": 70, "y": -20, "width": 100, "height": 50, "text": "6"},
    {"x": 70, "y": -90, "width": 100, "height": 50, "text": "9"},
    {"x": -170, "y": -160, "width": 100, "height": 50, "text": "0"},
]

# sign_buttons_co-ordinates
signs_cd = [
    {"x": -50, "y": -160, "width": 100, "height": 50, "sign": "="},
    {"x": 70, "y": -160, "width": 100, "height": 50, "sign": "C"},
    {"x": -170, "y": -230, "width": 50, "height": 50, "sign": "+"},
    {"x": -120, "y": -230, "width": 50, "height": 50, "sign": "-"},
    {"x": -50, "y": -230, "width": 50, "height": 50, "sign": "×"},
    {"x": 0, "y": -230, "width": 50, "height": 50, "sign": "÷"},
    {"x": 70, "y": -230, "width": 50, "height": 50, "sign": "^"},
    {"x": 120, "y": -230, "width": 50, "height": 50, "sign": "√"}
]


# buttons_creating_function
def buttons(dead, x, y, width, height, text):
    dead.penup()
    dead.goto(x, y)
    dead.pendown()
    dead.fillcolor("light blue")
    dead.begin_fill()
    for i in range(2):
        dead.forward(width)
        dead.right(90)
        dead.forward(height)
        dead.right(90)
    dead.end_fill()

    dead.penup()
    dead.goto(x + width//2, y - (10 + height//2))
    dead.write(text, align="center", font=("Arial", 12, "normal"))


# Managing_key_clicks
def key(click_x, click_y):
    global current_input, symbols, operation_1, operation_2
    for button in buttons_cd:
        button_x, button_y = button["x"], button["y"]
        width, height = button["width"], button["height"]
        text = button["text"]
        if button_x <= click_x <= button_x + width and button_y - height <= click_y <= button_y:
            current_input += text
            screen_update()

    for signs in signs_cd:
        sign_x, sign_y = signs["x"], signs["y"]
        width, height = signs["width"], signs["height"]
        sign = signs["sign"]
        if sign_x <= click_x <= sign_x + width and sign_y - height <= click_y <= sign_y:
            if sign == "C":
                current_input = ""
                symbols = ""
                operation_1 = None
                operation_2 = None
            elif sign == "=":
                if operation_1 is not None and symbols and current_input:
                    operation_2 = float(current_input)
                    current_input = str(operation())
                    symbols = ""
                    operation_1 = float(current_input)
                    operation_2 = None
                    screen_update()
            elif sign == "√":
                if current_input:
                    if operation_1 is None:
                        operation_1 = float(current_input)
                        current_input = str(math.sqrt(operation_1))
                        operation_1 = float(current_input)
                    else:
                        current_input = str(math.sqrt(float(current_input)))
                        operation_2 = float(current_input)
                elif operation_1 is not None:
                    current_input = str(math.sqrt(operation_1))
                    operation_1 = float(current_input)
                    operation_2 = None
                screen_update()
            else:
                if current_input:
                    if operation_1 is None:
                        operation_1 = float(current_input)
                        symbols = sign
                        current_input = ""
                    elif operation_1 is not None and symbols and current_input:
                        operation_2 = float(current_input)
                        current_input = str(operation())
                        symbols = sign
                        operation_1 = float(current_input)
                        current_input = ""
                    elif operation_1 is not None and operation_2 is None and not symbols and current_input:
                        operation_2 = float(current_input)
                        current_input = str(operation())
                        symbols = sign
                        operation_1 = float(current_input)
                        current_input = ""

            screen_update()

# Functions_of_signs
def operation():
    global operation_1, operation_2, symbols
    if symbols == "+":
        return operation_1 + operation_2
    elif symbols == "-":
        return operation_1 - operation_2
    elif symbols == "×":
        return operation_1 * operation_2
    elif symbols == "^":
        return operation_1 ** operation_2
    elif symbols == "÷":
        if operation_2 == 0:
            return "Error"
        else:
            return operation_1 / operation_2
    else:
        return operation_1

# screen_update
def screen_update():
    dead.clear()
    interface()
    # creating_button
    dead.begin_fill()
    for button in buttons_cd:
        buttons(dead, button["x"], button["y"], button["width"], button["height"], button["text"])

    for signs in signs_cd:
        buttons(dead, signs["x"], signs["y"], signs["width"], signs["height"], signs["sign"])
    if current_input:
        display = current_input
    else:
        display = ""
    dead.penup()
    dead.goto(-163, 113)
    dead.pendown()
    dead.write(display, align="left", font=("Arial", 17, "normal"))
    turtle.update()


dead = turtle.Turtle()
dead.hideturtle()
turtle.tracer(0, 0)

# creating_buttons
for button in buttons_cd:
    buttons(dead, button["x"], button["y"], button["width"], button["height"], button["text"])

for signs in signs_cd:
    buttons(dead, signs["x"], signs["y"], signs["width"], signs["height"], signs["sign"])

# creating_display
def interface():
    dead.penup()
    dead.goto(-170, 155)
    dead.pendown()
    dead.fillcolor("light blue")
    dead.begin_fill()
    for j in range(2):
        dead.forward(340)
        dead.right(90)
        dead.forward(60)
        dead.right(90)
    dead.end_fill()

    dead.penup()
    dead.goto(-165, 150)
    dead.pendown()

    dead.fillcolor("white")
    dead.begin_fill()
    for j in range(2):
        dead.forward(330)
        dead.right(90)
        dead.forward(50)
        dead.right(90)
    dead.end_fill()

    dead.fillcolor("blue")
    dead.penup()
    dead.goto(130, 110)
    dead.pendown()
    dead.begin_fill()
    dead.write("💋", font=("Arial", 20, "bold"))
    dead.end_fill()


interface()

turtle.update()

turtle.listen()
turtle.onscreenclick(key)

turtle.done()