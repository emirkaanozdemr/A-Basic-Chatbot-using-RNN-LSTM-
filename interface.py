import nltk
from tensorflow.keras.models import load_model
from nltk.stem import SnowballStemmer
import numpy as np
import random
nltk.download('punkt')
stemmer = SnowballStemmer("english")
model=load_model("chatbot.h5")
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)
def chat():
    print('You can type (write "quit" to exit)!')
    context = []
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        context.append(inp)
        if len(context) > sequence_length:
            context = context[-sequence_length:]

        bags = [bag_of_words(msg, words) for msg in context]
        bags = np.array(bags)
        bags = np.reshape(bags, (1, sequence_length, len(words)))

        results = model.predict(bags)[0]
        print(results)
        results_index = np.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.70:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            print(random.choice(responses))
        else:
            print("I didn't fully understand. Can you rephrase that?")

if __name__ == "__main__":
    chat()