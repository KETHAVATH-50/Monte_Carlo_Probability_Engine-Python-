import random

def run(iterations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(iterations):
        car = random.randint(0, 2)
        player_choice = random.randint(0, 2)

        possible = []
        for door in range(3):
            if door != player_choice and door != car:
                possible.append(door)

        opened = random.choice(possible)

        if player_choice == car:
            stay_wins += 1

        for door in range(3):
            if door != player_choice and door != opened:
                new_choice = door

        if new_choice == car:
            switch_wins += 1

    print("Stay:", stay_wins / iterations)
    print("Switch:", switch_wins / iterations)
