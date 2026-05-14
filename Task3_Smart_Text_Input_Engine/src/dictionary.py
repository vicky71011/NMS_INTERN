from nltk.corpus import wordnet


def get_meaning_synonyms(word):

    synsets = wordnet.synsets(word)

    if not synsets:
        return "Meaning not found", []

    meaning = synsets[0].definition()

    synonyms = set()

    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())

    return meaning, list(synonyms)[:5]