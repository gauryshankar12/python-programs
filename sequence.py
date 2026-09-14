numbers = input("Enter numbers: ")

my_list = numbers.split(",")
my_tuple = tuple(my_list)

print("List:", my_list)
print("Tuple:", my_tuple)
print("Total elements:", len(my_list))
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Reverse:", my_list[::-1])