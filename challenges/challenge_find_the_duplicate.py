def find_duplicate(nums):
    """Faça o código aqui."""
    if nums is None or isinstance(nums, str):
        return False
    num_dict  = { num: 0 for num in nums}
    for num in nums:
        num_dict[num] += 1
    for num, qnt in num_dict.items():
        if isinstance(num, str):
            return False
        if num < 0:
            return False
        if qnt > 1:
            return num
    return False
