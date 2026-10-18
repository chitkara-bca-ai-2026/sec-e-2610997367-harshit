sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for character in sentence:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        spaces += 1
    else:
        special += 1

letters = vowels + consonants

if letters > 0:
    percentage = vowels / letters * 100
else:
    percentage = 0

print("\n" + "=" * 45)
print("          DOCUMENT ANALYSIS REPORT")
print("=" * 45)
print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")
print("Words:               ", words)
print("Vowels:              ", vowels)
print("Consonants:          ", consonants)
print("Digits:              ", digits)
print("Spaces:              ", spaces)
print("Special characters:  ", special)

print("\n--- Summary ---")
print("Total letters:", letters)
print(f"Vowel percentage: {percentage:.1f}%")

print("\n" + "=" * 45)
print("Analysis Complete!")
print("=" * 45)


