def letter_analysis(sentence):
    letter_counting = []

    for char in word:
        if 'a' <= char <= 'z':
            letter_counting[char] =letter_counting(char, 0) + 1

    sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

    for letter, count in sorted_letters[:6]:
        print(f"{letter}: {count} times")


message = "Hello , how are you? Hope you're doing well!"

frequency_analysis(message)
