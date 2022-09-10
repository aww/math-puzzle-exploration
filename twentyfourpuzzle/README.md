# The 24 Puzzle

The [24 puzzle](https://en.wikipedia.org/wiki/24_(puzzle)) involves drawing a collection of four numbers with replacement.
Typically this might be from integers 1-9, 1-10, or 1-13, corresponding to single digits, non-face cards (using ace as 1),
or all cards in a poker deck.

You then must reduce all the numbers using the operations +, -, *, and / in any grouping you like such that the result is 24.

## Popular puzzles

Warm up: 3, 1, 5, 1

Harder: 6, 5, 4, 1

Harder still: 5, 5, 5, 1


## Terminology

A __puzzle__ is a collection of four numbers.

To __acheive__ a number is to find a sequence of operations starting from a puzzle that reduces to the number.

## Questions

### Why 24?

* Is there something special about 24?
* It obviously has a unusual number of divisors for its size, does this make it easier to achieve?
* Is it always possible to acheive?


### What puzzles are the most flexible?

* What puzzles can acheive the largest number of values?


## Running the code

The code of twentyfour.py runs in about 15 seconds on my MacBook Pro.
By default the code looks at the 1-9 case and below I will describe those results.
This range is trivial to change in the code, but changing the size of the collection of numbers is not.
The possible operator groupings are enumerated explicitly (there are only five).

I'm sure there is a slicker and/or more efficient way to enumerate all the possible combinations of operations.
It certainly doesn't prune redundencies in the permutations of values and communativity of the operations.

## Results

1. There are 495 possible puzzles
1. The value 24 is only achievable in 404 of the puzzles.
1. The most achievable number is 2 which is possible from 492 puzzles.
1. The puzzle with the most number of achievable positive integers is (6, 7, 8, 9) from which you can achieve 127 possible positive integers.
   This is largest possible collection of unique values. Is the fact that 127=2^7-1 of any significance?
1. The number 24 is the most achievable number greater than 18.
1. The most achievable positive numbers for their size are 2, 3, 6, 7, 8, 9, 10, 12, 16, 18, 24, 36.
1. Interestingly, if you are playing the game by drawing cards your chances of getting an achievable puzzle is likely higher than 404/495=81.6%
   because drawing from a 52 card deck without face cards yields duplicated digits with lower probability.
   In general duplicated digits lead to fewer achievable values and are likely underrepresented amongst the puzzles achieving 24.
   We could verify this with some modifications to the code.




