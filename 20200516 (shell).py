Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ========
>>> img.height
1800
>>> img.width
2880
>>> img.size
(2880, 1800)
>>> img.mode
'RGBA'
>>> img.format
'PNG'
>>> img.info

>>> img.palette
>>> img.getcolors
<bound method Image.getcolors of <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2880x1800 at 0x1015C4FA0>>
>>> img.getdata
<bound method Image.getdata of <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2880x1800 at 0x1015C4FA0>>
>>> from images import Image
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    from images import Image
ModuleNotFoundError: No module named 'images'
>>> img.getpixel
<bound method Image.getpixel of <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=2880x1800 at 0x1015C4FA0>>
>>> img.getpixel(0,0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    img.getpixel(0,0)
TypeError: getpixel() takes 2 positional arguments but 3 were given
>>> img.getpixel(0, 0)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    img.getpixel(0, 0)
TypeError: getpixel() takes 2 positional arguments but 3 were given
>>> coordinate = x, y = 0, 0
>>> img.getpixel(coordinate)
(0, 0, 0, 255)
>>> img.draw()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    img.draw()
AttributeError: 'PngImageFile' object has no attribute 'draw'
>>> from PIL import ImageDraw
>>> draw = ImageDraw.Draw(img)
>>> draw.line((0, 0) + img.size, fill = 128)
>>> img.show()
>>> del draw
>>> img.show()
>>> del draw
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    del draw
NameError: name 'draw' is not defined
>>> from PIL import ImageDraw
>>> draw = ImageDraw.Draw(img)
>>> img = Image(150, 150)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    img = Image(150, 150)
TypeError: 'module' object is not callable
>>> y = image.height() // 2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    y = image.height() // 2
NameError: name 'image' is not defined
>>> y = img.height() // 2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    y = img.height() // 2
TypeError: 'int' object is not callable
>>> img.height()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    img.height()
TypeError: 'int' object is not callable
>>> img.height()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    img.height()
TypeError: 'int' object is not callable
>>> y = img.height // 2
>>> y
900
>>> import Image
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    import Image
ModuleNotFoundError: No module named 'Image'
>>> from PIL import Image, ImageDraw
>>> im = Image.new('RGB', (100, 100), (255, 255, 255))
>>> im.getpixel((10,10))
(255, 255, 255)
>>> im.getpixel(10,10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    im.getpixel(10,10)
TypeError: getpixel() takes 2 positional arguments but 3 were given
>>> idraw = ImageDraw.Draw(im)
>>> idraw.line([(0, 0), (99, 99)], fill = (0, 0, 255), width = 2)
>>> im.save("C:\\python")
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2114, in save
    format = EXTENSION[ext]
KeyError: ''

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    im.save("C:\\python")
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2116, in save
    raise ValueError("unknown file extension: {}".format(ext))
ValueError: unknown file extension: 
>>> im.save()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    im.save()
TypeError: save() missing 1 required positional argument: 'fp'
>>> import os
>>> os.getcwd()
'/Users/hsiaotingluv/Desktop/python'
>>> im.save('/Users/hsiaotingluv/Desktop/python')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2114, in save
    format = EXTENSION[ext]
KeyError: ''

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    im.save('/Users/hsiaotingluv/Desktop/python')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2116, in save
    raise ValueError("unknown file extension: {}".format(ext))
ValueError: unknown file extension: 
>>> im.save('/Users/hsiaotingluv/Desktop/python/testimage.bmp')
>>> idraw.line([(0, 99), (99, 0)], fill = (255, 0, 0), width = 2)
>>> im.save('/Users/hsiaotingluv/Desktop/python/test2.bmp')
>>> idraw.rectangle([(10, 10), (40, 40)], fill = (0, 255, 0), outline = (0, 0, 0))
>>> im.save('/Users/hsiaotingluv/Desktop/python/test1.bmp')
>>> img.getcolor()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    img.getcolor()
AttributeError: 'PngImageFile' object has no attribute 'getcolor'
>>> coordinate
(0, 0)
>>> image.getpixel(coordinate)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    image.getpixel(coordinate)
NameError: name 'image' is not defined
>>> img.getpixel(coordinate)
(128, 0, 0, 0)
>>> image.getpixel((180, 69))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    image.getpixel((180, 69))
NameError: name 'image' is not defined
>>> imag.getpixel((180, 69))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    imag.getpixel((180, 69))
NameError: name 'imag' is not defined
>>> img.getpixel((180, 69))
(0, 0, 0, 255)
>>> img.getpixel((1800, 600))
(206, 157, 125, 255)
>>> img.paste("blue", (80, 80, 80, 200))
>>> img.show()
>>> img = Image.open("test1.bmp")
>>> img.paste("blue", (80, 80, 80, 200))
>>> img.show()
>>> img.paste("blue", (80, 20, 180, 200))
>>> img.show()
>>> img.show()
>>> img.thumbnail((120, 120))
>>> img.show()
>>> img.thumbnail((20, 20))
>>> img.show()
>>> img.thumbnail((1200, 1200))
>>> img.show()
>>> img.show()
>>> img.thumbnail((2880, 1800))
>>> img.show()
>>> img = Image.open("test1.bmp")
>>> img.show()
>>> img.resize((120, 80))
<PIL.Image.Image image mode=RGB size=120x80 at 0x101BA5CA0>
>>> img.show()
>>> img.resize((20, 80)).show()
>>> img.show()
>>> img.rotate(90).show()
>>> img.rotate(45).show()
>>> color = (0, 0, 0, 0)
>>> replace = (255, 255, 255, 255)
>>> newData = []
>>> for x in list(img.getdata()):
	if x == color:
		newData += [replace]
	else:
		newData += [x]

		
>>> img.rotate(45).show()
>>> for x in list(img.getdata()):
	if x == color:
		newData += [replace]
	else:
		newData += [x]

		
>>> newImage = Image.frombuffer( img.mode, img.size, newData)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    newImage = Image.frombuffer( img.mode, img.size, newData)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2675, in frombuffer
    return frombytes(mode, size, data, decoder_name, args)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 2615, in frombytes
    im.frombytes(data, decoder_name, args)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 797, in frombytes
    s = d.decode(data)
TypeError: a bytes-like object is required, not 'list'
>>> newImage = img.frombuffer( img.mode, img.size, newData)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    newImage = img.frombuffer( img.mode, img.size, newData)
AttributeError: 'BmpImageFile' object has no attribute 'frombuffer'
>>> rotatedImage.putdata(newData)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    rotatedImage.putdata(newData)
NameError: name 'rotatedImage' is not defined
>>> rotatedImage = img.rotate(45)
>>> rotatedImage.putdata(newData)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    rotatedImage.putdata(newData)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 1654, in putdata
    self.im.putdata(data, scale, offset)
TypeError: too many data entries
>>> rotatedImage.show()
>>> image = Image(150, 150)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    image = Image(150, 150)
TypeError: 'module' object is not callable
>>> im = Image.new('RGB', (100, 100), (255, 255, 255))
>>> idraw.line([(0, 0), (0, 0)], fill = (0, 0, 0), width = 2)
>>> idraw.line([(0, 0), (0, 0)], fill = (0, 0, 0), width = 2).show()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    idraw.line([(0, 0), (0, 0)], fill = (0, 0, 0), width = 2).show()
AttributeError: 'NoneType' object has no attribute 'show'
>>> im.save('/Users/hsiaotingluv/Desktop/python/test2.bmp')
>>> image = open("test2.bmp")
>>> image = Image.open("test2.bmp")
>>> image.info
{'dpi': (96, 96), 'compression': 0}
>>> image.height()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    image.height()
TypeError: 'int' object is not callable
>>> image.height
100
>>> img = Image.new('RGB', (250,250), "black")
>>> img.show
<bound method Image.show of <PIL.Image.Image image mode=RGB size=250x250 at 0x105B5FA60>>
>>> img.show()
>>> for y in range(img.height):    
	for x in range(img.width):
		pixels[x,y] = (x, y, (255, 0, 0))

		
Traceback (most recent call last):
  File "<pyshell#118>", line 3, in <module>
    pixels[x,y] = (x, y, (255, 0, 0))
NameError: name 'pixels' is not defined
>>> for y in range(img.height):
	for x in range(img.width):
		img.pixels[x,y] = (x, y, (255, 0, 0))

		
Traceback (most recent call last):
  File "<pyshell#120>", line 3, in <module>
    img.pixels[x,y] = (x, y, (255, 0, 0))
AttributeError: 'Image' object has no attribute 'pixels'
>>> img = Image.new('RGB', (250,250), "black")
>>> pixels = img.load()
>>> image_data = []
>>> img_data = []
>>> pixels = img.load()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		if pixels[i,j] != (255, 0, 0):
			pixels[i,j] = (255, 255, 255)

			
>>> img.show()
>>> for i in range(img.width, img.size):
	pixels[i, 50] = (255, 0, 0)

	
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    for i in range(img.width, img.size):
TypeError: 'tuple' object cannot be interpreted as an integer
>>> width = img.width
>>> width
250
>>> height = img.height
>>> for i in range(width, height):
	pixels[i, 50] = (255, 0, 0)

	
>>> im.show()
>>> img.show()
>>> for i in range(width, height):
	pixels[i, 50] = (255, 0, 0)

	
>>> img.show()
>>> 
>>> img.height
250
>>> for i in range(width, height):
	pixels[i, 150] = (255, 0, 0)

	
>>> img.show()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[i,150] = (255, 0, 0)

		
>>> img.show
<bound method Image.show of <PIL.Image.Image image mode=RGB size=250x250 at 0x105B5F790>>
>>> img.show()
>>> img.show()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[500,i] = (255, 0, 246)

		
Traceback (most recent call last):
  File "<pyshell#153>", line 3, in <module>
    pixels[500,i] = (255, 0, 246)
IndexError: image index out of range
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[50,i] = (255, 0, 246)

		
>>> img.show()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[100,i] = (25, 100, 246)

		
>>> img.show()
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		(r, g, b) = image.getpixel(x, y)
		average = (r, g, b) // 3
		if average < 128:
			pixels[x, y] = (0, 0, 0)
		else:
			pixels[x, y] = (255, 255, 255)

			
Traceback (most recent call last):
  File "<pyshell#166>", line 3, in <module>
    (r, g, b) = image.getpixel(x, y)
TypeError: getpixel() takes 2 positional arguments but 3 were given
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		(r, g, b) = image.getpixel((x, y))
		average = (r, g, b) // 3
		if average < 128:
			pixels[x, y] = (0, 0, 0)
		else:
			pixels[x, y] = (255, 255, 255)

			
Traceback (most recent call last):
  File "<pyshell#168>", line 4, in <module>
    average = (r, g, b) // 3
TypeError: unsupported operand type(s) for //: 'tuple' and 'int'
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		r, g, b = image.getpixel((x, y))
		average = (r + g + b) // 3
		if average < 128:
			pixels[x, y] = (0, 0, 0)
		else:
			pixels[x, y] = (255, 255, 255)

			
>>> img.show()
>>> r, g, b = image.getpixel((x, y))
>>> r
255
>>> g
255
>>> b
255
>>> r, g, b = image.getpixel((100, 5))
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    r, g, b = image.getpixel((100, 5))
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 1343, in getpixel
    return self.im.getpixel(xy)
IndexError: image index out of range
>>> r, g, b = image.getpixel((100, 50))
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    r, g, b = image.getpixel((100, 50))
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 1343, in getpixel
    return self.im.getpixel(xy)
IndexError: image index out of range
>>> r, g, b = image.getpixel((50, 50))
>>> r
255
>>> g
255
>>> b
255
>>> for i in range(img.size[0]):
	for j in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		average = (r + g + b) // 3
		if average < 128:
			pixels[x, y] = (0, 0, 0)
		else:
			pixels[x, y] = (255, 255, 255)

			
>>> img.show()
>>> img.getpixel((100, 50))
(25, 100, 246)
>>> r, g, b = img.getpixel((100, 50)))
SyntaxError: unmatched ')'
>>> r, g, b = img.getpixel((100, 50))
>>> r
25
>>> g
100
b
>>> average = (r + g + b) // 3
>>> average
123
>>> pixels[100, y] = (0, 0, 0)
>>> img.show()
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		average = (r + g + b) // 3
		if average < 128:
			pixels[x, y] = (0, 0, 0)
		else:
			pixels[x, y] = (255, 255, 255)

			
>>> img.show()
>>> img = Image.open("test1.bmp")
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = r * 0.299
		g = g * 0.587
		b = b * 0.114
		tgt = r + g + b
		pixels[x, y] = ((tgt, tgt, tgt))

		
Traceback (most recent call last):
  File "<pyshell#201>", line 8, in <module>
    pixels[x, y] = ((tgt, tgt, tgt))
TypeError: integer argument expected, got float
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		pixels[x, y] = ((tgt, tgt, tgt))

		
>>> img.show()
>>> img.size
(100, 100)
>>> r, g, b = img.getpixel((x, y))
>>> r, g, b = img.getpixel((20, 3))
>>> r
255
>>> g
255
b
>>> 
>>> b
255
>>> r, g, b = img.getpixel((20, 30))
>>> r
0
>>> g
255
b
>>> 
>>> b
0
>>> int(r * 0.299) + int(g * 0.587) + int(b * 0.114)
149
>>> tgt = 149
>>> pixels[20, 30] = ((tgt, tgt, tgt))
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		pixels[x, y] = ((tgt, tgt, tgt))

		
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		pixels[x, y] = ((0, 0, 0))

		
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		pixels[x, y] = (0, 0, 0)

		
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		img.putpixel((x, y), (0, 0, 0))

		
>>> img.show()
>>> img = Image.open("test1.bmp")
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		image.putpixel((x, y), (tgt, tgt, tgt))

		
>>> img.show()
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		tgt = (r + g + b) // 3
		image.putpixel((x, y), (tgt, tgt, tgt))

		
>>> img.show()
>>> 
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		image.putpixel((x, y), (tgt, tgt, tgt))
img.show()
SyntaxError: invalid syntax
>>> for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = img.getpixel((x, y))
		r = int(r * 0.299)
		g = int(g * 0.587)
		b = int(b * 0.114)
		tgt = r + g + b
		image.putpixel((x, y), (tgt, tgt, tgt))
	img.show()

	
>>> 
KeyboardInterrupt
>>> 
=================================== RESTART: Shell ===================================
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 48, in <module>
    pixels[x, y] = (255, 255, 255)
NameError: name 'pixels' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 65, in <module>
    img.draw()
AttributeError: 'BmpImageFile' object has no attribute 'draw'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 65, in <module>
    img.draw()
AttributeError: 'BmpImageFile' object has no attribute 'draw'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 98, in <module>
    blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 85, in blur
    centre = img.getpixel(x, y)
TypeError: getpixel() takes 2 positional arguments but 3 were given
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 98, in <module>
    blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 90, in blur
    sums = reduce(tripleSum, [centre, top, bottom, left, right])
NameError: name 'reduce' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 100, in <module>
    blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 96, in blur
    new.putpixel(x, y, averages)
TypeError: putpixel() takes 3 positional arguments but 4 were given
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 100, in <module>
    blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 96, in blur
    new.putpixel((x, y, averages))
TypeError: putpixel() missing 1 required positional argument: 'value'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
(0, 0, 1275)
(510, 510, 1275)
(765, 765, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
(1275, 1275, 1275)
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 104, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 101, in main
    new = blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 93, in blur
    print(sums)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
(0, 0, 255)
(102, 102, 255)
(153, 153, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 105, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 102, in main
    new = blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 96, in blur
    print(averages)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
(0, 0, 1275)
(0, 0, 255)
pasted
(510, 510, 1275)
(102, 102, 255)
pasted
(765, 765, 1275)
(153, 153, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
(255, 255, 255)
pasted
(1275, 1275, 1275)
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 109, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 106, in main
    new = blur(img)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 94, in blur
    print(sums)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Enter the value for edge detection: 10
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 140, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 138, in main
    detectEdges(img, value)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 121, in detectEdges
    centre = img.getpixel((x, y))
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 1343, in getpixel
    return self.im.getpixel(xy)
IndexError: image index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Enter the value for edge detection: 10
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 141, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 138, in main
    new = detectEdges(img, value)
  File "/Users/hsiaotingluv/Desktop/python/20200515 (file).py", line 121, in detectEdges
    centre = img.getpixel((x, y))
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/PIL/Image.py", line 1343, in getpixel
    return self.im.getpixel(xy)
IndexError: image index out of range
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200515 (file).py ===========
Enter the value for edge detection: 10
>>> 