from TaskController import TaskController
from Robot_Types import Robot

def main():
    List = TaskController()
    print("Welcome to the Bot-O-Mat Puzzle! Different Robots are created here.")
    print("Each bot will preform the first available task and will self destruct after three task.\n")
    List.printList()
    print("This above is the list of task and types of robots.\nDifferent Robots will preform tasks different rates.\nTry to complete the List as fast as you can using different types.")
    while List.complete == False:
        name = input("Enter a name for your Robot: ")
        while True:
            try:
                type = int(input("Enter the number of the type of Robot: ")) - 1
                if type >= 0 and type < 6:
                    break
                else: print("Invalid Input.")
            except:
                print("Error: Numbers only allowed")
        print("")
        UserBot = Robot(name,type)
        List.setRobot(UserBot)
        List.completeTask()
        print("Robot " + UserBot.name + " has self-destructed!")
        List.printList()
    print("All task completed in: " + str(List.totalTime) + " seconds!")

main()
