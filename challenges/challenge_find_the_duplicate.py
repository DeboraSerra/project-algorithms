def get_num_dict(nums):
    num_dict = {num: 0 for num in nums}
    for num in nums:
        num_dict[num] += 1
    return num_dict


def get_duplicate(num_dict):
    for num, qnt in num_dict.items():
        if isinstance(num, str):
            return False
        elif num < 0:
            return False
        elif qnt > 1:
            return num


def find_duplicate(nums):
    """Faça o código aqui."""
    if nums is None:
        return False
    num_dict = get_num_dict(nums)
    is_duplicate = get_duplicate(num_dict)
    if is_duplicate:
        return is_duplicate
    return False
