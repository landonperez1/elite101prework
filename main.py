def chatbot():
    print("Welcome to our chatbot!")
    name = input("May I have your name? ")
    age = input("How old are you? ")

    print(f"Thank you, {name}")

    while True:
        print("\nHow can I help you today?")
        print("1. Fun fact")
        print("2. Calculate the sum of two numbers")
        print("3. Tell a joke")
        print("4. Exit the conversation")
        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print("Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible")
        elif choice == "2":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"The sum of {num1} and {num2} is {num1 + num2}.")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "3":
            print("Why don’t scientists trust atoms? Because they make up everything")
        elif choice == "4":
            print("Goodbye! Have a great day")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    chatbot()
