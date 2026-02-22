import random

def run(iterations):
    success = 0

    for _ in range(iterations):
        birthdays = []

        for _ in range(23):
            birthdays.append(random.randint(1, 365))

        found = False
        for i in range(len(birthdays)):
            for j in range(i + 1, len(birthdays)):
                if birthdays[i] == birthdays[j]:
                    found = True
                    break
            if found:
                break

        if found:
            success += 1

    print("Birthday:", success / iterations)
