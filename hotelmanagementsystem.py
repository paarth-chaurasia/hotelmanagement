

       
       
        print("No Occupied Rooms")

def main():
    while True:
        print("== HOTEL MANAGEMENT SYSTEM ==")
        print("1. Check In")
        print("2. Check Out")
        print("3. Show Vacant Rooms")
        print("4. Show Occupied Rooms")
        print("5. Show All Rooms")
        print("6. Exit")

        choose = input("Pick Option :")

        if choose == "1":
            checkin()
        elif choose == "2":
            checkout()
        elif choose == "3":
            show_vacant_rooms()
        elif choose == "4":
            show_occupied_rooms()
        elif choose == "5":
            show_all_rooms()
        elif choose == "6":
            print("Thank You for using this service")
            break
        else:
            print("Wrong Input")

main()
