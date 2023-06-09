def main():
    while True:
        print("Welcome to the Simple Console Application!")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def option1():
    print("You chose Option 1.")
    # Add your code for Option 1 here

def option2():
    print("You chose Option 2.")
    # Add your code for Option 2 here

def option3():
    print("You chose Option 3.")
    # Add your code for Option 3 here

if __name__ == "__main__":
    main()
