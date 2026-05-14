import nltk
from nltk.corpus import brown
from collections import defaultdict, Counter


# words = brown.words()

# bigrams = list(nltk.bigrams(words))

# bigram_model = defaultdict(Counter)

# for w1, w2 in bigrams:
#     bigram_model[w1.lower()][w2.lower()] += 1


# def next_word_suggestions(sentence, top_n=5):

#     tokens = nltk.word_tokenize(sentence.lower())

#     if not tokens:
#         return []

#     last_word = tokens[-1]

#     suggestions = bigram_model[last_word]

#     if not suggestions:
#         return []

#     return [word for word, freq in suggestions.most_common(top_n)]

words = brown.words()

trigrams = list(nltk.trigrams(words))

trigram_model = defaultdict(Counter)

for w1, w2, w3 in trigrams:
    trigram_model[(w1.lower(), w2.lower())][w3.lower()] += 1


def next_word_suggestions(sentence, top_n=5):

    tokens = nltk.word_tokenize(sentence.lower())

    if len(tokens) < 2:
        return []

    last_two_words = (tokens[-2], tokens[-1])

    suggestions = trigram_model[last_two_words]

    if not suggestions:
        return []

    return suggestions.most_common(top_n)