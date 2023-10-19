# for i in range(10):
#     print (f"{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}{0:<5d}")
#
#
# for i in range(10):
#     print ("{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}{:<5d}".format(0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
#
#
# for i in range(10):
#     print ('%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i' % (0,0,0,0,0,0,0,0,0,0))
#
#
# for i in range(10):
#     print("%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i%-5i" % (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
# for i in range(10):
#     print("%-5i%-5i" % (i*10 , i*20))
#


# cols = 10
# rows = 10
# arr = [[0]*cols]*rows

# for row in arr:
#     for idx in row:
#         print(idx, end=" ")
#
#     print()

# x = [[0] * 10 for i in range(11)]
#
# # print(x, end='/n')
# for row in arr:
#     for x in row:
#         print(x, end=" ")
#
#     print()
import random

#######################################################
EMPTY = ' '
PLAYER = '!'
WALL = '■'
DIRT = 'O'
##############################################Variables
ground = []
RST = "\u001b[0m"
COLORED_WALL = "\u001b[48;5;8m" + " " + RST
COLORED_GROUND = "\u001b[48;5;94m" + " " + RST
COLORED_SPACE = "\u001b[48;5;232m" + " " + RST
COLORED_COIN = "\u001b[38;5;3m" + "$" + RST
COLORED_PLAYER = "\u001b[48;5;232m" + "\u001b[38;5;33m" + "!" + RST
COLORED_BOMB = "\u001b[48;5;196m" + " " + RST
w = int(input("enter width :"))
h = int(input("enter height : "))


def randomblock():
    t = random.randint(0 , 100)
    if t>0 and t<=30 :
        return EMPTY
    elif t>30 and t<=80:
        return DIRT
    else :
        return WALL

def initGround():
    for i in range(h):
        temp = []
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                temp.append(WALL)
            else:
                temp.append(" ")
        ground.append(temp)


def initblocks():
    for i in range(h):
        for j in range (w):
            if ground[i][j] == EMPTY :
                ground[i][j] = randomblock()


initGround()
initblocks()
for i in range(h) :
    for j in range(w) :
        print(ground[i][j] , end=' ')

    print()