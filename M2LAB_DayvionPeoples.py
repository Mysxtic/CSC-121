# Dayvion Peoples
# 1/22/2026
# M2LAB
# Menu-driven program that calls functions

# TODO: input validation so negatives and values +5 are not negative

def reading(time):
    time[0] += 30
    print("Add 30 to read_time")
    

def coding(time):
    time[1] += 45
    print("Add 45 to code_time")
    

def watch_video(time):
    time[2] += 20
    print("Add 20 to video_time")
    

def study_other(time):
    time[3] += 15
    print("Add 15 to other_time")
    

def main():
    print()
    
    
    # Create variables
    user_option = "1"
    
    read_time = 0
    code_time = 0
    video_time = 0
    other_time = 0
    
    # Create a list
    time = [read_time, code_time, video_time, other_time]


    while user_option != "5":
        print()
        print()
        print("Study Session Menu")
        print("1. Reading / Reviewing Notes")
        print("2. Coding Practice")
        print("3. Watching Lecture Videos")
        print("4. Other Study Activity")
        print("5. End Session")
    
        user_option = input("Select option by its number: ")
        
        
        if user_option == "1":
            reading(time)
        elif user_option == "2":
            coding(time)
        elif user_option == "3":
            watch_video(time)
        elif user_option == "4":
            study_other(time)
        
    print(time)
    
    print(f"Time spent reading: {time[0]}")
    print(f"Time spent coding: {time[1]}")
    print(f"Time spent watching videos: {time[2]}")
    print(f"Time spent otherwise: {time[3]}")
    print("--------------------------------------")
    print(f"Total Study Time: {sum(time)}")
    
    
    print("Thank you for studying with us! Goodbye.")
    
    
    
# Call the main
if __name__ == "__main__":
    main()