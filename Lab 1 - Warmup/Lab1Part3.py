"""
Part 3: camelCase

Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their
initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and
ParsER", your program will output "fontProcessorAndParser".

Optional extra question: print a warning message if the input will not produce a valid variable name. You don't need to
be exhaustive in checking, but test for a few common issues, such as starting with a number, or containing invalid
characters such as # or + or ".  Or, would it be easier to check that the name only contains valid characters?

Test your program with different example inputs, and comment your code.
"""

sentance = input("Enter a sentence: ")

wordliststart = sentance.split(' ')

result = ''

for word in wordliststart:
    if word == wordliststart[0]:
        word = word.lower()
    else:
        word = word.title()
    result += word

print(result)