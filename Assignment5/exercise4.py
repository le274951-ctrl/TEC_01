def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def main():
    numbers = [10, 20, 30, 40, 50]

    result = calculate_sum(numbers)

    print("The sum is:", result)


main()