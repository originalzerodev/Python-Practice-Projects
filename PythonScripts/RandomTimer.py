#RANDOM TIMER
import time,random,os
os.system('cls')

print("THIS IS A RANDOM TIMER")
print("ENTER THE MIN. AND MAX. TIME AND THE PROGRAM WILL DECIDE THE TIME")
print("THE TIME IS IN MINUTES")

min_time = int(input("Minimum time: "))
max_time = int(input("Maximum time: "))

time_limit = random.randint(min_time,max_time) 
print(f"The time for the task is {time_limit} minutes")

try:
    for minutes in range(time_limit,0,-1):
        print(f"The remaining time is {minutes - 1} minutes     ") 
        for seconds in range(59,-1,-1):
            print(f"                      {seconds} seconds    ", end="\r")
            time.sleep(1)
except KeyboardInterrupt:
    print("\nTimer stopped early! You can take break or start a new task.")

print("\n")
print("Take a Damn Break!\n"*5)
