import sys

# Var dec is un-needed. I am used to C#, sue me.
usrInput = 'NULL'
convOrder = 'NULL'
preConv = 0
postConv = 0
funnyVar = 0
x = 0


def ui_generator(menu_header, menu_input):
    count = 1
    border = "\n|------------------------------\n"
    print(menu_header + border)
    for _ in menu_input:
        print(str(count) + " - " + _)
        count += 1
    print(border + "Please enter number corresponding to action required\n\n")


# print("Fahrenheit to Celsius Conversion\n"
#       "|------------------------------\n"
#       "1 - Fahrenheit -> Celsius\n"
#       "2 - Celsius -> Fahrenheit\n"
#       "|------------------------------\n"
#       "Please enter number corresponding to action required\n"
#       "\n")

# Code was changed to allow easier modularity to UI alongside using a function for more good boy points
ui_generator("Fahrenheit to Celsius Conversion", ["Fahrenheit -> Celsius", "Celsius -> Fahrenheit", "Kelvin -> Celsius",
                                                  "Celsius -> Kelvin", "Kelvin -> Fahrenheit", "Fahrenheit -> Kelvin"])
# x is used to hold the user in the statement until input is done correctly
while x == 0:
    #
    # if usrInput == '1':
    #     convOrder = 'FtC'
    #     x = 1
    # elif usrInput == '2':
    #     convOrder = 'CtF'
    #     x = 1
    # else:
    #     print("Invalid input\n\n")

    # Apparently they added switch statements in 2021.
    # I... didn't actually know this until recently, hence the change.
    usrInput = input()
    match usrInput:
        case "1":
            convOrder = 'FtC'
            x = 1
        case "2":
            convOrder = 'CtF'
            x = 1
        case "3":
            convOrder = 'KtC'
            x = 1
        case "4":
            convOrder = 'CtK'
            x = 1
        case "5":
            convOrder = 'KtF'
            x = 1
        case "6":
            convOrder = 'FtK'
            x = 1
        case other:
            print("Invalid input\n\n")
x = 0
print("\n"
      "\n"
      "Please input amount\n")
while x == 0:
    usrInput = input()
    if usrInput.isdigit():
        print("\n\n")
        preConv = float(usrInput)
        x = 1
    else:
        # The actions of funnyVar are unneeded. However, it is only minimal added code to add a hint of humour
        if funnyVar == 0:
            print("That is not a number, how did you mess up typing in a number, like actually, "
                  "it's right at the top of your keyboard, as bright as day, at the top of your keyboard. "
                  "If you try to type in another string you are going to make me cry.\n\n")
            funnyVar = 1
        else:
            sys.exit("Alright buddy, I've had it up to here ^ with you")
# if convOrder == 'FtC':
#     postConv = ((preConv - 32) * 5 / 9)
# elif convOrder == 'CtF':
#     postConv = ((preConv * (9 / 5)) + 32)
# else:
#     sys.exit("What?")
match convOrder:
    case 'FtC':
        postConv = ((preConv - 32) * (5/9))
    case 'CtF':
        postConv = ((preConv * (9/5)) + 32)
    case 'KtC':
        postConv = (preConv - 273.15)
    case 'CtK':
        postConv = (preConv + 273.15)
    case 'KtF':
        postConv = ((preConv * (9/5)) - 459.67)
    case 'FtK':
        postConv = ((preConv + 459.67) * (5/9))
    case other:
        sys.exit("Bruh.")

print("Your converted variable is -  " + str(postConv))
