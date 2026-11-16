def word_frequency(text, word):
    words = text.split()
    frequencies = {}

    for item in words:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies.get(word, 0)


def main():
    text = input("Enter a piece of text: ")
    word = input("Enter the word to search for: ")

    frequency = word_frequency(text, word)

    print("The word", word, "appears", frequency, "times.")


main()