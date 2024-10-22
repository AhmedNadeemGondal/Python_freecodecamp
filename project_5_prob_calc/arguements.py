# create a dictionary with three key-value pairs where the keys are "a", "b", and "c",
# and the corresponding values are 3, 2, and 1 respectively
my_dict = {"a": 3, "b": 2, "c": 1}

# create a new list using a list comprehension that repeats each key a number of times
# equal to the corresponding value in the dictionary
my_list = []
for key, value in my_dict.items():  # iterate over each key-value pair in the dictionary using the items() method
    for i in range(value):  # repeat the key a number of times equal to the corresponding value
        my_list.append(key)  # add the key to the new list

# print the new list
print(my_list)
