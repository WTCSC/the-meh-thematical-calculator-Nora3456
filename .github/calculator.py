
print("Welcome to the meh-thematical calculator I guess.")
number_1 = float(input(f"Give me your first number or don't I don't care, I already know the answer anyways...:"))
print("Even though you should probably already know this I guess Ill still tell you that '+' mean addition, '-' means subtraction, '*' means multiplication, and '/' means division.")
symbol = input(f"Do you want to +, -, *, / ?:")
number_2 = float(input(f"I guess I'll take your second number now or whatever:"))

def addition():
    add_answer = number_1 + number_2
    return add_answer

def subtraction():
    sub_answer = number_1 - number_2
    return sub_answer

def multiplication():
    mult_answer = number_1 * number_2
    return mult_answer

def division():
    div_answer = number_1 / number_2
    return div_answer

if symbol == '+':
    print (f"{number_1} + {number_2} = {addition()}, got it? Now can you give me a one star review so I can get fired and not have to do this boring job anymore. ")

if symbol == '-':
    print (f"Ok. {number_1} - {number_2} = {subtraction()}, do you need any more obvious math questions to be answered? Too bad. Im on break now sooooo I won't help you either way.")

if symbol == '*':
    print (f"Ez. {number_1} - {number_2} = {multiplication()}, duh. Give me a challenge.")

if symbol == '/'and number_2 == 0:
    print("You think you're so funny don't you. Incase you didnt remember, dividing a number by 0 is impossible. Thanks for wasting my time. ")
if symbol == '/':
    print (f"Ok, are you sure you want the answer to this insanely hard question... {number_1} / {number_2} = {division()}. Great, can I go home now.")

