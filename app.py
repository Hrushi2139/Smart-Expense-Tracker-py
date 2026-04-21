while True:
    print("\n1. Add Expense");
    print("2. View Expense");
    print("3. Exit")
    chOpt=input("Enter your Option: ");
    if chOpt == "1":
        print("Add Expense Selected");
    elif chOpt == "2":
        print("View Expenses Selected");
    elif chOpt == "3":
        print("Exiting...");
        break
    else:
        print("Invalid Option");