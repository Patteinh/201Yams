# 201Yams 🎲

Welcome to **201yams**.

This project involves developing a software to calculate the probability of obtaining a specific combination in a Yams (Yahtzee) game.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** Via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 201yams

## Project Overview 🔎

The goal of 201yams is to create a program that calculates the chances of achieving certain combinations in a Yams game. The combinations include pairs, three-of-a-kind, four-of-a-kind, full house, straight, and yahtzee.

### Key Features

- **Combination Calculation:** Compute the probability for various dice combinations.
- **Command-Line Interface:** Provide a user-friendly command-line interface for input and results.

### Usage

```
∼> ./201yams -h
USAGE
./201yams d1 d2 d3 d4 d5 c
DESCRIPTION
d1 value of the first die (0 if not thrown)
d2 value of the second die (0 if not thrown)
d3 value of the third die (0 if not thrown)
d4 value of the fourth die (0 if not thrown)
d5 value of the fifth die (0 if not thrown)
c expected combination

∼> ./201yams 0 0 0 0 0 yams_4
Chances to get a 4 yams: 0.01%

∼> ./201yams 1 2 3 4 5 four_4
Chances to get a 4 four-of-a-kind: 1.62%

∼> ./201yams 2 2 5 4 6 straight_6
Chances to get a 6 straight: 16.67%

∼> ./201yams 0 0 0 0 0 full_2_3
Chances to get a 2 full of 3: 0.13%

∼> ./201yams 2 3 2 3 2 full_2_3
Chances to get a 2 full of 3: 100.00%
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `/201yams d1 d2 d3 d4 d5 c`.
4. For detailed guidelines, refer to `201yams.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
