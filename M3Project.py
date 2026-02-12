# Dayvion Peoples
# 2/10/2026
# M3 Project
# Use list to calculate tuition based on classes taken


# Create the three lists needed for the program
stu_names=["Zakari Watson","Jerome Williams","Dominique Ross","Diana Shepard","Yoko Mayo","Rashad Ahmed","Susan Jones"]

courses=["MAT 035 (Concepts of Algebra)","CTI 115 (Computer System Foundations)","BAS 120 Intro to Analytics","CSC 121 Python Programming"]

tuition=[460,520.98,500,783.88]

######### User-Defined Functions start here #######
def course_display():
    print()
    print("Course Name" + "\t\t\t\t" + "Tuition")
    print("-*" * 20)
    # Loop through the courses and tuition lists
    # at the same time using the index
    for i in range(0,4):
        print(f"{courses[i]:<40} \t ${tuition[i]}")
    
def display_menu():
    print("-" * 10 , "MENU" , "-" * 10)
    print("1) Calculate Tuition for ALL students")
    print("2) Calculate Tuition for Specific students")
    print("3) Exit")
    print()

def all_students():
    '''
    Loop through all_students
    Ask about student in each class
    User inputs y if the student is in the class
    '''
    
    total_tuition = []
    
    
    for student in stu_names:
        semester_cost = 0
        # Create empty list to hold classes student is taking
        registered_classes = []
        for course in courses:
            print(f"Is {student} taking {course}?")
            taking_course = input("Enter 'y' or 'n': ")
            if taking_course == "y":
                # Get the index of the course
                course_index = courses.index(course)
                # Get the value of the item at same index
                # But from the tuition list
                course_tuition = tuition[course_index]
                # Add the course_tuition to the tuition variable
                semester_cost += course_tuition
        #Before we switch to a new student, add tuition to new list
        total_tuition.append(semester_cost)
        
        
    # Display all students and their corresponding total_tuition
    print(f"{'Student Name':^30} Tuition")
    print("-" * 40)
    for i in range(0, len(stu_names)):
        print(f"{stu_names[i]:<30} ${total_tuition[i]}")
        
        
def selected_student():
    '''
    Allow user to choose one student
    Calculate tuition for that chosen student
    '''
    # Loop through all students
    # Include a reference value for each student
    print()
    for i in range(0, len(stu_names)):
        print(f"{i + 1}) {stu_names[i]}")
    print()
    
    # Get user input - they choose a student by the number
    chosen_student = int(input("Select a student: "))
    
    print()
    # Tell the user who they chose
    print(f"You selected: {stu_names[chosen_student - 1]}")
    
    student_name = stu_names[chosen_student - 1]
    
    # Determine which courses chosen_student is taking
    semester_cost = 0
    classes_taking_indexes = []
    for course in courses:
            print(f"Is {student_name} taking {course}?")
            taking_course = input("Enter 'y' or 'n': ")
            if taking_course == "y":
                # Get the index of the current course
                course_index = courses.index(course)
                # Add course_index to a list
                classes_taking_indexes.append(course_index)
                # Get the item at the matching index from tuitionlist 
                tuition_cost = tuition[course_index]
                # Increment semester_cost by tuition_cost
                semester_cost += tuition_cost
    # Loop to display only the classes the student is taking
    print()
    print()
    for each in classes_taking_indexes:
        # For each index int the list, print the corresponding
        # item from courses and from tuititon
        print(f"{courses[each]}   ${tuition[each]}")
    # Display total cost for all courses taken
    print("-" * 40)
    print(f"Total Cost   ${semester_cost}")

######### User-Defined Functions start here #######

def main():
    # Call the course_display() function
    course_display()
    
    display_menu()
    
    # Create a variable to get into the loop once
    user_choice = 10
    
    while user_choice != 3:
        print()
        user_choice = int(input("Choose your option: "))
    
        if user_choice == 1:
            all_students()
        if user_choice == 2:
            selected_student()
        while user_choice not in [1,2,3]:
            print ("You entered an invalid option")
            user_choice = int(input("Enter a valid option:"))
            
# Call the main
if __name__ == "__main__":
    main()