import random

articles = ['the', 'a', 'an']
nouns = ['boy', 'girl', 'dog', 'cat', 'ball']
verbs = ['kicked', 'played', 'took', 'threw', 'caught']
adjectives = ['red', 'blue', 'green', 'yellow', 'sore', 'happy', 'angry']
prepositions = ['at', 'in', 'on', 'over', 'under']
conjunctions = ['and', 'but', 'or']

def generate_sentence():
    sentence = []
    
    if random.choice([True, False]):
        sentence.append(random.choice(adjectives))
    
    sentence.append(random.choice(articles))
    sentence.append(random.choice(nouns))
    sentence.append(random.choice(verbs))
    sentence.append(random.choice(articles))
    sentence.append(random.choice(nouns))
    
    if random.choice([True, False]):
        sentence.append(random.choice(prepositions))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))
    
    if random.choice([True, False]):
        sentence.append(random.choice(conjunctions))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))
        sentence.append(random.choice(verbs))
        sentence.append(random.choice(articles))
        sentence.append(random.choice(nouns))
    
    return ' '.join(sentence) + '.'

if __name__ == "__main__":
    for _ in range(5):
        print(generate_sentence())
