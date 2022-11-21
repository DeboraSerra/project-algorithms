def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    times = 0
    if target_time is None:
        return None
    for enter, leave in permanence_period:
        if (enter is None or leave is None) or (
            not isinstance(enter, int) or not isinstance(leave, int)
        ):
            return None
        list = [index for index in range(enter, leave + 1)]
        if target_time in list:
            times += 1
    return times
