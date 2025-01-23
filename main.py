def task():
    task = []
    task_input = int(input("How many task do you want to add ?"))
    for i in range(1,task_input+1):
        task_name = input(f"Task {i} = ")
        task.append(task_name)

    print(task)

    while True:
        operation = int(input("what do you want to do :\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n= "))
        if operation == 1:
            task_add = input("What do you want to add ?")
            task.append(task_add)
            print("done")

        elif operation == 2:
            update_what = input("what term do you want to update?")
            if update_what in task:
                update_to = input("what to update it to ?")
                ind = task.index(update_what)
                task[ind] = update_to
                print("done")

        elif operation == 3:
            del_which = input("which term you want to delete?")
            if del_which in task:
                ind = task.index(del_which)
                del task[ind]
                print("done")

        elif operation == 4:
            print(task)
            print("Done")

        elif operation == 5:
            print("you have come out of the loop")
            break

        else:
            print("invalid try again")
task()