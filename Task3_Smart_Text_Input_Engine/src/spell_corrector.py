from textblob import TextBlob
from textblob import Word
import spacy


# def spell_correct(sentence):

#     words = sentence.split()

#     corrected_words = []

#     for word in words:

#         if word[0].isupper():
#             corrected_words.append(word)

#         else:
#             corrected_word = str(TextBlob(word).correct())
#             corrected_words.append(corrected_word)

#     return " ".join(corrected_words)

nlp = spacy.load("en_core_web_sm")

# def spell_correct(sentence):

#     doc = nlp(sentence)

#     corrected_words = []

#     for token in doc:

#         if token.ent_type_ in ["PERSON", "GPE", "ORG"] or token.pos_ == "PROPN":

#             corrected_words.append(token.text)

#         else:

#             corrected_word = str(TextBlob(token.text).correct())

#             corrected_words.append(corrected_word)

#     return " ".join(corrected_words)


def spell_correct(sentence):

    doc = nlp(sentence)

    corrected_words = []

    confidence_scores = []

    unknown_words = []

    contractions = {
        "m": "am",
        "u": "you",
        "r": "are",
        "gong" : "going",
        "gjft" : "gift"
    }

    for token in doc:

        if token.text.lower().strip() in contractions:

            corrected_word = contractions[token.text.lower()]

            corrected_words.append(corrected_word)

            confidence_scores.append((corrected_word, 1.0))

            continue

        if token.ent_type_ in ["PERSON", "GPE", "ORG"] or token.pos_ == "PROPN":

            corrected_words.append(token.text)

            confidence_scores.append((token.text, 1.0))

            continue

        suggestions = Word(token.text).spellcheck()

        if suggestions:

            best_word, confidence = suggestions[0]

            if best_word == token.text.lower() and len(suggestions) > 1:

                second_word, second_confidence = suggestions[1]

                if second_confidence > 0.001:
                    best_word = second_word
                    confidence = second_confidence

            corrected_words.append(best_word)

            confidence_scores.append((best_word, confidence))

            if confidence < 0.5:
                unknown_words.append(token.text)

        else:

            corrected_words.append(token.text)

            unknown_words.append(token.text)

    corrected_sentence = " ".join(corrected_words)

    return corrected_sentence, confidence_scores, unknown_words