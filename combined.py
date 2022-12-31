# open numbers files
numbers1 = open('numbers1.txt', 'r')
numbers2 = open('numbers2.txt', 'r')
all_numbers = open('all_numbers.txt', 'w')

# read files and add all numbers to a single string
all_nums = numbers1.read().strip() + "," + numbers2.read().strip()

# spit the string into a list of numbers, mapped as ints
all_nums_list = list(map(int, all_nums.split(",")))

# write to the file a joined list of the sorted ints
all_numbers.write(",".join(list(map(str, sorted(all_nums_list)))))

# close the files
numbers1.close()
numbers2.close()
all_numbers.close()
