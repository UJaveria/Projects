# ==============Personal Expense Management System==============
expense_book = []
total_money = 0

while True :
    print("1.Add Expense\n2.View Expenses\n3.Search\n4.Save\n5.Exit")
    op = input("Enter option : ")
    # For storing data

    # Add Expense
    if (op.lower() == "add expnse" or op == "1") :
        Limit = int(input("How many expenses you want to enter : "))
        
        for ex in range(1,Limit+1) :
            name   = input("Product : ")
            quant  = int(input("Quantity: "))
            price  = float(input("Price   : "))
            ctg    = input("Category: ")
            date   = input("Date    : ")

            #Adding Expense to dictionary 
            expense = {}
            expense["Product_name"]   = name
            expense["Pro_Category"]   = ctg
            expense["Pro_Quantity"]   = quant
            expense["Price_p_unit"]   = price
            expense["Total_Amount"]   = price * quant
            expense["Buying__Date"]   = date
            expense_book.append(expense)
            total_money += expense["Total_Amount"]
            print("- "*10)
            print("\n")

    # View Expense
    elif (op.lower() == "view expense" or op == "2") :
        # Displying in readable format

            print("Expense Details ")
            print("- "* 10)
            for data_dict in expense_book :
                for key, value in data_dict.items() :
                    print(f"{key} : {value}")
                print("- " * 10)
            # Total Money spent
            print("Total money you spent :",total_money)
            print("\n")

    # Search Expense
    elif (op.lower() == "search" or op == "3") :
            search_val = input("Enter product name : ")
            found = False
            for data_dict in expense_book :
                if data_dict["Product_name"].lower() == search_val.lower() :
                    for key, value in data_dict.items() :
                        print(f"{key} : {value}")
                    print("Found successfully")
                    found = True
            if not found :
                print("Not found")
            print("\n")

    elif(op.lower() == "save" or op == "4") :
        
        with open("Expenses.txt", "w") as file:
            for data_dict in expense_book:
                file.write(str(data_dict) + "\n")
        print("Save successfuly. ")

    elif(op.lower() == "exit" or op == "5") :
        print("Exit successfully.")
        break
