from collections import Counter

def frequency_checker():
    word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
    freqeuncy = Counter(word_list)
    for word, count in freqeuncy.items():
        print (f"{word} {count}")


    unique_word_li = {}
    for word in word_list:
        if word in unique_word_li:
            unique_word_li[word] += 1
        else:
            unique_word_li[word] = 1

    unique_words = list(unique_word_li.keys())
    print(f"Here is the unique word's list {unique_words}")


frequency_checker()
def pass_strength(password):
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_digit and has_letter and len(password)>=8:
        print("strong")
    else:
        print("weak")

password = input("Please enter the password: ")
#pass_strength(password)