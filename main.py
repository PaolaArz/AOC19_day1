from functools import reduce
with open('input_file.txt') as my_file:
	my_input_list = my_file.read().splitlines()

def calculate_fuel(acc, mass):
	return acc + (int(int(mass)/3)-2)

total_fuel = reduce(calculate_fuel, my_input_list, 0)
print(total_fuel)