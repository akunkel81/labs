def zipmap(key_list: list, value_list: list, override=False):
    if len(key_list) > len(value_list):
        value_list.extend([None] * (len(key_list) - len(value_list)))
    elif len(value_list) > len(key_list):
        value_list = value_list[:len(key_list)]

    zipped = zip(key_list, value_list)

    if override:
        result = {k: v for k, v in zipped}  # Later values override earlier ones
    else:
        result = {}
        for k, v in zipped:
            if k in result:
                return {}  # Duplicate key found, return an empty dictionary
            result[k] = v

    return result

# Examples
print(zipmap(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6]))
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))
print(zipmap([1, 3, 5, 7], [2, 4, 6]))
