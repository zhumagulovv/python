day = 4;

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Looking forward to the weekend")

def get_current_day(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Looking forward to the weekend")

get_current_day(3)
get_current_day(5)

# Combine Values

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is weekday")
    case 6 | 7:
        print("I love weekdays")
    case _:
        print("Looking forward to the weekend")

# If Statements as Guards

month = 12;

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 12:
        print("A weekday in December")
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("A weekday in Junuary")
    case _:
        print("Mo match")
