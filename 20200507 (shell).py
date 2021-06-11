Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> aString = "hello"
>>> index = 0
>>> if index < len(aString):
	example(aString, index + 1)print(aString[index], end = "")
	
SyntaxError: invalid syntax
>>> if index < len(aString):
	example(aString, index + 1)print(aString[index], end = "")
	
SyntaxError: invalid syntax
>>> if index < len(aString):
	example(aString, index + 1)print(aString[index], end = "")
	
SyntaxError: invalid syntax
>>> if index < len(aString):
	example(aString, index + 1)
	print(aString[index], end = "")

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    example(aString, index + 1)
NameError: name 'example' is not defined
>>> while index < len(aString):
	print(aString[index], end = "")
	index += 1

	
hello
>>> while index < len(aString):
	index += 1
	print(aString[index], end = "")

	
>>> 
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
4
o 3
l 2
l 1
e 0
h None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
index is 4
o index is 3
l index is 2
l index is 1
e index is 0
h None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
index is 4
o
index is 3
l
index is 2
l
index is 1
e
index is 0
h
None
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200506 (file).py ===========
Enter a sentence and a number: hello,0
helloNone
>>> import os
>>> curDir = os.getcwd()
>>> print(curDir)
/Users/hsiaotingluv/Desktop/python
>>> os.mkdir('newDir')
>>> import time
>>> time.sleep(2)
>>> 
>>> os.rename('newDir','newDir2')
>>> time.sleep(2)

>>> help(os)

>>> print(curDir)
/Users/hsiaotingluv/Desktop/python
>>> os.chdir('/Users/hsiaotingluv/Desktop/')
>>> print(curDir)
/Users/hsiaotingluv/Desktop/python
>>> print(os.getcwd())
/Users/hsiaotingluv/Desktop
>>> print(os.listdir())
['musescore', 'Chen_Hsiao Ting_Resume.PDF', '.DS_Store', 'python', '.localized', 'Design ideas', 'others', 'photoshop', 'HCI ISP', 'NUS scholarship_files', 'Premiere Pro', 'wix pictures']
>>> os.makedirs('OS-Demo-2')
>>> os.makedirs('OS-Demo-2/Sub-Dir-1')
>>> os.removedirs('OS-Demo-2/Sub-Dir-1')
>>> os.removedirs('OS-Demo-2')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    os.removedirs('OS-Demo-2')
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/os.py", line 241, in removedirs
    rmdir(name)
OSError: [Errno 66] Directory not empty: 'OS-Demo-2'
>>> os.removedirs('OS-Demo-2\')
	      
SyntaxError: EOL while scanning string literal
>>> os.rename('test.txt','demo.txt')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    os.rename('test.txt','demo.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'test.txt' -> 'demo.txt'
>>> os.stat('OS-Demo-2')
os.stat_result(st_mode=16877, st_ino=37338645, st_dev=16777220, st_nlink=3, st_uid=502, st_gid=20, st_size=96, st_atime=1588812395, st_mtime=1588812354, st_ctime=1588812354)
>>> os.stat('OS-Demo-2').st_size
96
>>> from datetime import datetime
>>> mod_time = os.stat('OS-Demo-2').st_mtime
>>> print(datetime.fromtimestamp(mod_time))
2020-05-07 08:45:54.819116
>>> os.walk()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    os.walk()
TypeError: walk() missing 1 required positional argument: 'top'
>>> for dirpath, dirnames, filenames in os.walk(/Users/hsiaotingluv/Desktop):
	
SyntaxError: invalid syntax
>>> for dirpath, dirnames, filenames in os.walk("/Users/hsiaotingluv/Desktop"):
	print('current path:', dirpath)
	print('directories:', dirnames)
	print('files:', filenames)
	print()

	
current path: /Users/hsiaotingluv/Desktop
directories: ['musescore', 'python', 'OS-Demo-2', 'Design ideas', 'others', 'photoshop', 'HCI ISP', 'NUS scholarship_files', 'Premiere Pro', 'wix pictures']
files: ['Chen_Hsiao Ting_Resume.PDF', '.DS_Store', '.localized']

current path: /Users/hsiaotingluv/Desktop/musescore
directories: []
files: ['draft_2.mscz', '.作品2（原版）.mscz,', '作品2.3.mscz', '.作品1.mscx,', '.你的韵律.mscz,', '.DS_Store', '作品2.2.mscz', 'hong.mscz', '.HCI 100th.mscx,', '心有雨馨accompaniment.mscz', '转身的那一刻（编曲）.mscx', 'draft_2 有伴奏.mscz', '心有雨馨vocal.mscz', '.作品2（ver2）.mscz,', '阑珊灯火.mscz', '.心有雨馨accompaniment.mscz,', '飘啊飘.mscz', '阑珊灯火.pdf', '心有雨馨.mscz', '转身的那一刻.mscz', '作品2.4.mscz', '.转身的那一刻（编曲）.mscx,', '心有雨馨pdf.pdf', '.hci song.mscz,', '.hong.mscz,', '心有雨馨FINAL.mscz', '.作品2.3.mscz,', '繁华之未央.mscz', '友情的考验.pdf', '心有雨馨.pdf', '.心有雨馨draft3.mscz,', '塔罗说.mscz', '.心有雨馨draft4.mscz,', '友情的考验 .mscx', '心有雨馨2.mscz', '你的韵律.mscz', '.作品2.4.mscz,', '心有雨馨3.mscz', 'draft_无伴奏.mscz', '.心有雨馨draft41.mscz,', '歌曲（2）.mscx']

current path: /Users/hsiaotingluv/Desktop/python
directories: ['.vscode']
files: ['20200404 (payment).txt', 'conjunctions.txt', '20200502 (shell).py', '20200430 (shell).py', '20200420 (decrypt).txt', '20200503 (file).py', 'nouns.txt', '20200420 (file).py', '.DS_Store', 'test1.txt', '20200418 (file).py', '20200406 (file).py', '20200329  (shell).py', 'prepositions.txt', '20200402  (shell).py', '20200502 (file).py', '20200405 (shell).py', '20200329 (file).py', '20200326 (shell) (zh).py', '20200325  (shell).py', '20200328(file).py', '20200504 (file).py', '20200326 shell.py', '20200403 (shell).py', '20200420 (encrypt).txt', 'adjectives.txt', '20200430 (file).py', '20200428 (shell).py', '20200402(file).py', '20200501 (file).py', '20200506 (shell).py', '20200403 (file).py', '20200420 (shell).py', '20200326(file).py', '20200329(test).txt', '20200406 (shell).py', 'test.txt', '20200504 (shell).py', '20200325 (game file).py', '20200501 (shell).py', '20200404(file).py', '2018 lesson1~10.py', '20200418 (shell).py', 'articles.txt', 'verbs.txt', '20200506 (file).py', '20200404 (shell).py', '20200328  (shell).py']

current path: /Users/hsiaotingluv/Desktop/python/.vscode
directories: []
files: ['settings.json']

current path: /Users/hsiaotingluv/Desktop/OS-Demo-2
directories: []
files: ['.DS_Store']

current path: /Users/hsiaotingluv/Desktop/Design ideas
directories: []
files: ['Screenshot 2019-09-27 at 1.32.02 PM.png', 'Screenshot 2019-09-27 at 1.26.29 PM.png', 'Screenshot 2019-09-27 at 1.25.55 PM.png', 'Screenshot 2019-09-27 at 1.27.37 PM.png', 'Screenshot 2019-09-27 at 1.30.53 PM.png']

current path: /Users/hsiaotingluv/Desktop/others
directories: []
files: ['desktop photo.pptx', '校园写作.docx', '作文.docx', '《互联网时代的名人》.pdf', 'scripts.docx', '陈筱婷，真实语料.docx']

current path: /Users/hsiaotingluv/Desktop/photoshop
directories: []
files: ['weiyang a5 back -2.jpg', '.DS_Store', 'CLASSPHOTO.psd', 'IMG-20190115-WA0050.BMP', 'Screenshot 2019-11-30 at 1.01.58 AM.png', '18S6B.pdf', 'final front.jpg']

current path: /Users/hsiaotingluv/Desktop/HCI ISP
directories: []
files: ['O Level.pdf', 'sph internship.jpg', 'CCA Portfolio Certiﬁcate.pdf', 'CIP Certificate.pdf', 'J2 Overall results.pdf', 'YFC merit award.jpg', 'testimonial(A).jpg', 'J1 Overall results.pdf', 'HCI diploma (2).jpg', 'HCI diploma.jpg', 'J2 BT2 results.pdf', 'J1 CA results.pdf', 'J2 BT1 results.pdf', 'Discipline Records.pdf', 'O Level (2).jpg', 'J2 Preliminary results.pdf', 'Admissions Data.pdf', 'J1 BT results.pdf', 'My ID.jpg', 'O Level (1).jpg', 'NRIC.jpg', 'ID:student card.pdf', 'A Level PW result.pdf', 'Personal Particulars.pdf', 'Past Records.pdf', 'A Level PW.jpg', 'A Level.pdf', 'My Subjects.pdf', 'chinmeihuaID.jpg', 'Testimonial(O).jpg', 'J1 Promotional results.pdf']

current path: /Users/hsiaotingluv/Desktop/NUS scholarship_files
directories: []
files: ['bootstrap.min.css', 'jquery.validate.min.js', 'jquery-ui.min.js', 'jquery-ui.min.css', 'oam.js', 'diskett2.gif', 'printr02.gif', 'linkbar2.gif', 'jquery.min.js', 'bootstrap.min.js', 'title.gif', 'nus.gif', 'nusstyles.css', 'oam.css', 'cata.js']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro
directories: ['music', 'hsiaohong', 'youtube videos', 'sound effect', 'Transition Premiere Pro', 'youtube photo']
files: ['Screenshot 2019-11-30 at 10.58.54 PM.png', 'Channel Art Template (Photoshop).png', '.DS_Store', 'premierepro.pptx', '未央 (final).mov', 'youtube 1280x720.png', 'Screenshot 2018-12-04 at 5.08.32 PM.png']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/music
directories: []
files: ['Purple Planet Music - Inspirational - Successful Motivation.mp3', 'Purple Planet Music - Inspirational - Teamwork.mp3', 'happythoughts.mp3']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/hsiaohong
directories: []
files: ['ChangiBeach.mp4', 'hsiaohong1.mp4', 'hsiaohong3.mp4', 'hsiaohong2.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/youtube videos
directories: []
files: ['HCI prom.mp4', 'youtube 台湾和新加坡的生活差异.mp4', '.DS_Store', 'H2CLL考试.mp4', 'AVENGERS ENDGAME Trailer 2 Music Version Best Proper Movie Trailer Soundtrack Final Theme Son.mp4', 'ALevelResultsDay.mp4', '18S6BClass BBQ.mp4', '2020除夕夜.mp4', 'campus tour.mp4', '18S6B class montage final 1.mp4', 'Internship.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/sound effect
directories: []
files: ['game1.wav', 'hit1.wav', '.DS_Store', 'beep.wav', 'bomb explode.wav', 'hit4.wav', 'woosh1.wav', 'thingsdropping.aiff', 'spinning.wav', 'woosh2.wav', 'ending song.mp3', 'ring1.mp3', 'seagull.mp3', 'spray.wav', 'camera.wav', 'Popular sound effects YouTubers use.mp3', 'ending music.mp3', 'fire cracker explode.wav']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro
directories: ['Tutorial', 'Other Pruducts for Premiere Pro', 'Motion Presets', 'Color Corrections', 'Mogrt', 'Assets']
files: ['.DS_Store']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Tutorial
directories: []
files: ['CHANGE RESOLUTION.pdf', 'Solution to the problem missing files.pdf']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Other Pruducts for Premiere Pro
directories: []
files: ['Video Library for Premiere Pro by nitrozme - VideoHive.url', 'Instagram Library for Premiere Pro by nitrozme - VideoHive.url', 'Premiere Library - Most Handy Effects by nitrozme - VideoHive.url', 'Effects Pack by nitrozme - VideoHive.url', 'Motion Text Presets by nitrozme - VideoHive.url']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Motion Presets
directories: ['Project File', 'Video Tutorial']
files: ['.DS_Store']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Motion Presets/Project File
directories: []
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Motion Presets/Video Tutorial
directories: []
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Color Corrections
directories: []
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Mogrt
directories: []
files: ['transition_47.mogrt', 'transition_02.mogrt', 'transition_63.mogrt', 'transition_26.mogrt', 'transition_61.mogrt', 'transition_24.mogrt', 'transition_19.mogrt', 'transition_45.mogrt', 'transition_39.mogrt', 'transition_41.mogrt', 'transition_04.mogrt', 'transition_65.mogrt', 'transition_20.mogrt', 'transition_58.mogrt', 'transition_67.mogrt', 'transition_22.mogrt', 'transition_43.mogrt', 'transition_06.mogrt', 'transition_18.mogrt', 'transition_25.mogrt', 'transition_60.mogrt', 'transition_01.mogrt', 'transition_44.mogrt', 'transition_03.mogrt', 'transition_46.mogrt', 'transition_27.mogrt', 'transition_62.mogrt', 'transition_23.mogrt', 'transition_66.mogrt', 'transition_07.mogrt', 'transition_42.mogrt', 'transition_05.mogrt', 'transition_40.mogrt', 'transition_38.mogrt', 'transition_59.mogrt', 'transition_21.mogrt', 'transition_64.mogrt', 'transition_55.mogrt', 'transition_10.mogrt', 'transition_34.mogrt', 'transition_09.mogrt', 'transition_36.mogrt', 'transition_57.mogrt', 'transition_12.mogrt', 'transition_53.mogrt', 'transition_16.mogrt', 'transition_32.mogrt', 'transition_30.mogrt', 'transition_48.mogrt', 'transition_29.mogrt', 'transition_51.mogrt', 'transition_14.mogrt', 'transition_37.mogrt', 'transition_13.mogrt', 'transition_56.mogrt', 'transition_11.mogrt', 'transition_54.mogrt', 'transition_08.mogrt', 'transition_35.mogrt', 'transition_49.mogrt', 'transition_31.mogrt', 'transition_15.mogrt', 'transition_50.mogrt', 'transition_28.mogrt', 'transition_17.mogrt', 'transition_52.mogrt', 'transition_33.mogrt']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets
directories: ['Background', 'TR_Smudge', 'LL', 'LIGHT Preview', 'TR_Glitch', 'Audio FX', 'NEW', 'GLITCH PRESETS', 'Preview', 'TR_Glass', 'TR_Grunge', 'TR_Modern']
files: ['.DS_Store', 'Thug_Image_700px.png']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/Background
directories: []
files: ['8.jpg', '9.jpg', '14.jpg', '15.jpg', '12.jpg', '13.jpg', '11.jpg', '10.jpg', '4.jpg', '5.jpg', '7.jpg', '6.jpg', '2.jpg', '3.jpg', '1.jpg']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/TR_Smudge
directories: []
files: ['TR_Smudge_Flash.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LL
directories: []
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview
directories: ['Light motion 105mm', 'Light motion 35mm', 'Light motion 50mm', 'Light']
files: ['.DS_Store']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light motion 105mm
directories: []
files: ['Flat right 1x.mp4', 'Flat Up 1x.mp4', 'Flat down  1x.mp4', 'Flat Left 1x.mp4', 'Flat Left 2x.mp4', 'Flat down  2x.mp4', 'Flat right 2x.mp4', 'Flat Up 2x.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light motion 35mm
directories: []
files: ['Flat right 1x.mp4', 'Flat Up 1x.mp4', 'Flat down  1x.mp4', 'Flat Left 1x.mp4', 'Flat Left 2x.mp4', 'Flat down  2x.mp4', 'Flat right 2x.mp4', 'Flat Up 2x.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light motion 50mm
directories: []
files: ['Flat right 1x.mp4', 'Flat Up 1x.mp4', 'Flat down  1x.mp4', 'Flat Left 1x.mp4', 'Flat Left 2x.mp4', 'Flat down  2x.mp4', 'Flat right 2x.mp4', 'Flat Up 2x.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light
directories: ['105 mm', '50 mm', '35mm']
files: ['.DS_Store']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light/105 mm
directories: []
files: ['Down Right.mp4', 'Right.mp4', 'Left.mp4', 'Down.mp4', 'Up Left.mp4', 'Up Right.mp4', 'Zoom.mp4', 'Up.mp4', 'Down Left.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light/50 mm
directories: []
files: ['Down Right.mp4', 'Right.mp4', 'Left.mp4', 'Down.mp4', 'Up Left.mp4', 'Up Right.mp4', 'Zoom.mp4', 'Up.mp4', 'Down Left.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/LIGHT Preview/Light/35mm
directories: []
files: ['Down Right.mp4', 'Right.mp4', 'Left.mp4', 'Down.mp4', 'Up Left.mp4', 'Up Right.mp4', 'Zoom.mp4', 'Up.mp4', 'Down Left.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/TR_Glitch
directories: []
files: ['TR_Glitch_Roll_Down.mp4', 'TV Glitch_03_ML.mp4', 'TV Glitch_01_ML.mp4', 'TR_Glitch_Roll_Up.mp4', 'TV Glitch_02_ML.mp4', 'TR_Glitch_Roll_Right.mp4', 'Glitch_Rewind_02.mp4', 'Glitch_Rewind_03.mp4', 'Glitch_Rewind_01.mp4', 'TR_Glitch_Roll_Left.mp4', 'Glitch.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/Audio FX
directories: []
files: ['Whoosh_Panoramed_10.wav', 'Whoosh_Panoramed_1.wav', 'Whoosh_Panoramed_12.wav', 'Whoosh_15.wav', 'Whoosh_16.wav', '4_Classical_Whoosh_Soft_Elements.wav', 'Soft_Whoosh_12.wav', 'Soft_Whoosh_22.wav', 'Whooshe_Modern_12.wav', 'Whoosh_19.wav', 'Soft_Whoosh_33.wav', 'Whoosh_18.wav']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW
directories: ['Blocks Vertical Glow P', 'GLOW P', 'Blocks Horizontal Glow P']
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW/Blocks Vertical Glow P
directories: []
files: ['Blocks -02.mp4', 'Blocks -16.mp4', 'Blocks -17.mp4', 'Blocks -03.mp4', 'Blocks -15.mp4', 'Blocks -01.mp4', 'Blocks -14.mp4', 'Blocks -10.mp4', 'Blocks -04.mp4', 'Blocks -05.mp4', 'Blocks -11.mp4', 'Blocks -07.mp4', 'Blocks -13.mp4', 'Blocks -18_1.mp4', 'Blocks -12.mp4', 'Blocks -06.mp4', 'Blocks -08_1.mp4', 'Blocks -08.mp4', 'Blocks -21.mp4', 'Blocks -19.mp4', 'Blocks -18.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW/GLOW P
directories: ['Flat', 'Shake', 'Elastic', 'Stretch', 'Short', 'Bounce']
files: []

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW/GLOW P/Flat
directories: []
files: ['Flat down-.mp4', 'Flat right.mp4', 'Flat Up Fast.mp4', 'Flat Left Fast.mp4', 'Flat right Fast.mp4', 'Flat down  Fast.mp4', 'Flat Left.mp4', 'Flat Up.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW/GLOW P/Shake
directories: []
files: ['Flat down-.mp4', 'Flat right.mp4', 'Flat Up Fast.mp4', 'Flat Left Fast.mp4', 'Flat right Fast.mp4', 'Flat down  Fast.mp4', 'Flat Left.mp4', 'Flat Up.mp4']

current path: /Users/hsiaotingluv/Desktop/Premiere Pro/Transition Premiere Pro/Assets/NEW/GLOW P/Elastic
Traceback (most recent call last):
  File "<pyshell#47>", line 2, in <module>
    print('current path:', dirpath)
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> os.environ.get('HOME')
'/Users/hsiaotingluv'
>>> file_path = os.path.join(os.environ.get('HOME'),'test.txt')
>>> print(file_path)
/Users/hsiaotingluv/test.txt
>>> os.path.basename('/dir/file.txt')
'file.txt'
>>> os.path.dirname('/dir/file.txt')
'/dir'
>>> os.path.split('/dir/file.txt')
('/dir', 'file.txt')
>>> os.path.exists('/dir/file.txt')
False
>>> os.path.isdir('/dir/file.txt')
False
>>> os.path.isfile('/dir/file.txt')
False
>>> os.path.splitext('/dir/file.txt')
('/dir/file', '.txt')
>>> dir(os.path)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
>>> os.stat('Premiere Pro')
os.stat_result(st_mode=16877, st_ino=34625723, st_dev=16777220, st_nlink=15, st_uid=502, st_gid=20, st_size=480, st_atime=1588812935, st_mtime=1585630598, st_ctime=1585630598)
>>> print(os.getcwd())
/Users/hsiaotingluv/Desktop
>>> print(curDir)
/Users/hsiaotingluv/Desktop/python
>>> os.chdir('/Users/hsiaotingluv/Desktop/')
>>> curDir
'/Users/hsiaotingluv/Desktop/python'
>>> os.getcwd()
'/Users/hsiaotingluv/Desktop'
>>> os.getcwd().stats
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    os.getcwd().stats
AttributeError: 'str' object has no attribute 'stats'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 116, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 14, in main
    print(os.getcwd())
NameError: name 'os' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 1
Below is the list of current directory
20200404 (payment).txt
conjunctions.txt
20200502 (shell).py
20200430 (shell).py
20200420 (decrypt).txt
20200503 (file).py
nouns.txt
20200420 (file).py
.DS_Store
test1.txt
20200418 (file).py
20200406 (file).py
20200329  (shell).py
prepositions.txt
20200402  (shell).py
20200502 (file).py
20200405 (shell).py
20200329 (file).py
20200326 (shell) (zh).py
20200325  (shell).py
20200328(file).py
20200504 (file).py
20200326 shell.py
20200403 (shell).py
20200420 (encrypt).txt
adjectives.txt
20200430 (file).py
20200428 (shell).py
20200402(file).py
20200501 (file).py
20200506 (shell).py
20200403 (file).py
20200420 (shell).py
20200326(file).py
20200329(test).txt
20200406 (shell).py
20200507 (file).py
test.txt
.vscode
20200504 (shell).py
20200325 (game file).py
20200501 (shell).py
20200404(file).py
2018 lesson1~10.py
20200418 (shell).py
articles.txt
verbs.txt
20200506 (file).py
20200404 (shell).py
20200328  (shell).py
>>> 
KeyboardInterrupt
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 1
Below is the list of current directory
20200404 (payment).txt
conjunctions.txt
20200502 (shell).py
20200430 (shell).py
20200420 (decrypt).txt
20200503 (file).py
nouns.txt
20200420 (file).py
.DS_Store
test1.txt
20200418 (file).py
20200406 (file).py
20200329  (shell).py
prepositions.txt
20200402  (shell).py
20200502 (file).py
20200405 (shell).py
20200329 (file).py
20200326 (shell) (zh).py
20200325  (shell).py
20200328(file).py
20200504 (file).py
20200326 shell.py
20200403 (shell).py
20200420 (encrypt).txt
adjectives.txt
20200430 (file).py
20200428 (shell).py
20200402(file).py
20200501 (file).py
20200506 (shell).py
20200403 (file).py
20200420 (shell).py
20200326(file).py
20200329(test).txt
20200406 (shell).py
20200507 (file).py
test.txt
.vscode
20200504 (shell).py
20200325 (game file).py
20200501 (shell).py
20200404(file).py
2018 lesson1~10.py
20200418 (shell).py
articles.txt
verbs.txt
20200506 (file).py
20200404 (shell).py
20200328  (shell).py
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 1
Below is the list of current directory
20200404 (payment).txt
conjunctions.txt
20200502 (shell).py
20200430 (shell).py
20200420 (decrypt).txt
20200503 (file).py
nouns.txt
20200420 (file).py
.DS_Store
test1.txt
20200418 (file).py
20200406 (file).py
20200329  (shell).py
prepositions.txt
20200402  (shell).py
20200502 (file).py
20200405 (shell).py
20200329 (file).py
20200326 (shell) (zh).py
20200325  (shell).py
20200328(file).py
20200504 (file).py
20200326 shell.py
20200403 (shell).py
20200420 (encrypt).txt
adjectives.txt
20200430 (file).py
20200428 (shell).py
20200402(file).py
20200501 (file).py
20200506 (shell).py
20200403 (file).py
20200420 (shell).py
20200326(file).py
20200329(test).txt
20200406 (shell).py
20200507 (file).py
test.txt
.vscode
20200504 (shell).py
20200325 (game file).py
20200501 (shell).py
20200404(file).py
2018 lesson1~10.py
20200418 (shell).py
articles.txt
verbs.txt
20200506 (file).py
20200404 (shell).py
20200328  (shell).py
Enter a number: 2
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 3
Enter the name of directory: 
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 43, in runCommand
    moveDown(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 72, in moveDown
    name = input("Enter the name of directory: ")
KeyboardInterrupt
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
Enter a number: 2
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 3
Enter the name of directory: Desktop
You have moved to the next directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 4
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 47, in runCommand
    countFiles(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 89, in countFiles
    count += countFiles(getcwd())
UnboundLocalError: local variable 'count' referenced before assignment
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 4
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 47, in runCommand
    countFiles(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 89, in countFiles
    num += countFiles(getcwd())
NameError: name 'getcwd' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 4
The total number of files is 1576
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 51, in runCommand
    sizeCWD(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 102, in sizeCWD
    size += sizeCWD(getcwd())
NameError: name 'getcwd' is not defined
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
The total number of bytes is 23555325583
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 6
Enter the search string: Premier Pro
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 55, in runCommand
    fileList = searchFile(target, os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 114, in searchFile
    os.chdir(element)
NotADirectoryError: [Errno 20] Not a directory: 'Chen_Hsiao Ting_Resume.PDF'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 6
Enter the search string: Premiere Pro
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 55, in runCommand
    fileList = searchFile(target, os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 114, in searchFile
    os.chdir(element)
NotADirectoryError: [Errno 20] Not a directory: '20200404 (payment).txt'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 6
Enter the search string: txt
/Users/hsiaotingluv/Desktop/python/20200404 (payment).txt
/Users/hsiaotingluv/Desktop/python/conjunctions.txt
/Users/hsiaotingluv/Desktop/python/20200420 (decrypt).txt
/Users/hsiaotingluv/Desktop/python/nouns.txt
/Users/hsiaotingluv/Desktop/python/test1.txt
/Users/hsiaotingluv/Desktop/python/prepositions.txt
/Users/hsiaotingluv/Desktop/python/20200420 (encrypt).txt
/Users/hsiaotingluv/Desktop/python/adjectives.txt
/Users/hsiaotingluv/Desktop/python/20200329(test).txt
/Users/hsiaotingluv/Desktop/python/test.txt
/Users/hsiaotingluv/Desktop/python/articles.txt
/Users/hsiaotingluv/Desktop/python/verbs.txt
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 6
Enter the search string: youtube
String not found
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: youtube
Please enter a correct number
Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 6
Enter the search string: youtube
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 119, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 61, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 55, in runCommand
    fileList = searchFile(target, os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 115, in searchFile
    files.extend(searchFile(target, os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 115, in searchFile
    files.extend(searchFile(target, os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 108, in searchFile
    lyst = os.listdir(path)
PermissionError: [Errno 1] Operation not permitted: '/Users/hsiaotingluv/Pictures/Photos Library.photoslibrary'
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 1
Below is the list of current directory
20200404 (payment).txt
conjunctions.txt
20200502 (shell).py
20200430 (shell).py
20200420 (decrypt).txt
20200503 (file).py
nouns.txt
20200420 (file).py
.DS_Store
test1.txt
20200418 (file).py
20200406 (file).py
20200329  (shell).py
prepositions.txt
20200402  (shell).py
20200502 (file).py
20200405 (shell).py
20200329 (file).py
20200326 (shell) (zh).py
20200325  (shell).py
20200328(file).py
20200504 (file).py
20200326 shell.py
20200403 (shell).py
20200420 (encrypt).txt
adjectives.txt
20200430 (file).py
20200428 (shell).py
20200402(file).py
20200501 (file).py
20200506 (shell).py
20200403 (file).py
20200420 (shell).py
20200326(file).py
20200329(test).txt
20200406 (shell).py
20200507 (file).py
test.txt
.vscode
20200504 (shell).py
20200325 (game file).py
20200501 (shell).py
20200404(file).py
2018 lesson1~10.py
20200418 (shell).py
articles.txt
verbs.txt
20200506 (file).py
20200404 (shell).py
20200328  (shell).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 1
Below is the list of current directory
musescore
Chen_Hsiao Ting_Resume.PDF
.DS_Store
python
.localized
Design ideas
others
photoshop
HCI ISP
Premiere Pro
wix pictures
/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 120, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 51, in runCommand
    sizeCWD(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 97, in sizeCWD
    lyst = os.listdir(path)
PermissionError: [Errno 1] Operation not permitted: '/Users/hsiaotingluv/Pictures/Photos Library.photoslibrary'
>>> 
=== RESTART: /Users/hsiaotingluv/Desktop/python/20200507 (file).py ===
/Users/hsiaotingluv/Desktop/python
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
The total number of bytes is 23555325579

/Users/hsiaotingluv/Desktop
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 2
You have moved to the previous directory

/Users/hsiaotingluv
1 List the current directory 
2 Move up 
3 Move down 
4 Number of files in the directory 
5 Size of the directory in bytes 
6 Search for a filename 
7 Quit the program 

Enter a number: 5
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 120, in <module>
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 62, in runCommand
    main()
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 19, in main
    runCommand(command)
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 51, in runCommand
    sizeCWD(os.getcwd()))
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 103, in sizeCWD
    size += sizeCWD(os.getcwd())
  File "/Users/hsiaotingluv/Desktop/python/20200507 (file).py", line 97, in sizeCWD
    lyst = os.listdir(path)
PermissionError: [Errno 1] Operation not permitted: '/Users/hsiaotingluv/Pictures/Photos Library.photoslibrary'
>>> 