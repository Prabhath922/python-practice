# Data Structures with to-do list manager

def to_do_Manager():
    tasks=[]

    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice=input("please enter your choice no")

        if(choice=='1'):
            task =input("please enter the task:")
            tasks.append(task)
            print("task added")
        elif choice=="2":
            print("/nyour tasks")
            for i ,tasks in enumerate(tasks,1):
                print(f" these are the following tasks: {i}, {tasks}")
        elif choice=="3":
            if not tasks:
                print("no tasks to remove")
            else :
                print("/n your tasks:")
                for i ,tasks in enumerate(tasks,1):
                    print("f {i},{taks}")
                    remove= int(input("please enter the task no to remove"))
                    if 1<= remove<=tasks.len():
                        tasks.pop(remove-1)
                    else :
                        print("invalid task no")
        elif choice=="4":
             print("/n exiting applicaiton")
             break
        else:
            print("invalid choice")

to_do_Manager()

