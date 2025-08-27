import random

articles = ["the", "a", "an"]
nouns = ["boy", "girl", "dog", "cat", "man", "woman"]
verbs = ["kicked", "jumped", "ran", "walked", "hit"]
adjectives = ["big", "small", "red", "blue", "green", "yellow"]
prepositions = ["on", "in", "to", "over", "under"]
conjunctions = ["and", "but", "or"]

def sentence():
    if random.choice([True, False]):
        adj = random.choice(adjectives) + " "
    else:
        adj = ""

    rand_noun = random.choice(nouns)
    rand_verb = random.choice(verbs)
    rand_article = random.choice(articles)

    sentence = rand_article + " " + adj + rand_noun + " " + rand_verb

    if random.choice([True, False]):
        prep = " " + random.choice(prepositions) + " "
        sentence += prep + random.choice(articles) + " " + random.choice(nouns)

    if random.choice([True, False]):
        conjunction = " " + random.choice(conjunctions) + " "
        sentence += conjunction + sentence()

    return sentence + "."

def main():
    num_sentences = int(input("How many sentences do you want to generate? "))
    for _ in range(num_sentences):
        print(sentence())

if __name__ == "__main__":
    main()
