while(True):
    
    print("Menu:\n 0.Paneer Punjabi\n 1.hakka noodles\n 2.Manchurian\n 3.Gulab-jamun\n 4.french fries\n 5.burger\n ");
    choice=int(input("what Do you want to do?\n 1=delete item from menu\n 2=Find item according to Its number\n 3=Add item\n"));
    item_name=["Paneer Punjabi","hakka noodles", "Manchurian","Gulab-jamun","french fries","burger"]
    if choice ==1:
        n=int(input("Enter The number of item You want to delete: "))
        item_name.pop(n);
        print("Items are {} ".format(item_name))
    if choice ==2:
        find=int(input("Enter the number of the food you want to find: "))
        x=item_name.pop(find);
        print("You are finding {} ".format(x))
    if choice == 3:
        name=input("Enter the name of item you want to add: ")
        item_name.append(name)
        print("The total items are {}.".format(item_name))
    choice2=input("Do you wish to continue(y/n): ")
    if (choice2== "n"):
        exit()
    else:
        pass
