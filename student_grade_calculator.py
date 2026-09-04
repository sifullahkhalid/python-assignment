def calculator(student_name,subject_1,subject_2,subject_3):
        total_marks = int(subject_1+subject_2+subject_3)
        average = (total_marks/3)
        print(f"Sudent Name: {student_name}")
        print(f"Total Marks: {total_marks}")
        print(f"Average: {average:.2f}")
        if average >= 80 and average <=100: 
                print("Grade: A+")
        elif average >= 70 and average < 80:
                print("Grade: A")
        elif average >= 60 and average < 70:
                print("Grade: B")
        elif average >= 50 and average < 60:
                        print("Grade: C")
        elif average < 50 and average >-1:
            print("Grade: F")
        else:
            print("enter correct value")

       
student_name = str(input("Enter Student Name : "))
subject_1 = float(input("Enter 1st subject mark : "))
subject_2 = float(input("Enter 2nd subject mark : "))
subject_3  = float(input("Enter 3rd subject mark : "))


calculator(student_name,subject_1,subject_2,subject_3)
