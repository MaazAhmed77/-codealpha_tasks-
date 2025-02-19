import nltk
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections  

nltk.download('punkt')


pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hey there! What can I do for you?']),
    (r'how are you?', ['I am doing well, thank you! How about you?', 'I am great! How are you?']),
    (r'I am (good|great|fine|okay|doing well)', ['That’s awesome! How can I assist you today?']),
    (r'what is your name?', ['I am a chatbot. You can call me Chatbot!']),
    (r'bye|goodbye|see you|exit', ['Goodbye! Have a nice day!', 'Take care!']),
    (r'(.*) your name(.*)', ['I am just a simple chatbot! You can call me Chatbot.']),
    (r'(.*) help(.*)', ['Of course! How can I assist you today?']),
    (r'(.*)', ['Sorry, I didn’t quite understand that. Can you rephrase?'])
]

chatbot = Chat(pairs, reflections)

def send_message():
    user_input = entry_box.get().strip()
    if not user_input:
        return

    chat_box.config(state=tk.NORMAL)  # Enable editing
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    entry_box.delete(0, tk.END)


    if user_input.lower() in ['bye', 'goodbye', 'exit', 'see you']:
        chat_box.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n", "bot")
        chat_box.config(state=tk.DISABLED)
        root.after(2000, root.quit)  # Close after 2 seconds
        return


    response = chatbot.respond(user_input)
    chat_box.insert(tk.END, f"Chatbot: {response}\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)  


root = tk.Tk()
root.title("AI Chatbot")
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#E8E8E8")


chat_box = scrolledtext.ScrolledText(root, bg="white", fg="black", font=("Arial", 12), wrap=tk.WORD, height=20)
chat_box.config(state=tk.DISABLED)
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")
chat_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)


entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.pack(pady=5, padx=10, fill=tk.X)


send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(pady=5)


root.bind('<Return>', lambda event: send_message())



root.mainloop()
