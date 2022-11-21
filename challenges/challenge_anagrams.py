def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_word, second_word = first_string.lower(), second_string.lower()
    list_word_one = [letter for letter in first_word]
    list_word_two = [letter for letter in second_word]
    sort_word(list_word_one, 0, len(list_word_one) - 1)
    sort_word(list_word_two, 0, len(list_word_two)- 1)
    is_anagram = list_word_one == list_word_two
    if first_string == "" or second_string == "":
        is_anagram = False
    return ("".join(list_word_one), "".join(list_word_two), is_anagram)


def sort_word(list_word, start, end):
    if start < end:
        p = get_pivot(list_word, start, end)
        sort_word(list_word, start, p - 1)
        sort_word(list_word, p + 1, end)


def get_pivot(list, start, end):
    pivot = list[end]
    delimiter = start - 1

    for index in range(start, end):
        if list[index] <= pivot:
            delimiter += 1
            list[index], list[delimiter] = list[delimiter], list[index]
    list[delimiter + 1], list[end] = list[end], list[delimiter + 1]
    return delimiter + 1
