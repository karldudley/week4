# ask user for the number of students
num_students = int(input("How many students would you like to register?\t"))

# open file and write heading
exam_deets = open('reg_form.txt', 'w')
exam_deets.write("Name\t\tID\t\tPlease Sign Below\n")

# loop for number of students, each time get student name, id and write to file
for i in range(num_students):
    print(f"Student {i+1}")
    stud_name = input("Name:\t")
    stud_id = input("ID:\t")
    exam_deets.write(stud_name + "\t" + stud_id + "\t" + "............................" + "\n")

# close file
exam_deets.close()
