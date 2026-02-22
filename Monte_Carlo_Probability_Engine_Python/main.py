import monty_hall
import birthday_paradox
import law_of_large_numbers

def main():
    iterations = 100000
    print("Monte Carlo Probability Engine in Python\n")
    monty_hall.run(iterations)
    birthday_paradox.run(iterations)
    law_of_large_numbers.run()

if __name__ == "__main__":
    main()
