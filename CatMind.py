import graphics as g
import time

field_x = 10
field_y = 10
block_size = 25


def DrawBlock(window, point_x_1, point_y_1, point_x_2, point_y_2):
    block = g.Rectangle(g.Point(point_x_1, point_y_1), g.Point(point_x_2, point_y_2))
    block.draw(window)


def clear(window):
    for item in window.items[:]:
        item.undraw()


cats = 10
cat_code = []

win = g.GraphWin("aaa", field_x * block_size, field_y * block_size)

index_x = 0
index_y = 0
while index_x < field_x:
    while index_y < field_y:
        DrawBlock(win, index_x * block_size, index_y * block_size, (index_x + 1) * block_size,
                  (index_y + 1) * block_size)
        index_y += 1
    index_x += 1

win.getMouse()

print(cat_code)
