# Commands 
# pip install -r requirements.txt
# python -m spacy download en_core_web_sm  # Only needed for spaCy
import nltk
from nltk.chat.util import Chat, reflections
import spacy

# --------- NLTK SECTION (Rule-based) ---------
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there! How can I assist you today?"]
    ],
    [
        r"what is your name\??",
        ["I am a chatbot created for you. What's on your mind?"]
    ],
    [
        r"how are you\??",
        ["I'm doing well, thank you! How can I help you today?"]
    ],
    [
        r"exit|quit|bye",
        ["Bye! Take care. If you need anything else, just ask."]
    ],
]

chat = Chat(pairs, reflections)

# --------- spaCy SECTION (NLP-based) ---------
nlp = spacy.load("en_core_web_sm")

def spacy_response(user_input):
    doc = nlp(user_input)
    # Simple intent/entity demonstration
    if any(ent.label_ == "PERSON" for ent in doc.ents):
        names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        return f"Nice to meet you, {' and '.join(names)}!"
    elif any(token.lemma_ == "weather" for token in doc):
        return "I can't check real-time weather, but I hope it's nice where you are!"
    elif any(token.lemma_ == "name" for token in doc):
        return "My name is Chatbot. What's yours?"
    elif any(token.lemma_ == "help" for token in doc):
        return "How can I assist you? You can ask about my name, greet me, or just have a chat."
    else:
        return "Tell me more about that."

# --------------- Main Chat Loop ---------------
def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' or 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Bye! Take care.")
            break

        # First try NLTK response
        response = chat.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            # Fall back to spaCy-based response
            print("Chatbot:", spacy_response(user_input))

if __name__ == "__main__":
    chatbot()