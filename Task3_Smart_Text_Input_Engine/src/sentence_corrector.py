from spell_corrector import spell_correct
import spacy

nlp = spacy.load("en_core_web_sm")

# def sentence_correction(sentence):

#     corrected = spell_correct(sentence)

#     tokens = corrected.split()

#     pronouns = ['he', 'she', 'it']

#     for i in range(len(tokens) - 1):

#         if tokens[i].lower() in pronouns:

#             verb = tokens[i + 1]

#             if verb == "go":
#                 tokens[i + 1] = "goes"

#             elif verb == "do":
#                 tokens[i + 1] = "does"

#             elif not verb.endswith('s'):
#                 tokens[i + 1] = verb + 's'

#     return " ".join(tokens)


def sentence_correction(sentence):

    corrected, confidence_scores, unknown_words = spell_correct(sentence)

    # tokens = corrected.split()

    doc = nlp(corrected)
    tokens = [token.text for token in doc]

    pronouns = ['he', 'she', 'it']
    modals = [
        "might", "may", "can", "could",
        "will", "would", "shall",
        "should", "must"
    ]

    # for i in range(len(tokens) - 1):

    #     if tokens[i].lower() in modals:

    #         next_word = tokens[i + 1].lower()

    #         if next_word == "has":
    #             tokens[i + 1] = "have"

    #         elif next_word == "goes":
    #             tokens[i + 1] = "go"

    #         elif next_word == "does":
    #             tokens[i + 1] = "do"

    #         elif next_word.endswith("ies"):

    #             tokens[i + 1] = next_word[:-3] + "y"

    #         elif next_word.endswith("es"):

    #             tokens[i + 1] = next_word[:-2]

    #         elif next_word.endswith("s"):

    #             tokens[i + 1] = next_word[:-1]

    for i in range(len(tokens) - 1):

        if tokens[i].lower() in modals:

            next_word = tokens[i + 1].lower()

            if next_word == "has":

                old_word = tokens[i + 1]

                tokens[i + 1] = "have"

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    "have"
                )

            elif next_word == "goes":

                old_word = tokens[i + 1]

                tokens[i + 1] = "go"

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    "go"
                )

            elif next_word == "does":

                old_word = tokens[i + 1]

                tokens[i + 1] = "do"

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    "do"
                )

            elif next_word.endswith("ies"):

                old_word = tokens[i + 1]

                corrected_word = next_word[:-3] + "y"

                tokens[i + 1] = corrected_word

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    corrected_word
                )

            elif next_word.endswith("es"):

                old_word = tokens[i + 1]

                corrected_word = next_word[:-2]

                tokens[i + 1] = corrected_word

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    corrected_word
                )

            elif next_word.endswith("s"):

                old_word = tokens[i + 1]

                corrected_word = next_word[:-1]

                tokens[i + 1] = corrected_word

                confidence_scores = update_confidence(
                    confidence_scores,
                    old_word,
                    corrected_word
                )

    doc = nlp(" ".join(tokens))

    tokens = [token.text for token in doc]

    for i in range(len(doc) - 1):

        current_word = doc[i]
        next_word = doc[i + 1]

        if current_word.text.lower() in pronouns or current_word.pos_ == "PROPN":

            if i > 0 and doc[i - 1].text.lower() in modals:
                continue

            if next_word.pos_ == "VERB":

                verb = next_word.text

                if verb in ["is", "was", "has", "does", "goes"]:
                        continue
                    
                if verb == 'go':
                    verb = 'goes'
                
                elif verb == 'do':
                    verb ='does'

                elif verb.endswith(('o', 'ch', 'sh', 'x', 's', 'z')):
                    verb += 'es'

                elif verb.endswith('y') and len(verb) > 1 and verb[-2] not in "aeiou":
                    verb = verb[:-1] + 'ies'

                elif not verb.endswith('s'):
                    verb += 's'

                tokens[i + 1] = verb

    final_sentence = " ".join(tokens)
    
    return final_sentence, confidence_scores, unknown_words

def update_confidence(confidence_score, old, new):

    updated_scores = []

    for word, score in confidence_score:

        if word == old:
            updated_scores.append((new, 1.0))

        else:
            updated_scores.append((word, score))

    return updated_scores