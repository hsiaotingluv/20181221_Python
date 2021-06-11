from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    pt1 = Point(250, 250)
    pt2 = Point(250, 350)

    #pt.setOutline(color_rgb(255, 255, 255))
    #pt.draw(win)

    ln = Line(pt1, pt2)
    ln.setOutline(color_rgb(0, 255, 255))
    ln.setWidth(5)
    ln.draw(win)

    rect = Rectangle(Point(150, 150), Point(250, 250))
    rect.setOutline(color_rgb(255, 255, 255))
    rect.setFill(color_rgb(255, 100, 0))
    rect.draw(win)

    cir = Circle(Point(250, 250), 50)
    cir.setOutline(color_rgb(255, 255, 255))
    cir.setFill(color_rgb(100, 255, 50))
    cir.setWidth(5)
    cir.draw(win)

    poly = Polygon(Point(40, 40), 
                    Point(100, 100), 
                    Point(40, 100), 
                    Point(0, 60),
                    Point(450, 450))
    poly.setFill(color_rgb(255, 0, 255))
    poly.setOutline(color_rgb(0, 255, 0))
    poly.setWidth(2)
    poly.draw(win)

    txt = Text(Point(150, 450), "What's up?")
    txt.setTextColor(color_rgb(255, 255, 255))
    txt.setSize(30)
    txt.setFace('courier')
    txt.draw(win)

    #img = Image(Point(250, 250), "apple.gif")
    #img.draw(win)

    input_box = Entry(Point(250, 250), 10)
    input_box.draw(win)
    txt1 = Text(Point(250, 300), "")
    txt1.draw(win)

    while True:
        txt1.setText(input_box.getText())
        break

    win.getMouse()
    win.close()

main()

