#Chapter 7 case study
'''
from turtle import Turtle, tracer, update

def cCurve(t, x1, y1, x2, y2, level):

    def drawLine(t, x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    if level == 0:
        drawLine(t, x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

def main():
    level = int(input("Enter level (0 or greater): "))
    t = Turtle()
    if level > 8:
        tracer(False)
    t.hideturtle()
    t.pencolor("blue")
    t.speed(10)
    cCurve(t, 50, -50, 50, 50, level)
    if level > 8:
        update()

main()
'''

#convert image to black and white
from PIL import Image, ImageDraw
img = Image.open("test1.bmp")

'''
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = img.getpixel((x, y))
        average = (r + g + b) // 3
        if average < 128:
            img.putpixel((x, y), (0, 0, 0))
        else:
            img.putpixel((x, y), (255, 255, 255))
			
img.show()
'''

#convert image to grayscale
'''
def grayscale(img):
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = img.getpixel((x, y))
            tgt = int(r * 0.299) + int(g * 0.587) + int(b * 0.114)
            img.putpixel((x, y), (tgt, tgt, tgt))
            
    img.show()
'''

#copy image
'''  
draw = ImageDraw.Draw(img)
newImg = img.copy()
grayscale(newImg)
newImg.save('/Users/hsiaotingluv/Desktop/python/test1.bmp')
'''

#blurring image
#examines neighbors above, below, left, right 
'''
from functools import reduce

def blur(img):

    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    new = img.copy()
    for y in range(1, img.height - 1):
        for x in range(1, img.width - 1):
            centre = img.getpixel((x, y))
            top = img.getpixel((x, y - 1))
            bottom = img.getpixel((x, y + 1))
            left = img.getpixel((x - 1, y))
            right = img.getpixel((x + 1, y))
            sums = reduce(tripleSum, [centre, top, bottom, left, right])
            
            averages = tuple(map(lambda x: x // 5, sums))

            new.putpixel((x, y), averages)
            
    return new

def main():
    new = blur(img)
    new.show()

main()
'''

#edge detection
#examines neighbors below and left
'''
def detectEdges(img, value):

    def average(triple):
        r, g, b = triple
        return (r + g + b) // 3

    new = img.copy()
    
    for y in range(img.height - 1):
        for x in range(1, img.width):
            centre = img.getpixel((x, y))
            bottom = img.getpixel((x, y + 1))
            left = img.getpixel((x - 1, y))
            centreAve = average(centre)
            bottomAve = average(bottom)
            leftAve = average(left)

            if abs(centreAve - bottomAve) > value or \
               abs(centreAve - leftAve) > value:
                new.putpixel((x, y), (0, 0, 0))
            else:
                new.putpixel((x, y), (255, 255, 255))
                
    return new

def main():
    value = int(input("Enter the value for edge detection: "))
    new = detectEdges(img, value)
    new.show()

main()
'''
