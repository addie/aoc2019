# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's
# protected by a password. The Elves had written the password
# on a sticky note, but someone threw it out.
#
# However, they do remember a few key facts about the password:
#
# 1. It is a six-digit number.
# 2. The value is within the range given in your puzzle input.
# 3. Two adjacent digits are the same (like 22 in 122345).
# 4. Going from left to right, the digits never decrease;
#    they only ever increase or stay the same (like 111123 or 135679).
# 5. Other than the range rule, the following are true:
#
# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?
#
# Your puzzle input is 367479-893698.
#
# --- Part Two ---
# An Elf just remembered one more important detail:
# the two adjacent matching digits are not part of a larger group of matching digits.
#
# Given this additional criterion, but still ignoring the range rule, the following are now true:
#
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?
#
# Your puzzle input is still 367479-893698.

from typing import List, AnyStr, Tuple, Set


def valid(i):
    digits = []
    while i:
        digits.append(i % 10)
        i //= 10

    repeating = decreasing = False
    for n in range(len(digits) - 1, 0, -1):
        if digits[n] == digits[n - 1]:
            repeating = True
        if digits[n] > digits[n - 1]:
            decreasing = True

    return repeating and not decreasing


def part1(mn: int, mx: int) -> int:
    counter = 0
    nums = []
    for i in range(mn, mx):
        if valid(i):
            nums.append(i)
            counter += 1
    return counter


def valid_pairs(i):
    digits = []
    while i:
        digits.append(i % 10)
        i //= 10

    decreasing = False
    n = len(digits) - 1
    while n > 0:
        if digits[n] > digits[n - 1]:
            decreasing = True
        n -= 1

    if digits[0] == digits[1] and digits[0] != digits[2] or \
            digits[1] == digits[2] and digits[1] != digits[0] and digits[1] != digits[3] or \
            digits[2] == digits[3] and digits[2] != digits[1] and digits[2] != digits[4] or \
            digits[3] == digits[4] and digits[3] != digits[2] and digits[3] != digits[5] or \
            digits[4] == digits[5] and digits[4] != digits[3]:
        return not decreasing

    return False


def part2(mn: int, mx: int) -> int:
    counter = 0
    nums = []
    for i in range(mn, mx):
        if valid_pairs(i):
            nums.append(i)
            counter += 1
    return counter


if __name__ == '__main__':
    min_val = 367479
    max_val = 890000
    # print(part1(min_val, max_val))
    print(part2(min_val, max_val))
