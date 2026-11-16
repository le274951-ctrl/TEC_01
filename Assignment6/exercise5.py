def remove_odd_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = remove_odd_numbers(numbers)

    print("Original list:", numbers)
    print("Cut-down list:", even_numbers)


main()