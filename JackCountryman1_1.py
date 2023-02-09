def main():                        #complete
    groceries = [0,0,0]
    cost = [0,0,0]
    choice = 'q'
    while (choice != 'x'):
        choice = main_menu()
        if (choice == 's'):
            selection = -123
            while (selection != '1' and selection != '2' and selection != '3'):
                selection = cart_menu()
                if(selection == '1'):
                    print("\nAdded cookie")
                if(selection == '2'):
                    print("\nAdded sandwich")
                if(selection == '3'):
                    print("\nAdded water")
                groceries[int(selection)-1] = groceries[int(selection)-1] + 1
    cost[0] = groceries[0] * 1.5
    cost[1] = groceries[1] * 4
    cost[2] = groceries[2] * 1
    total = 0
    for x in cost:
        total += x
        x = str(x)
    print("----------------------------------")
    print("\n("+str(groceries[0])+") - Cookie = ${:.2f}".format(cost[0]))
    print("\n("+str(groceries[1])+") - Sandwich = ${:.2f}".format(cost[1]))
    print("\n("+str(groceries[2])+") - Water = ${:.2f}".format(cost[2]))
    print("\n----------------------------------")
    print("\nGRAND TOTAL = ${:.2f}".format(total))
    print("\n----------------------------------")



def main_menu():      #complete
    print("\n----MAIN MENU----\n\ns: Shop\n\nx: Exit")
    option = input("\nOption: ").lower().strip()
    if(option != 's' or option != 'x'):
        while (option != 'x' and option != 's'):
                option = input("\nInvalid (s\\x):").lower().strip()
    return option

def cart_menu():      #complete
    print("\n----CART MENU----\n\n1: Cookie - $1.50\n\n2: Sandwich - $4.00\n\n3: Water - $1.00")
    choice = input("\nItem: ").strip()
    while (choice != '1' and choice != '2' and choice != '3'):
        choice = input("\nInvalid (1-3):").strip()
    return choice

main()