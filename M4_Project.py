# Dayvion Peoples
# 2/17/2026
# M4 Project
# Use nested dictionaries

# Define the dictionaries  needed

# In courses, the keys are course names and the values are dictionaries
courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 508},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}

# In students, keys are names and the values are lists
students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}

def menu():
    print("-----------MENU------------")
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses and Tuition for Specific Student")
    print("4) Display Tuition for All Students")
    print("5) Display # of Students and Tuition for All Courses")
    print("6) Exit")
    print("-----------------------------")
    
    
def display_courses():
    
    print(f"{'Code':<15}{'Description':<30}{'Tuition'}")
    print("-" *  40)
    for key in courses.keys():
        print(f"{key:<15}{courses[key]["desc"]:<30}{courses[key]["tuition"]}")
    print("-" *  40)
    
def course_search():
    print()
    # Get a course from the  user
    course_entered = input("Enter a course code: ")
    while course_entered not in courses.keys():
        
        print("Invalid Course Code")
        course_entered = input("Enter a course code: ")
    # At this point, the input should be valid
    print(f"You chose the course: {course_entered}")
    # Display the course's desc and tuition
    print(f"Description for {course_entered}: \
        {courses[course_entered]["desc"]}")
    print()
    print(f"Tuition for {course_entered}: \
        {courses[course_entered]["tuition"]}")
    print()
    
def get_student_courses():
    # For loop to show all students and assign a number
    for index in range(1,len(students.keys())+1):
        print(f"{index}) {list(students.keys())[index-1]}")
        print()
    
    chosen_student = int(input("Enter a number to choose a student: "))
    chosen_student = list(students.keys())[chosen_student-1]
    print()
    print(f"You selected: {chosen_student}")
    print()
    
    # Grab the chosen student's classes  (list) and assign a variable
    chosen_student_courses = students[chosen_student]
    
    print(f"{chosen_student}'s Courses and Tuition: ")
    
    # Create a increment variable to hold tuition for all courses
    total_tuition = 0
    for course in chosen_student_courses:
        print(f"{course:<15}{courses[course]["desc"]:<30}$ {courses[course]["tuition"]}")
        print()
        total_tuition += courses[course]["tuition"]
    # Loop breaks here
    print(f"Overall Total:              ${total_tuition:,.2f}")
    
def all_student_info():
    # For loop to loop through all students
    print("Name              # courses             Tuition")
    print("--------------------------------------------------")
    grand_total = 0
    for name, course_list in students.items():
        student_tuition = 0
        for c in course_list:
            student_tuition += courses[c]["tuition"]
        print(f"{name:<25}{len(students[name]):<8}${student_tuition:,.2f}")
        grand_total += student_tuition
    print(f"Grand Total                      ${grand_total:,.2f}")

def main():
    print("Welcome to Course Registration")
    
    # variable to make the loop run first time
    user_choice = 0

    # Make a loop that runs until user enters 6
    while user_choice != 6:
        menu()
        user_choice = int(input("Choose an option by its number: "))
        
        # Attempt to use a switch-case
        match user_choice:
            case 1:
                display_courses()
            case 2:
                course_search()
            case 3:
                get_student_courses()
            case 4:
                all_student_info()
            case 5:
                pass
            case 6:
                break
            case _:
                print("Invalid Option chosen")
    # Loop breaks here
    print("Thanks for registering, goodbye!")
        

    
# Call the main
if __name__ == "__main__":
    main()