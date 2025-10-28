
def addition(number_1, number_2):
    add_answer = number_1 + number_2
    rounded_number = round(add_answer, 2)
    return rounded_number

def subtraction(number_1, number_2):
    sub_answer = number_1 - number_2
    rounded_number = round(sub_answer, 2)
    return rounded_number

def multiplication(number_1, number_2):
    mult_answer = number_1 * number_2
    rounded_number = round(mult_answer, 2)
    return rounded_number

def division(number_1, number_2):
    if number_2 == 0:
        return ZeroDivisionError
    else:
        div_answer = number_1 / number_2
        rounded_number = round(div_answer, 2)
        return rounded_number

def main():
    print("Welcome to the meh-thematical calculator I guess.")
    number_1 = float(input(f"Give me your first number or don't I don't care, I already know the answer anyways...:"))
    print("Even though you should probably already know this I guess Ill still tell you that '+' mean addition, '-' means subtraction, '*' means multiplication, and '/' means division.")
    symbol = input(f"Do you want to +, -, *, / ?:")
    number_2 = float(input(f"I guess I'll take your second number now or whatever:"))


    if symbol == '+':
        print (f"{number_1} + {number_2} = {addition(number_1, number_2)}, got it? Now can you give me a one star review so I can get fired and not have to do this boring job anymore. ")

    if symbol == '-':
        print (f"Ok. {number_1} - {number_2} = {subtraction(number_1, number_2)}, do you need any more obvious math questions to be answered? Too bad. Im on break now sooooo I won't help you either way.")

    if symbol == '*':
        print (f"Ez. {number_1} - {number_2} = {multiplication(number_1, number_2)}, duh. Give me a challenge.")

    if symbol == '/'and number_2 == 0:
        print("You think you're so funny don't you. Incase you didnt remember, dividing a number by 0 is impossible. Thanks for wasting my time. ")
        

    if symbol == '/':
        print (f"Ok, are you sure you want the answer to this insanely hard question... {number_1} / {number_2} = {division(number_1, number_2)}. Great, can I go home now.")

if __name__ == "__main__":
    main()
