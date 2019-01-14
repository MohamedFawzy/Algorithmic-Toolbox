# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    answer = 0
    for i, next in enumerate(text, start=1):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                answer = i
                break
            top = opening_brackets_stack.pop()
            match = are_matching(top.char, next)
            if match == False:
                answer = i
                break

    return answer, opening_brackets_stack


def main():
    text = input()
    answer, opening_brackets_stack = find_mismatch(text)
    # Printing answer, write your code here
    if answer != 0:
        print(answer)
    elif len(opening_brackets_stack):
        top = opening_brackets_stack.pop()
        print(top.position)
    else:
        print("Success")


if __name__ == "__main__":
    main()
