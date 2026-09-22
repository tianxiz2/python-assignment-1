# Name: Zhu Tianxi
# Assignment One
# ddl is 22/9/2026 23:59pm
import turtle

def show_menu():
    print("\n" + "="*40)
    print("         Welcome to Python Assignment Suite")
    print("="*40)
    print("1. Simple Calculator")
    print("2. QA Bot")
    print("3. Turtle Drawing")
    print("0. Exit Program")
    print("="*40)

def calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")
        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Error: Invalid operation!")
    except ValueError:
        print("Error: Please enter valid numbers!")

def qa_bot():
    print("\n--- QA Bot ---")
    print("You can ask me about: hello, python, jetson, ai, name")
    question = input("Ask me something: ").lower().strip()
    if question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")

def turtle_drawing():
    print("\n--- Turtle Drawing ---")
    print("Drawing a colorful spiral pattern...")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(100):
        t.pencolor(colors[i % len(colors)])
        t.forward(i * 2)
        t.left(59)
    t.hideturtle()
    print("Drawing complete! Close the graphics window to continue.")
    turtle.done()

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-3): ").strip()
        if choice == "1":
            calculator()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            turtle_drawing()
        elif choice == "0":
            print("Thank you for using! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        if choice != "0":
            input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()
