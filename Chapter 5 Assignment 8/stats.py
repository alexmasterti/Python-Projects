def median(numbers):
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    if not numbers:
        return 0
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode[0] if len(mode) == 1 else 0

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Median:", median(test_list))
    print("Mode:", mode(test_list))
    print("Mean:", mean(test_list))

if __name__ == "__main__":
    main()
