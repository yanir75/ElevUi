import time
import tkinter
from tkinter import *
from win32api import GetSystemMetrics


class ElevatorUi:
    def __init__(self, floors, elev, width=GetSystemMetrics(0), height=GetSystemMetrics(1)):
        self.floorsNum = floors
        self.elevNum = elev
        self.root = Tk()
        self.width = width
        self.height = height
        self.root.attributes('-fullscreen', True)
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack(fill=tkinter.BOTH, expand=True)
        self.countingPep = 0
        self.countingInElev = 0
        self.countingFinishedCalls = 0
        self.waitingPeople = self.canvas.create_text(((self.width / self.elevNum * (0 + 1)) - 20 - 200 / self.elevNum),
                                                     self.height / self.floorsNum * (self.floorsNum - 1),
                                                     text=f'Waiting people for the elevator:{self.countingPep}',
                                                     anchor='w',
                                                     fill='red')
        self.inElev = self.canvas.create_text(((self.width / self.elevNum * (0 + 1)) - 20 - 200 / self.elevNum),
                                              self.height / self.floorsNum * (self.floorsNum - 1),
                                              text=f'People in the {self.countingInElev}', anchor='w',
                                              fill='blue')
        self.finishedCall = self.canvas.create_text(((self.width / self.elevNum * (0 + 1)) - 20 - 200 / self.elevNum),
                                                    self.height / self.floorsNum * (self.floorsNum - 1),
                                                    text=f'Finished calls:{self.countingFinishedCalls}', anchor='w',
                                                    fill='green')
        self.draw_floors()
        self.rectText = []
        self.rectList = self.draw_elev()
        self.peopleList = []
        self.canvas.tag_raise(self.waitingPeople)
        self.canvas.tag_raise(self.inElev)
        self.canvas.tag_raise(self.finishedCall)

    def move_elev(self, elev, floors, speed=1):
        self.canvas.move(self.rectList[elev], 0, -self.height / self.floorsNum * floors * speed)
        self.canvas.move(self.rectText[elev], 0, -self.height / self.floorsNum * floors * speed)
        self.update_drawing()

    def move_people_up(self, pep, where_to):
        self.canvas.move(pep, 0, -self.height / self.floorsNum * where_to)
        self.update_drawing()

    def move_people_up1(self, pep, where_to):
        self.canvas.move(self.peopleList[pep], 0, -self.height / self.floorsNum * where_to)
        self.update_drawing()

    def draw_floors(self):
        for i in range(self.floorsNum):
            self.canvas.create_line(0, self.height / self.floorsNum * i, self.width - 100 / self.elevNum,
                                    self.height / self.floorsNum * i,
                                    fill="red")
        self.update_drawing()
        return self.height / self.floorsNum

    def draw_elev(self):
        rect_list = []
        for i in range(self.elevNum):
            self.rectText.append(
                self.canvas.create_text(((self.width / self.elevNum * (i + 1)) - 20 - 200 / self.elevNum),
                                        self.height / self.floorsNum * (self.floorsNum - 1), text=f'{i}', anchor='w',
                                        fill='white'))
            rect_list.append(
                self.canvas.create_rectangle(self.width / self.elevNum * i, self.height,
                                             (self.width / self.elevNum * (i + 1)) - 20 - 200 / self.elevNum,
                                             self.height / self.floorsNum * (self.floorsNum - 1),
                                             fill='grey'))
        self.move_to_the_middle()
        self.update_drawing()
        return rect_list

    def draw(self):
        self.root.mainloop()

    def update_drawing(self):
        self.root.update()

    def move_to_the_middle(self):
        for i in self.rectText:
            self.canvas.move(i, -self.width / self.elevNum / 2, self.height / self.floorsNum / 2)
            self.canvas.tag_raise(i)
        self.canvas.move(self.waitingPeople, 0, (-self.height / self.floorsNum * (self.floorsNum - 1)) + 10)
        self.canvas.move(self.waitingPeople, -self.width / self.elevNum / 1.5, 0)
        self.canvas.move(self.inElev, 0, (-self.height / self.floorsNum * (self.floorsNum - 1)) + 25)
        self.canvas.move(self.inElev, -self.width / self.elevNum / 1.5, 0)
        self.canvas.move(self.finishedCall, 0, (-self.height / self.floorsNum * (self.floorsNum - 1)) + 40)
        self.canvas.move(self.finishedCall, -self.width / self.elevNum / 1.5, 0)
        self.update_drawing()

    def move_from_1_to_10(self, event):
        # if event.char == "x":
        for i in range(9):
            self.move_elev(0, 1)
            self.root.update()
            time.sleep(1)

    def create_people(self, floor_num=0):
        pep = self.canvas.create_oval(self.width - 25, self.height - 25, self.width - 35, self.height - 35,
                                      fill='red')
        self.peopleList.append(pep)
        self.move_people_up(pep, floor_num)
        self.countingPep += 1
        self.canvas.itemconfig(self.waitingPeople, text=f'Waiting people for the elevator:{self.countingPep}')

        self.update_drawing()
        return pep

    def move_people_to_elev(self, elev, people):
        pep = self.peopleList[people]
        self.canvas.move(pep, -self.width / self.elevNum * (self.elevNum - elev - 1), 0)
        self.update_drawing()

    def number_of_floors(self, min1_floor, max1_floor):
        count = 0
        for i in range(min1_floor, max1_floor + 1):
            self.canvas.create_text(self.width - 20, self.height - 20 - self.height / self.floorsNum * count,
                                    text=f'{i}', anchor='w')
            count += 1
        self.update_drawing()

    def entered_the_elev(self, num):
        self.canvas.itemconfig(self.peopleList[num], fill='blue')
        self.countingInElev += 1
        self.countingPep+=-1
        self.canvas.itemconfig(self.waitingPeople, text=f'Waiting people for the elevator:{self.countingPep}')
        self.update_drawing()
        self.canvas.itemconfig(self.inElev, text=f'People in the elevator:{self.countingInElev}')
        self.update_drawing()

    def exited_the_elev(self, num):
        self.canvas.itemconfig(self.peopleList[num], fill='white')
        self.countingInElev += -1
        self.canvas.itemconfig(self.inElev, text=f'People in the elevator:{self.countingInElev}')
        self.countingFinishedCalls += 1
        self.canvas.itemconfig(self.finishedCall, text=f'Finished calls:{self.countingFinishedCalls}')
        self.update_drawing()
