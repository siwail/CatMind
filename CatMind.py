
import time, random


import graphics as g

field_x = 50
field_y = 50
block_size = 10

cats = 0

cat_code = []
cat_x = []
cat_y = []
cat_size = []
cat_vision_radius = []
cat = []
win = g.GraphWin("Обучение котов", field_x * block_size, field_y * block_size)


def DrawBlock(point_x_1, point_y_1, point_x_2, point_y_2):
    block = g.Rectangle(g.Point(point_x_1, point_y_1), g.Point(point_x_2, point_y_2))
    block.draw(win)


def AddCat(x, y, size, radius):
    global cats
    cat_x.append(x)
    cat_y.append(y)
    cat_size.append(size)
    cat_vision_radius.append(radius)
    cat.append(CreateCat(x, y, size, radius))
    cats += 1
    return cats


def MoveCat(x, y, index):

    cat_x[index] += x
    cat_y[index] += y

    if cat_x[index] < 0:
        cat_x[index] = 0
    if cat_x[index] + cat_size[index] > field_x:
        cat_x[index] = field_x - cat_size[index]
    if cat_y[index] < 0:
        cat_y[index] = 0
    if cat_y[index] + cat_size[index] > field_y:
        cat_y[index] = field_y - cat_size[index]

    cat[index] = TransformCat(cat[index], cat_x[index], cat_y[index], cat_size[index])


def CreateCat(x, y, size, radius):
    '''vision = g.Rectangle(g.Point(x * block_size, y * block_size),
                        g.Point(x * block_size + size * block_size, y * block_size + size * block_size))
    vision.setFill('yellow')
    vision.draw(win)'''

    block = g.Rectangle(g.Point(x * block_size, y * block_size),
                        g.Point(x * block_size + size * block_size, y * block_size + size * block_size))
    block.setFill('green')
    block.draw(win)
    return block


def TransformCat(block, x, y, size):
    block.undraw()
    block = g.Rectangle(g.Point(x * block_size, y * block_size),
                        g.Point(x * block_size + size * block_size, y * block_size + size * block_size))
    block.setFill('green')
    block.draw(win)
    return block


def clear():
    for item in win.items[:]:
        item.undraw()


index_x = 0
while index_x < field_x:
    index_y = 0
    while index_y < field_y:
        DrawBlock(index_x * block_size, index_y * block_size, (index_x + 1) * block_size,
                  (index_y + 1) * block_size)
        index_y += 1
    index_x += 1
    index_y = 0

AddCat(1, 1, 2, 5)
AddCat(2, 2, 2, 5)
AddCat(3, 3, 2, 5)
print(cats)

while True:
    time.sleep(0.01)
    MoveCat(random.randint(-1, 1), random.randint(-1, 1), 0)
    MoveCat(random.randint(-1, 1), random.randint(-1, 1), 1)
    MoveCat(random.randint(-1, 1), random.randint(-1, 1), 2)

win.getMouse()

print(cat_code)

