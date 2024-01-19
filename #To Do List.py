#To Do List
#Max Steffanus and Tommy Chen
#Intial
todo = []



def prompt():
    print("\nSelect an option \n1. Add Task To List \n2. View List \n3. Mark as Complete \n4. Remove Task \n5. Remove all Tasks \n6. Sort List Alphabetically \n7. Print the number of items on the list \n8. Exit Program\n")
    y = int(input("Option: "))
    if y == 1:
        todo.append(input("What do you want to add? "))
        prompt()
    elif y == 2:
        print(todo)
        prompt()
    elif y == 3:
        x = input("What did you complete? ")
        todo.remove(x)
        todo.append("X " + x)
        prompt()
    elif y == 4:
        todo.remove(input("What do you want to remove? "))
        prompt()
    elif y == 5:
        todo.clear()
        prompt()
    elif y == 6:
        todo.sort()
        prompt()
    elif y == 7:
        print(len(todo))
        prompt()
    else:
        quit()
        
prompt()