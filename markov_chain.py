import random


def load_corpus(filename):
    with open(filename, "r") as file:
        corpus = file.read()
    return corpus


def build_markov_chain(corpus, chain_size=1):
    words = corpus.split()
    markov_chain = {}
    for i in range(len(words) - chain_size):
        current_tuple = tuple(words[i : i + chain_size])
        next_word = words[i + chain_size]
        if current_tuple in markov_chain:
            markov_chain[current_tuple].append(next_word)
        else:
            markov_chain[current_tuple] = [next_word]
    return markov_chain


def generate_text(markov_chain, chain_size=1, text_length=50):
    current_tuple = random.choice(list(markov_chain.keys()))
    generated_words = list(current_tuple)
    for _ in range(text_length - chain_size):
        next_word_options = markov_chain.get(current_tuple)
        if not next_word_options:
            break
        next_word = random.choice(next_word_options)
        generated_words.append(next_word)
        current_tuple = tuple(generated_words[-chain_size:])
    return " ".join(generated_words)


corpus = load_corpus("input.txt")
chain_size = 2
markov_chain = build_markov_chain(corpus, chain_size)

generated_text = generate_text(markov_chain, chain_size, text_length=20)
print("Generated Text: ", generated_text)
