def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if len(word) == 0:
        return False
    low_index, high_index = 0, len(word) - 1
    is_palindrome = False
    while is_palindrome == False:
        if low_index == high_index:
            is_palindrome = True
        elif high_index >= (len(word) // 2):
            low_index, high_index = low_index + 1, high_index - 1
        elif word[low_index] == word[high_index]:
            is_palindrome = True
        else:
            return False
    return is_palindrome
    
