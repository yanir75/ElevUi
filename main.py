import random
import time
from ElevatorUi import ElevatorUi


def main(min1, max1, elev):
    ui = ElevatorUi(max1 - min1 + 1, elev)
    ui.number_of_floors(min1, max1)
    curpos1 = 0
    curpos2 = 0
    pep = 0
    pep1 = 1
    for i in range(100):
        if i % 10 == 0:
            x = random.randint(0, max1 - min1)
            ui.create_people(x)
            ui.move_people_to_elev(0, pep)
            x1 = random.randint(0, max1 - min1)
            ui.create_people(x1)
            ui.move_people_to_elev(1, pep1)
            while curpos1 > x and curpos2 > x1:
                ui.move_elev(0, -1)
                curpos1 += -1
                ui.move_elev(1, -1)
                curpos2 += -1
                time.sleep(1)
            while curpos1 < x and curpos2 < x1:
                ui.move_elev(0, 1)
                curpos1 += 1
                ui.move_elev(1, 1)
                curpos2 += 1
                time.sleep(1)
            while curpos1 > x and curpos2 < x1:
                ui.move_elev(0, -1)
                curpos1 += -1
                ui.move_elev(1, 1)
                curpos2 += 1
                time.sleep(1)
            while curpos1 < x and curpos2 > x1:
                ui.move_elev(0, 1)
                curpos1 += 1
                ui.move_elev(1, -1)
                curpos2 += -1
                time.sleep(1)
            while curpos1 > x:
                ui.move_elev(0, -1)
                curpos1 += -1
                time.sleep(1)
            while curpos1 < x:
                ui.move_elev(0, 1)
                curpos1 += 1
                time.sleep(1)
            while curpos2 > x1:
                ui.move_elev(1, -1)
                curpos2 += -1
                time.sleep(1)
            while curpos2 < x1:
                ui.move_elev(1, 1)
                curpos2 += 1
                time.sleep(1)
            ui.entered_the_elev(pep)
            ui.entered_the_elev(pep1)
            y = random.randint(0, max1 - min1)
            y1 = random.randint(0, max1 - min1)
            while x == y or y1 == x1:
                y = random.randint(0, max1 - min1)
                y1 = random.randint(0, max1 - min1)
            while curpos1 > y and curpos2 > y1:
                ui.move_elev(0, -1)
                curpos1 += -1
                ui.move_elev(1, -1)
                curpos2 += -1
                ui.move_people_up1(pep, -1)
                ui.move_people_up1(pep1, -1)
                time.sleep(1)
            while curpos1 < y and curpos2 < y1:
                ui.move_elev(0, 1)
                curpos1 += 1
                ui.move_elev(1, 1)
                curpos1 += 1
                ui.move_people_up1(pep, 1)
                ui.move_people_up1(pep1, 1)
                time.sleep(1)
            while curpos1 > y and curpos2 < y1:
                ui.move_elev(0, -1)
                curpos1 += -1
                ui.move_elev(1, 1)
                curpos1 += 1
                ui.move_people_up1(pep, -1)
                ui.move_people_up1(pep1, 1)
                time.sleep(1)
            while curpos1 < y and curpos2 > y1:
                ui.move_elev(0, 1)
                curpos1 += 1
                ui.move_elev(1, -1)
                curpos2 += -1
                ui.move_people_up1(pep, 1)
                ui.move_people_up1(pep1, -1)
                time.sleep(1)
            while curpos1 > y:
                ui.move_elev(0, -1)
                curpos1 += -1
                ui.move_people_up1(pep, -1)
                time.sleep(1)
            while curpos1 < y:
                ui.move_elev(0, 1)
                curpos1 += 1
                ui.move_people_up1(pep, 1)
                time.sleep(1)
            while curpos2 > y1:
                ui.move_elev(1, -1)
                curpos2 += -1
                ui.move_people_up1(pep1, -1)
                time.sleep(1)
            while curpos2 < y1:
                ui.move_elev(1, 1)
                curpos2 += 1
                ui.move_people_up1(pep1, 1)
                time.sleep(1)
            ui.exited_the_elev(pep)
            ui.exited_the_elev(pep1)
            pep += 2
            pep1 += 2
    ui.draw()


def func2(x, ui, pep1, curpos2, max1, min1, curpos):
    while curpos[curpos2] > x:
        ui.move_elev(1, -1)
        curpos[curpos2] += -1
        time.sleep(1)
    while curpos[curpos2] < x:
        ui.move_elev(1, 1)
        curpos[curpos2] += 1
        time.sleep(1)
    ui.entered_the_elev(pep1)
    y = random.randint(0, max1 - min1)
    while x == y:
        y = random.randint(0, max1 - min1)
    while curpos[curpos2] > y:
        ui.move_elev(1, -1)
        curpos[curpos2] += -1
        ui.move_people_up1(pep1, -1)
        time.sleep(1)
    while curpos[curpos2] < y:
        ui.move_elev(1, 1)
        curpos[curpos2] += 1
        ui.move_people_up1(pep1, 1)
        time.sleep(1)
    ui.exited_the_elev(pep1)


if __name__ == '__main__':
    main(-5, 10, 2)
