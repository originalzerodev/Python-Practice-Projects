import random,os,time
os.system('cls')
try:
    while True:
        task_num = input("How many task do u want to enter?: ")
        try:
            task_num = int(task_num)
            if task_num > 1:
                break
            else:
                print("The no. of task can't be less than 2")
        except ValueError:
            print("Invalid input by the User\nThe User must input an integer")
    task = []
    for i in range(task_num):
        t = input(f"Task ({i+1}): ")
        task.append(t)
    def get_task():
        return random.choice(task)
    print("THE FINAL RESULT WILL BE THE RESULT OF THE THIRD DRAW")
    draw_num = 0
    while draw_num != 3:
        time.sleep(5) 
        print(f"The random task ({draw_num + 1}): ", get_task())
        draw_num += 1
except KeyboardInterrupt:
    print("\nInterrupted by User")
