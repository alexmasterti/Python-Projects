def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0

    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

def mode(numbers):
    if not numbers:
        return 0

    # Count occurrences of each number
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Find the mode(s)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    # If all numbers appear only once, there is no mode
    if len(modes) == len(numbers):
        return None

    return modes

def main():
    # Test the statistical functions with a given list
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List:", test_list)
    print("Mean:", mean(test_list))
    print("Median:", median(test_list))
    print("Mode:", mode(test_list))

if __name__ == "__main__":
    main()
