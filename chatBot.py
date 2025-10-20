# ------ Chatbot ------
#  Mehak Farman

print("Hello! I’m Chatty, your friendly Python chatbot.")
print("Type 'bye' anytime to end our chat.\n")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Chatty: Hey there!  How are you doing today?")

    elif "how are you" in user:
        print("Chatty: I’m just a bunch of Python code, but I’m feeling great! What about you?")

    elif "your name" in user:
        print("Chatty: My name’s Chatty — nice to meet you!")

    elif "thank" in user:
        print("Chatty: Aww, you’re so kind! You’re welcome ")

    elif "bye" in user or "exit" in user:
        print("Chatty: Bye-bye! Have a wonderful day ahead ")
        break

    else:
        print("Chatty: Hmm... I’m not sure what that means but I’ll learn someday!")
