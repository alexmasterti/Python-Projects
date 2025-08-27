import random

def getWords(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return tuple(words)
    except FileNotFoundError:
        print("File not found.")
        return ()

def generate_sentence(nouns, verbs, articles, prepositions, adjectives, conjunctions):
    sentence = ""
    # Determine whether to include an adjective
    if random.choice([True, False]):
        sentence += random.choice(adjectives) + " "

    sentence += random.choice(nouns) + " "
    sentence += random.choice(verbs) + " "
    sentence += random.choice(articles) + " "
    sentence += random.choice(nouns)

    # Determine whether to include a prepositional phrase
    if random.choice([True, False]):
        sentence += " " + random.choice(prepositions) + " "
        sentence += random.choice(articles) + " "
        sentence += random.choice(nouns)

    # Determine whether to include a conjunction and a second independent clause
    if random.choice([True, False]):
        sentence += " " + random.choice(conjunctions) + " "
        sentence += random.choice(articles) + " "
        sentence += random.choice(nouns) + " "
        sentence += random.choice(verbs)

    sentence += "."
    return sentence

def main():
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    articles = getWords("articles.txt")
    prepositions = getWords("prepositions.txt")
    adjectives = getWords("adjectives.txt")
    conjunctions = getWords("conjunctions.txt")

    print("Generated Sentence:", generate_sentence(nouns, verbs, articles, prepositions, adjectives, conjunctions))

if __name__ == "__main__":
    main()
