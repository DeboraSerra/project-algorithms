def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if len(word) == 0 or low_index < 0 or high_index < 0:
        return False
    elif low_index == high_index:
        return True
    elif high_index >= (len(word) // 2):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    elif word[low_index] == word[high_index]:
        return True
    else:
        return False
