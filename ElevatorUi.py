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
        self.draw_floors()
        self.rectText = []
        self.rectList = self.draw_elev()
        self.peopleList = []

    def move_elev(self, elev, floors,speed=1):
        self.canvas.move(self.rectList[elev], 0, -self.height / self.floorsNum * floors*speed)
        self.canvas.move(self.rectText[elev], 0, -self.height / self.floorsNum * floors*speed)

    def move_people_up(self, pep, where_to):
        self.canvas.move(pep, 0, -self.height / self.floorsNum * where_to)

    def draw_floors(self):
        for i in range(self.floorsNum):
            self.canvas.create_line(0, self.height / self.floorsNum * i, self.width - 100 / self.elevNum,
                                    self.height / self.floorsNum * i,
                                    fill="red")
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
                                             fill='black'))
        self.move_to_the_middle()
        return rect_list

    def draw(self):
        self.root.mainloop()

    def update_drawing(self):
        self.root.update()

    def move_to_the_middle(self):
        for i in self.rectText:
            self.canvas.move(i, -self.width / self.elevNum / 2, self.height / self.floorsNum / 2)
            self.canvas.tag_raise(i)

    def move_from_1_to_10(self, event):
        if event.char == "x":
            for i in range(9):
                self.move_elev(0, 1)
                self.root.update()
                time.sleep(1)

    def create_people(self, floor_num=0):
        pep = self.canvas.create_oval(self.width - 25, self.height - 25, self.width - 35, self.height - 35,
                                      fill='red')
        self.peopleList.append(pep)
        self.move_people_up(pep, floor_num)

    def move_people_to_elev(self, elev):
        pep = self.peopleList[0]
        self.canvas.move(pep, -self.width / self.elevNum * elev, 0)

    def number_of_floors(self, min_floor, max_floor):
        count = 0
        for i in range(min_floor, max_floor + 1):
            self.canvas.create_text(self.width - 20, self.height - 10 - self.height / self.floorsNum * count,
                                    text=f'{i}', anchor='w')
            count += 1

    def entered_the_elev(self, num):
        self.canvas.itemconfig(self.peopleList[num], fill='white')

    def exited_the_elev(self, num):
        self.canvas.itemconfig(self.peopleList[num], fill='green')
