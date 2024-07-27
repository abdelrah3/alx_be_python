def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name= input("Enter the item's name ")
            shopping_list.append(item_name)
            
        elif choice == '2':
            item_name2 = input("Enter the item's name to remove ")
            if item_name2 in shopping_list:
                shopping_list.remove(item_name2)
            else:
                print("Item not found")
                    
        elif choice == '3':
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
