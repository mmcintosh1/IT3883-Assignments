# Program Name: Assignment1.py
# Course: IT3883
# Name: Mario McIntosh
# Assignment Number: Assignment 1
# Due Date: 09/22/2026
# Purpose: This program lets the user add, clear, or display text using a menu.

text = ""

while True:
    print("\nMenu")
    print("1. Add text")
    print("2. Clear text")
    print("3. Display text")
    print("4. Exit")

    option = input("Choose an option: ")

    # Adds text to what is already saved
    if option == "1":
        new_text = input("Enter text: ")
        text = text + new_text

    # Clears the saved text
    elif option == "2":
        text = ""
        print("Text cleared")

    # Shows the saved text
    elif option == "3":
        print("Saved text:", text)

    # Ends the program
    elif option == "4":
        print("Program ended")
        break

    # Runs if the user enters something other than 1-4
    else:
        print("Invalid option")
