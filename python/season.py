month = int(input("enter the month: "))
match month:
    case 12|1|2:
        print("winter")
    case 3|4|5:
        print("spring")
    case 6|7|8:
        print("summer")
    case 9|10|11:
        print("autumn")