#Chapter 7
#Reduce image size

from PIL import Image, ImageDraw

'''
def shrink(img, factor):
    width = img.width
    height = img.height
    newWidth = width // factor
    newHeight = height // factor
    new = Image.new('RGB', (newWidth, newHeight))
    oldY = 0
    newY = 0
    while oldY <= height - factor:
        oldX = 0
        newX = 0
        while oldX <= width - factor:
            oldP = img.getpixel((oldX, oldY))
            new.putpixel((newX, newY), oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    return new

def main():
    factor = int(input("Enter a shrink factor: "))
    img = Image.open("test1.bmp")
    new = shrink(img, factor)
    new.show()

main()
'''

#Enlarge image size
#dont know how to code algorithm

'''
def enlarge(img, factor):
    width = img.width
    height = img.height
    newWidth = width * factor
    newHeight = height * factor
    return img.resize((newWidth, newHeight))

def main():
    factor = int(input("Enter enlarge factor: "))
    img = Image.open("test1.bmp")
    new = enlarge(img, factor)
    new.show()

main()
'''

#Exercies
#2 
'''Each pixel typically consists of 8 bits (1 byte) for B&W image
or 24 bits (3 bytes) for a RGB image'''
