import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you?"]),
    (r"how are you?", ["I'm good, thanks for asking!", "I'm doing great, how about you?"]),
    (r"what is your name?", ["I am a chatbot created to assist you.", "I don't have a name, but you can call me Bot."]),
    (r"quit|exit|bye", ["Goodbye! Take care.", "Bye! Have a nice day!"]),
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", 
                        "Why don't programmers like nature? It has too many bugs!"]),
    (r"(.*)", ["I'm not sure what you mean, could you clarify?", "Sorry, I didn't quite understand that."])
]


def chat_with_bot():
    print("Hi! I'm your friendly chatbot. Type 'quit' or 'exit' to end the conversation.")
    
    chatbot = Chat(pairs, reflections)
    
    
    chatbot.converse()


if __name__ == "__main__":
    chat_with_bot()
