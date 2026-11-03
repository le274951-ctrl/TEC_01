def sum_numbers(paragraph):
    total = 0

    for word in paragraph.split():
        word = word.strip(".,!?")
        if word.isdigit():
            total += int(word)

    return total


paragraph = input("Enter paragraph: ")
print(sum_numbers(paragraph))