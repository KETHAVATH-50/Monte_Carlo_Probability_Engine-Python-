# Monte Carlo Probability Engine in Python

## Overview
This project is a Python program developed to better understand probability concepts through simulation instead of only studying formulas. It uses Monte Carlo methods to repeatedly run classical probability problems and compare experimental results with their theoretical values. Observing convergence in practice helped build intuition about why probability laws work.

---

## Problems Simulated

### 1. Monty Hall Problem
The Monty Hall problem involves three doors:
- One door has a prize
- Two doors do not

After the player chooses a door, the host opens one losing door.  
The simulation compares two strategies:
- Staying with the original choice
- Switching to the remaining door

**Results:**
- Staying wins about **1/3** of the time
- Switching wins about **2/3** of the time

These results match the theoretical conditional probability.

---

### 2. Birthday Paradox
The Birthday Paradox asks whether at least two people in a group share the same birthday.

The simulation runs experiments with 23 people and shows that the probability of a shared birthday is slightly above **50%**, which agrees with the theoretical value of about 0.507.

This demonstrates how unintuitive combinatorics problems can be.

---

### 3. Law of Large Numbers
The Law of Large Numbers states that as the number of experiments increases, the average result approaches the expected value.

In this project:
- Random numbers between 0 and 1 are generated
- A running average is computed
- The average converges toward **0.5**, which is the expected value

This validates the convergence behaviour of random variables.

---

## How It Works
- Each experiment runs for **100,000+ iterations**
- Results are averaged over all runs
- Experimental values are compared with known theoretical values
- Python built-in `random` number generator is used

---

## Technologies Used
- Python 3
- Standard Python libraries
- `random` module

---

## Building and Running
Make sure Python 3 is installed, then run:

```bash
python main.py
```

---

## Sample Output
```
Stay: 0.33
Switch: 0.66
Birthday: 0.50

Iterations    Mean
10            0.53
100           0.46
1000          0.50
10000         0.49
100000        0.50
```

---

## What I Learned
- How Monte Carlo simulations work
- How empirical probability approaches theoretical probability
- Behaviour of the Law of Large Numbers
- Structuring a small Python project with multiple files

---

## Possible Improvements
- Add more probability puzzles
- Measure runtime and performance
- Output results to files for plotting
- Improve code structure further

---

## Final Note
This project was built mainly as a learning exercise to understand probability through simulation rather than only theory.
