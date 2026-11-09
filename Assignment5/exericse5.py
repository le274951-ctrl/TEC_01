def remove_odd_numbers(numbers):
    new_list = []

    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = remove_odd_numbers(numbers)

    print("Original list:", numbers)
    print("List without odd numbers:", result)


main()
