def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    times = 0
    if target_time is None or isinstance(target_time, tuple):
        return None
    for enter, leave in permanence_period:
        if (enter is None or leave is None) or (
            not isinstance(enter, int) or not isinstance(leave, int)
        ):
            return None
        if enter <= target_time and target_time <= leave:
            times += 1
    return times
