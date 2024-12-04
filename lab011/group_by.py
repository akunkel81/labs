def group_by(func, target_list: list):
    from itertools import groupby
    target_list_sorted = sorted(target_list, key=func)
    grouped = groupby(target_list_sorted, key=func)
    return {k: list(v) for k, v in grouped}

# Examples
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
