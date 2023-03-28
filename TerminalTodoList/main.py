import atexit

#Variables
alltodo = []
thingToAdd = ""
thingToRemove = 0
currentLoop = 0

#Open the file and load the contents into the list and close file once done
file = open('todos.txt', 'r')
for line in file:
    alltodo.append(line.rstrip('\n'))
file.close()

def check_command(whatToCheck):
    #Print the current todo's
    if(whatToCheck == "list"):
        if len(alltodo) == 0:
            print("Nothing on the todo list, try adding something!")

        global currentLoop

        for todo in alltodo:
            currentLoop += 1
            print(f"{currentLoop}. {todo}")
        
        currentLoop = 0

    #Add a todo
    elif(whatToCheck == "add"):
        thingToAdd = input('Enter todo to add... ').rstrip('\n')
        alltodo.append(thingToAdd)

    #Remove a todo
    elif(whatToCheck == "remove"):
        thingToRemove = input('Enter todo to remove: ')
        alltodo.remove(thingToRemove)

    #Quit program
    elif(whatToCheck == "quit"):
        quit()


def save():
    file = open('todos.txt', 'w')
    if alltodo:
        file.write("\n".join(alltodo))
    file.close()

atexit.register(save)

#Always ask the user for an Input then check what was sent
while True:
    command = input('Enter command: ')
    check_command(command)
