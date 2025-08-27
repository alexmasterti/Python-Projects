def newGuessCalc(guess, number):
    return (guess + number / guess) / 2

def newton(number):
    guess = number / 2
    while True:
        new_guess = newGuessCalc(guess, number)
        if abs(new_guess - guess) < 0.0001:
            return new_guess
        guess = new_guess

def main():
    while True:
        user_input = input("Enter a number (type 'exit' to quit): ")
        if user_input == "exit":
            break
        number = float(user_input)
        sqrt_estimate = newton(number)
        print(f"Square root of {number} is approximately {sqrt_estimate}")

if __name__ == "__main__":
    main()
