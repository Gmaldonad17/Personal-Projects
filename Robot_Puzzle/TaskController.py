import time
from Robot_Types import types

class TaskController():
    def __init__(self, robot = None):
        # initList Format: Discription, Estimated Time (ms), Leg Requirements, Dexterity Requirements, Complete Status
        self.List = [['doing the dishes'         , 1000, 0, 2, False],
                     ['doing the laundry'        , 3000, 0, 1, False],
                     ['taking out the recycling' , 4000, 1, 1, False],
                     ['making a sammich'         , 7000, 0, 1, False],
                     ['mowing the lawn'          ,20000, 2, 0, False],
                     ['raking the leaves'        ,18000, 2, 2, False],
                     ['giving the dog a bath'    ,14500, 0, 2, False],
                     ['baking some cookies'      , 8000, 0, 2, False],
                     ['washing the car'          ,20000, 1, 0, False]]
        self.robot = robot
        self.totalTime = 0
        self.complete = False

    def checkCondition(self):
        complete = True
        for i in self.List:
            if i[4] == False:
                complete = False
        if complete == False:
            return False
        if complete == True:
            return True

    def printList(self):
        for i in range(len(self.List)):
            if i == 0:
                print("_" * (37) + "  " + "_" * (45))
            if i >= 0 and i < 6:
                print("| " + self.List[i][0] + (26 - len(self.List[i][0])) * " " + "| " + str(self.List[i][4]) + " " * (6 - len(str(self.List[i][4]))) + "| "
                      " | "+ str(i+1) + " " + types[i][0] + (14 - len(types[i][0])) * " " + "| " + "Speed: " + str(types[i][1]) + (2 - len(str(types[i][1]))) * " " + "| " + "Dexterity: " + str(types[i][2]) + " |")
            if i == 6:
                print("| " + self.List[i][0] + (26 - len(self.List[i][0])) * " " + "| " + str(self.List[i][4]) + " " * (
                            6 - len(str(self.List[i][4]))) + "|" + "  " + "-" * 45)
            if i > 6 and i <= len(self.List) - 1:
                print("| " + self.List[i][0] + (26 - len(self.List[i][0])) * " " + "| " + str(self.List[i][4]) + " " * (6 - len(str(self.List[i][4]))) + "|")
            if i == len(self.List) - 1:
                print("-" * (37))
        print("")

    def reqCheck(self, array):
        if self.robot.type[1] >= array[2] and self.robot.type[2] >= array[3]:
            return True
        else:
            return False

    def completeTask(self):
        i = 0
        robotUsed = False
        for task in self.List:
            taskTime = task[1]
            taskComp = task[4]

            if taskComp == False and self.robot.task > 0:
                if self.reqCheck(task) == True:
                    robotUsed = True
                    divider = (self.robot.type[1] * task[2]/2 + self.robot.type[2] * task[3]/2)
                    t = float('{0:.3g}'.format(task[1]/(divider*1000)))
                    print("Robot " + self.robot.name + " is " + task[0])
                    print("Estimated time: " + str(t * 1000) + "ms")

                    time.sleep(t/2)
                    print("Task Complete!\n")

                    self.totalTime += t
                    self.robot.task -= 1
                    self.List[i][4] = True
            i += 1
        if robotUsed != True:
            print("No task could be found for Robot " + self.robot.name + "\n")

        print("Total Time: " + str(self.totalTime) + " seconds")
        self.complete = self.checkCondition()

    def setRobot(self, robot):
        self.robot = robot