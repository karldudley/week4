# USE TKINTER FOR GUI!!!!!
# useful for capstone 2 & 3
# read file
tasks_read = open('data.txt', 'r')


data = tasks_read.readlines()

for pos, line in enumerate(data, 1):
    split_data = line.split(", ")

    output = f'——————————[{pos}]——————————\n'
    output += f'Assigned to: \t\t{split_data[0]}\n'
    output += f'Task: \t\t\t{split_data[1]}\n'
    output += f'Description: \t\t{split_data[2]}\n'
    output += f'Assigned Date: \t\t{split_data[3]}\n'
    output += f'Due Date: \t\t{split_data[4]}\n'
    output += f'Is Completed: \t\t{split_data[5]}\n'
    output += '\n'
    output += '———————————————————————————\n'

    print(output)

# fail safe so use can not break the system
while True:
    task_choice = int(input('Please select a task number: '))-1

    if task_choice < 0 or task_choice > len(data):
        print('You have selected an invalid option, try again.')
        continue

    edit_data = data[task_choice]
    break

while True:
    output = f'——————————[SELECT AN OPTION]——————————\n'
    output += '1 - Edit due date \n'
    output += '2 - Mark as completed \n'
    output += '——————————————————————————————————————\n'

    choice = int(input(output))

    if choice <= 0 or choice >= 3:
        print('You have selected an invalid option, try again.')
        continue

    if choice == 1:
        print("") # TODO - I need to do this thing for capstone 3
    elif choice == 2:
        split_data = edit_data.split(", ")
        split_data[-1] = 'Yes\n' # -1 because we want the end piece of data
        new_data = ", ".join(split_data)
        data[task_choice] = new_data

    tasks_write = open('data.txt', 'w')
    for line in data:
        tasks_write.write(line)

    break

tasks_write.close()
tasks_read.close()
print("You've finished the task!")
