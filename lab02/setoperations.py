def make_set(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

user_input = input("For function make_set, enter numbers separated by spaces: ")
user_list = user_input.split()
user_list = [int(x) for x in user_list]

unique_list = make_set(user_list)

print("Results of make_set function:", unique_list)

def is_set(data):
    if data is None:
        return False
    unique_elements = []
    for item in data:
        if item in unique_elements:
            return False
        unique_elements.append(item)
    return True

user_input_set = input("For function is_set, enter numbers separated by spaces: ")
user_list_set = user_input_set.split()
user_list_set = [int(x) for x in user_list_set]

unique_list_set = is_set(user_list_set)

print("Results for is_set function:", unique_list_set)

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    return make_set(setA + setB)

user_input1 = input("For the union function, enter the first set of numbers, separated by spaces: ")
user_input2 = input("For the union function, enter the second set of numbers, separated by spaces: ")

setA = [int(x) for x in user_input1.split()]
setB = [int(x) for x in user_input2.split()]

union_result = union(setA, setB)


print("The results of the union function:", union_result)

def intersection(setC, setD):
    if not is_set(setC) or not is_set(setD):
        return []
    result = []
    for item in setC:
        if item in setD and item not in result:
            result.append(item)
    return result

new_user_input1 = input("For the intersection function, enter the first set of numbers, separated by spaces: ")
new_user_input2 = input("For the intersection function, enter the second set of numbers, separated by spaces: ")

setC = [int(x) for x in new_user_input1.split()]
setD = [int(x) for x in new_user_input2.split()]

intersection_result = intersection(setC, setD)

print("The results of the intersection function:" , intersection_result)
