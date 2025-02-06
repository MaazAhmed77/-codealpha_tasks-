import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')


pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hey there! What can I do for you?']),
    (r'how are you?', ['I am doing well, thank you! How about you?', 'I am great! How are you?']),
    (r'I am (good|great|fine)', ['That’s awesome! How can I assist you today?']),
    (r'what is your name?', ['I am a chatbot. You can call me Chatbot!']),
    (r'bye|goodbye', ['Goodbye! Have a nice day!', 'Take care!']),
    (r'(.*)', ['Sorry, I didn’t quite understand that. Can you rephrase?'])
]


chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
