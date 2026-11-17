def count_vowels_and_consonants(text: str) -> dict:
    counter = {
        'unli' : 0,
        'undosh' : 0
    }
    
    for i in text.lower():
        if i in "AEIOUaeiou":
            counter['unli'] += 1
        elif i.isalpha():
            counter['undosh'] += 1

    return counter


print(count_vowels_and_consonants("Salom Dunyo"))


