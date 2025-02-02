def count_chars(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spaces = 0
    vowel_count = 0
    consonant_count = 0
    other_chars = 0
    digit_sum = 0

    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digit_sum += int(char)
        else:
            other_chars += 1
    
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Spaces: {spaces}")
    print(f"Other Characters: {other_chars}")
    print(f"Sum of Digits: {digit_sum}")

input_string = input("Enter a string: ")
count_chars(input_string)
