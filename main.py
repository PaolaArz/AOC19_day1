from functools import reduce
with open('input_file.txt') as my_file:
	my_input_list = my_file.read().splitlines()

def calculate_fuel(acc, mass):
	return acc + (int(int(mass)/3)-2)

total_fuel = reduce(calculate_fuel, my_input_list, 0)
#total_fuel = reduce(calculate_fuel, [100756], 0)
print(f'total fuel: {total_fuel}')

#part2

def module_fuel(mass):
	return int(int(mass)/3)-2

my_fuel_list = list(map(module_fuel, my_input_list))

def extra_fuel(acc, fuel):
	while True:
		fuel = int(fuel/3)-2
		if fuel > 0:
			acc += fuel
		else:
		 	break
	return acc

total_fuel_extra = reduce(extra_fuel, my_fuel_list, 0)
print(f'total fuel including fuel: {total_fuel + total_fuel_extra}')


