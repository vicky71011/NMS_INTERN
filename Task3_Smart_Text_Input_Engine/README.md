# Smart Text Input Engine (CLI)

A Command Line Interface (CLI) based Natural Language Processing (NLP) project that performs:

- Spell Correction
- Grammar/Sentence Correction
- Next Word Prediction
- Dictionary Meaning & Synonyms
- Confidence Score Generation
- Unknown Word Handling
- Frequency-Based Word Ranking

---

# Features

## 1. Spell Correction

Detects misspelled words and automatically corrects them.

### Example

Input:

i m gong to schol

Output:

I am going to school

### Technologies Used

- TextBlob
- SpaCy

---

## 2. Sentence Correction

Corrects simple grammatical mistakes using:
- Subject-Verb Agreement
- Modal Verb Rules
- POS Tagging

### Example

Input:

he go to school

Output:

he goes to school

### Another Example

Input:

he might has cold

Output:

he might have cold

### Technologies Used

- SpaCy POS Tagging
- Rule-Based NLP

---

## 3. Next Word Prediction

Predicts the next probable words using a Trigram Language Model.

### Example

Input:

I am going to

Output:

be / to / get

### Technologies Used

- NLTK
- Brown Corpus
- Trigram Language Model
- Frequency-Based Ranking

---

## 4. Dictionary Support

Displays:
- Meaning
- Synonyms

### Example

Input:

school

Output:

Meaning: an educational institution
Synonyms: school, schooling, educate

### Technologies Used

- NLTK WordNet

---

## 5. Confidence Score

Each corrected word is assigned a confidence score.

### Example

school → 66%
going → 100%

---

## 6. Unknown Word Handling

Low-confidence or unrecognized words are safely identified.

### Example

Unknown / Low Confidence Words:
1 : coll

---

# Technologies Used

| Technology | Purpose |

| Python | Programming Language |
| NLTK | NLP corpus & tokenization |
| TextBlob | Spell correction |
| SpaCy | POS tagging & grammar analysis |
| WordNet | Dictionary meanings & synonyms |
| Collections.Counter | Frequency-based ranking |

---

# Project Structure

Smart_Text_Input_Engine/
│
├── src/
│   ├── main.py
│   ├── spell_corrector.py
│   ├── sentence_corrector.py
│   ├── next_word.py
│   ├── dictionary.py
│   └── set_up.py
│
├── requirements.txt
└── README.md

---

# Installation

## 1. Clone the Repository

git clone <repository-link>

---

## 2. Install Required Packages

pip install nltk textblob spacy

---

## 3. Download SpaCy Model

python -m spacy download en_core_web_sm

---

## 4. Download NLTK Datasets

Run:

python set_up.py

This downloads:
- punkt
- punkt_tab
- brown
- wordnet

---

# How It Works

## Spell Correction

Uses:

Word(word).spellcheck()

The system:
1. Compares the input word with known English words
2. Uses probability-based ranking
3. Selects the most likely correction

### Example

schol → school
goig → going

---

## Grammar Correction

Uses:
- SpaCy POS tagging
- Subject-verb agreement rules
- Modal verb correction

### Examples

he go → he goes
might has → might have

The system dynamically checks:
- pronouns
- proper nouns
- verbs
- modal auxiliaries

before applying corrections.

---

## Next Word Prediction

Uses a Trigram Language Model.

### Example Sentence

I am going to school

Generated trigrams:


(I, am, going)
(am, going, to)
(going, to, school)

Predictions are ranked using word frequency.

---

# Sample Output

SMART TEXT INPUT ENGINE

Enter the Sentence: i m gong to schol

Corrected Sentence: I am going to school

Confidence score of each word.!

i → 100.0%
am → 100.0%
going → 100.0%
to → 100.0%
school → 66.0%

Next Word Suggestions:

with (Frequency: 3)
, (Frequency: 3)
'' (Frequency: 3)
. (Frequency: 2)
and (Frequency: 1)

Enter a word from the sentence for meaning and synonyms:
school

Meaning:
an educational institution

Synonyms:
school, schooling, civilize, educate, shoal

---

# File Description

## main.py

Controls the complete execution flow:
- User input
- Sentence correction
- Confidence display
- Next word prediction
- Dictionary support

---

## spell_corrector.py

Handles:
- Spell correction
- Confidence scoring
- Unknown word detection
- Proper noun handling

---

## sentence_corrector.py

Handles:
- Grammar correction
- Subject-verb agreement
- Modal verb correction

---

## next_word.py

Implements:
- Trigram language model
- Frequency-based next word prediction

---

## dictionary.py

Provides:
- Meaning
- Synonyms

using WordNet.

---

## set_up.py

Downloads required NLTK datasets.

---

# Constraints Satisfied

| Requirement | Status |

| Spell Correction | ✅ |
| Dictionary Support | ✅ |
| Next Word Suggestion | ✅ |
| Sentence Correction | ✅ |
| Confidence Score | ✅ |
| Unknown Word Handling | ✅ |
| Frequency-Based Ranking | ✅ |
| NLP-based Implementation | ✅ |

---

# Future Improvements

Possible enhancements:
- Transformer-based grammar correction
- Deep learning next-word prediction
- Context-aware spell correction
- GUI/Web interface
- Speech-to-text integration
- Real-time typing suggestions

---

# Conclusion

The Smart Text Input Engine is a mini NLP project that combines:
- statistical language modeling
- rule-based grammar correction
- spell checking
- lexical databases

to create an intelligent text-processing CLI application.

The project demonstrates practical implementation of:
- NLP preprocessing
- POS tagging
- Trigram prediction
- Frequency-based ranking
- Probabilistic spell correction
- Grammar correction rules