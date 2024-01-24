def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books"
    is converted to "displayAllBooks" """
    title_case = sentence.title() # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '') # remove spaces
    # Lowercase first letter, join with rest of string
    # Slices don't produce index out of bounds errors.
    # So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def banner(text: str) -> str:
    """ Add a banner around the string and return new string """
    return f"{'*' * len(text)}\n{text}\n{'*' * len(text)}"


def main():
    sentence = input('Enter your sentence: ')
    output = banner(camelcase(sentence))
    print(output)


if __name__ == '__main__':
    main()