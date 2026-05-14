from sentence_corrector import *
from next_word import *
from dictionary import *


def main():
    print("SMART TEXT INPUT ENGINE")

    while True:

        sentence = str(input("Enter the Sentence: "))

        if sentence.lower() == "exit":
            print("\nI hope I corrected ur sentence.")
            return
        
        corrected_sentence, confidence_scores, unknown_words = sentence_correction(sentence)

        print()

        print(f"Corrected Sentence: {corrected_sentence[0].upper() + corrected_sentence[1:]}")

        print()

        print("Confidence score of each word.!")

        for word, score in confidence_scores:
            print(f"{word} → {round(score * 100, 2)}%")

        print()

        if unknown_words:
            print("Unknown / Low Confidence Words:")

            for id, word in enumerate(unknown_words, 1):
                print(f"{id} : {word}")

        print()

        suggestions = next_word_suggestions(corrected_sentence)

        print("Next Word Suggestions:")

        if suggestions:
            for word, freq in suggestions:
                print(f"{word} (Frequency: {freq})")
        
        else:
            print("No suggestions found")

        print()

        word = input("Enter a word from the sentence for meaning and synonyms, if not enter \"no\": ")
        
        if word.strip() == "no":
            print()
            continue

        meaning, synonyms = get_meaning_synonyms(word)

        print(f"Meaning: {meaning}")
        print(f"Synonyms: {','.join(synonyms)}")

        print()



if __name__ == "__main__":
    main()