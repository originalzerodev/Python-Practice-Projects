#RANDOM TASK PICKER
import random,os,time
os.system('cls')
try:
    task_num = int(input("How many task do u want to enter?: "))
    task = []
    for i in range(task_num):
        time.sleep(1)
        t = input(f"Task ({i+1}): ")
        task.append(t)
    while True:
        def third_random_task():
            Third_task = [random.choice(task) for _ in range(3)]
            return Third_task[2]
        time.sleep(1)
        print("The Third random task is ", third_random_task())
        time.sleep(1)
        another = input("Do u want another draw?(Y/N): ").strip().lower()
        if another == "n":
            time.sleep(1)
            print("EXITING.......")
            time.sleep(1)
            break
        elif another == "y":
            time.sleep(1)
            print("Re-Drawing.......")
            time.sleep(1)
            continue
        else:
            time.sleep(1)
            print("User Input Not Valid!!")
            time.sleep(1)
            print("EXITING..............")
            time.sleep(1)
            break
except KeyboardInterrupt:
    time.sleep(1)
    print("\nInterrupted by the User!")
    time.sleep(1)
    print("EXITING................")
