# Dayvion Peoples
# 2/10/2026
# M3 Project
# Use list to calculate tutition based on classes taken


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
    for student in stu_names:
        # Create empty list to hold classes student is taking
        registered_classes = []
        for course in courses:
            print(f"Is {student} taking {course}?")
            taking_course = input("Enter 'y' or 'n': ")
            if taking_course == "y":
                registered_classes.append(course)
        # For each studemt, display name and list of classes taken
        print(f"{student} \t\t {registered_classes}")
        

######### User-Defined Functions start here #######

def main():
    # Call the course_display() function
    course_display()
    
    display_menu()
    
    # Create a variable to get into the loop once
    user_choice = 10
    
    while user_choice != 3:
        print("While loop is looping!")
        user_choice = int(input("Choose your option: "))
    
        if user_choice == 1:
            all_students()
        if user_choice == 2:
            print("You chose option 2")
        while user_choice not in [1,2,3]:
            print ("You entered an invalid option")
            user_choice = int(input("Enter a valid option:"))
            
# Call the main
if __name__ == "__main__":
    main()