import random

def run():
    print("\nIterations    Mean")
    for n in [10, 100, 1000, 10000, 100000]:
        total = 0
        for _ in range(n):
            total += random.randint(0, 1)
        mean = total / n
        print(n, "        ", round(mean, 2))
