#RANDOM TIMER
import time,random,os
os.system('cls')

def intro():
    print("THIS IS A RANDOM TIMER")
    print("ENTER THE MIN. AND MAX. TIME AND THE PROGRAM WILL DECIDE THE TIME")
    print("THE TIME IS IN MINUTES")

def min_max():
    min_time = int(input("Minimum time: "))
    max_time = int(input("Maximum time: "))
    chosen_time = random.randint(min_time,max_time)
    print(f"The time for the task is {chosen_time} {'minutes' if chosen_time != 1 else 'minute'}")
    return chosen_time


def countdown(time_limit):
    
    for minutes in range(time_limit,0,-1): 
        for seconds in range(59,-1,-1):
            print(f"              {minutes-1:02d} {'minutes' if minutes-1 != 1 else 'minute'} {seconds:02d} {'seconds' if seconds != 1 else 'second'} remaining  ", end="\r")
            time.sleep(1)

def ending():
    print("\n")
    print("Take a Damn Break!\n"*5)

intro()
try:
    chosen_time = min_max() # use this if think u gonna need chosen_time later if not use countdown(min_max()).
    # this make the min_max() called and chosen_time make reusable at the same time
    countdown(chosen_time) # countdown(min_max()) #this make it use only here
    ending()
except KeyboardInterrupt:
    print("\nInterrupted by user\nExited")
