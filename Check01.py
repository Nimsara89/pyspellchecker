from spellchecker import SpellChecker
spell = SpellChecker()
paragraph = input("Please enter a paragraph: ")

# Tokenize the paragraph into words
words = paragraph.split()

# Find misspelled words
misspelled = spell.unknown(words)

# Correcting
corrected_paragraph = []
for word in words:
    if word in misspelled:
        # Get the most likely correction
        corrected_word = spell.correction(word)
        corrected_paragraph.append(corrected_word)
    else:
        corrected_paragraph.append(word)
corrected_text = ' '.join(corrected_paragraph)

# Output the original and corrected paragraphs
print("\nOriginal Paragraph:\n", paragraph)
print("\nCorrected Paragraph:\n", corrected_text)
