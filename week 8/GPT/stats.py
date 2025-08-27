def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2 
    if n % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]


def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_frequency]
    if len(modes) == len(numbers):
        return 0
    return modes[0]


def main():
    test_list = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
    print(mean(test_list)) 
    print(median(test_list))
    print(mode(test_list))


if __name__ == "__main__":
    main()
