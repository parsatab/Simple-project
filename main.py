from colorama import Style, Fore

print(Style.BRIGHT)
userList = []

while True:
    print(Fore.YELLOW + "1. Add to list.")
    print("2. Watch your list.")
    print("3. Update(edit) your list.")
    print("4. Delete from list with index number.")
    print("5. Sort your list.")
    print("6. Remove duplicate list members.")
    print("7. Clear all list elements")
    print("8. Exit the program.")

    print(Fore.CYAN)
    option = int(input("Enter your desired option : "))

    if option == 8:
        print(Fore.WHITE)
        exit_or_not = input("Do you want to exit the program?? (yes/no)")

        if exit_or_not == 'yes' or exit_or_not == 'Yes' or exit_or_not == 'y' or exit_or_not == 'Y':
            print(Style.RESET_ALL)
            break
        elif exit_or_not == 'no' or exit_or_not == 'No' or exit_or_not == 'n' or exit_or_not == 'N':
            continue
        else:
            print(Fore.RED + "you return to the main options because you must write yes or no for exit the program or continue.")

    elif option == 1:
        print(Fore.YELLOW + "A. Add number to list.")
        print("B. Add string to list.")

        print(Fore.CYAN)
        int_or_string = input("Enter your desired option : ")

        if int_or_string == 'A':
            print(Fore.GREEN)
            integerInput = int(input("Enter your desired number for add to list : "))
            userList.append(integerInput)
        elif int_or_string == 'B':
            print(Fore.GREEN)
            stringInput = input("Enter your desired string for add to list : ")
            userList.append(stringInput)
        else:
            print(Fore.RED)
            print("You must choice between option A or B.")
            print("You return to the main options.")

    elif option == 2:
        print(Fore.BLUE)
        print(userList)

    elif option == 3:
        print(Fore.CYAN)
        update = int(input("Enter your desired index number from your list for update(edit) : "))
        if update != 0:
            index_count = update - 1
            print(Fore.YELLOW + "A. Replace number to list.")
            print("B. Replace string to list.")
            print(Fore.CYAN)
            number_or_string = input("Enter your desired option : ")

            if number_or_string == 'A':
                print(Fore.CYAN)
                intInput = int(input("Enter your desired number for add to list : "))
                userList[index_count] = intInput
                print(Fore.BLUE)
                print(userList)
            elif number_or_string == 'B':
                print(Fore.CYAN)
                strInput = input("Enter your desired string for add to list : ")
                userList[index_count] = strInput
                print(Fore.BLUE)
                print(userList)
            else:
                print(Fore.RED)
                print("You must choice between option A or B.")
                print("You return to the main options.")
        else:
            print(Fore.RED)
            print("We don't have index zero from list!")

    elif option == 4:
        can_delete_from_userList = len(userList)
        if can_delete_from_userList == 0:
            print(Fore.LIGHTBLUE_EX)
            print("You have no items to delete in your list! \n First you need to add something to the list and then you can remove it.")
        else:
            print(Fore.CYAN)
            delete = int(input("Enter your desired index number from your list for delete : "))
            if delete != 0:
                select_item_for_delete = delete - 1
                userList.pop(select_item_for_delete)
                print(Fore.BLUE)
                print(userList)
            else:
                print(Fore.RED)
                print("We don't have index zero from list!")

    elif option == 5:
        print(Fore.YELLOW + "A. Sort the list in ascending order.")
        print("B. Sort the list in descending order." + Fore.CYAN)
        sorting = input("Enter your desired option: ")

        if sorting == 'A':
            string_sorting = [x for x in userList if isinstance(x, str)]
            integer_sorting = [x for x in userList if isinstance(x, int)]
            string_sorted = sorted(string_sorting)
            integer_sorted = sorted(integer_sorting)
            if string_sorted and integer_sorted:
                userList = string_sorted + integer_sorted
                print(Fore.BLUE)
                print(userList)
            else:
                if len(integer_sorted) == 0:
                    userList = string_sorted
                    print(Fore.BLUE)
                    print(userList)
                else:
                    userList = integer_sorted
                    print(Fore.BLUE)
                    print(userList)
        elif sorting == 'B':
            string_sorting = [x for x in userList if isinstance(x, str)]
            integer_sorting = [x for x in userList if isinstance(x, int)]
            string_sorted = sorted(string_sorting, reverse=True)
            integer_sorted = sorted(integer_sorting, reverse=True)
            if string_sorted and integer_sorted:
                userList = string_sorted + integer_sorted
                print(Fore.BLUE)
                print(userList)
            else:
                if len(integer_sorted) == 0:
                    userList = string_sorted
                    print(Fore.BLUE)
                    print(userList)
                else:
                    userList = integer_sorted
                    print(Fore.BLUE)
                    print(userList)
        else:
            print(Fore.RED)
            print("You must choice between option A or B.")
            print("You return to the main options.")

    elif option == 6:
        userList = list(set(userList))
        print(Fore.BLUE)
        print(userList)

    elif option == 7:
        userList.clear()
        print(f'{Fore.BLUE} {userList}')

    else:
        print(Fore.RED)
        print("Your option is invalid")