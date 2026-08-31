# Basic Chatbot
# CodeAlpha Internship - Task 4

from datetime import datetime


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hello! 👋 How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great! 😊 Thanks for asking."

    elif "your name" in user_input:
        return "I'm CodeAlpha Bot 🤖."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    elif "help" in user_input:
        return (
            "You can ask me about the time, date, "
            "my name, or simply say hello!"
        )

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I don't understand that yet. 🤔"


def main():
    print("=" * 45)
    print("🤖 Welcome to CodeAlpha Basic Chatbot!")
    print("Type 'help' to see what I can do.")
    print("Type 'bye', 'exit', or 'quit' to stop.")
    print("=" * 45)

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()