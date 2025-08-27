replacements = {
    "i": "you",
    "me": "you",
    "my": "your",
    "am": "are",
    "you": "I",
    "your": "my",
    "are": "am",
}

def reply(input_text):
    words = input_text.lower().split()
    for i, word in enumerate(words):
        if word in replacements:
            words[i] = replacements[word]
    return ' '.join(words)

def main():
    patient_input = "you are not a helpful therapist."
    therapist_reply = reply(patient_input)
    print("Patient:", patient_input)
    print("Therapist:", therapist_reply)

if __name__ == "__main__":
    main()
