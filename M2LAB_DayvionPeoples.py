# Dayvion Peoples
# 1/22/2026
# M2LAB
# Menu-driven program that calls functions

# TODO: input validation so negatives and values +5 are not negative

def reading():
    print("Add 30 to read_time")

def coding():
    print("Add 45 to code_time")

def watch_video():
    print("Add 20 to video_time")

def study_other():
    print("Add 15 to other_time")

def main():
    print()
    
    
    # Create variables
    user_option = "1"
    read_time = 0
    code_time = 0
    video_time = 0
    other_time = 0
    
    while user_option != "5":
        print("Study Session Menu")
        print("1. Reading / Reviewing Notes")
        print("2. Coding Practice")
        print("3. Watching Lecture Videos")
        print("4. Other Study Activity")
        print("5. End Session")
    
        user_option = input("Select option by its number: ")
        
        
        if user_option == "1":
            reading()
        elif user_option == "2":
            coding()
        elif user_option == "3":
            watch_video()
        elif user_option == "4":
            study_other()
        
    print("Thank you for studying with us! Goodbye.")
    
    
# Call the main
if __name__ == "__main__":
    main()