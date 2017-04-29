#! /usr/bin/python2.7
# cm.py - Code manager (Your way to organised code)
############################### USAGE ####################################
# 1. To clean the kitchen(Copy the problem url to clip-board):
#						./cm.py clean - takes out the garbage :p
# 2. To save a new code:
#						./cm.py <fileName> 
# 						and follow the instructions on the screen
# 3. To make a note:
#						./cm.py note
# 						select the topic, and write the note
# 4. To read a note:
#						./cm.py readnote
#						select the topic, and read the notes
##########################################################################


import requests,shutil,os,pyperclip,sys

def getDir(cat):
	locDict = {1:'dp/',2:'graph/',3:'numberTheory/',4:'segTree/',5:'misc/'}
	return '/media/sandeep/Sandeep/myCodes/' + locDict[cat]

if sys.argv[1].lower() == 'clean':
	filesList = os.listdir('/media/sandeep/Sandeep/cooking/')
	del filesList[filesList.index('cm.py')]
	for fileName in filesList:
		os.unlink('/media/sandeep/Sandeep/cooking/'+fileName)
	sys.exit()

if sys.argv[1].lower() == 'note':
	print '1. DP\n2. Graph theory\n3. Number theory\n4. Segment tree\n5. Misc\n'
	print 'Select category: ',
	cat = input()
	print 'Enter the note (Press ENTER when done):'
	note = raw_input()
	newdir = getDir(cat)
	f = open(newdir + 'notes.txt','a')
	f.write('* ' + note+'\n')
	f.close()
	sys.exit()

if sys.argv[1].lower() == 'readnote':
	print '1. DP\n2. Graph theory\n3. Number theory\n4. Segment tree\n5. Misc\n'
	print 'Select category: ',
	cat = input()
	newdir = getDir(cat)
	f = open(newdir + 'notes.txt','r')
	print f.read()
	f.close()
	sys.exit()

fileName = sys.argv[1]
url = pyperclip.paste()
origFile = '/media/sandeep/Sandeep/cooking/' + sys.argv[1]
print 'Want to rename (y/n): ',
choice = raw_input()
choice.lower()
if choice == 'y':
	print 'Enter new name: ',
	ext = fileName.split('.')[1]
	fileName = raw_input()
	fileName = fileName + '.' + ext

print '1. DP\n2. Graph theory\n3. Number theory\n4. Segment tree\n5. Misc\n'
print 'Select category: ',
cat = input()
newdir = getDir(cat)
shutil.move(origFile,newdir+fileName)
problemWebPage = requests.get(url)
buff = open(newdir+fileName.split('.')[0]+'_problem.html','w')
for chunk in problemWebPage.iter_content(100000):
	buff.write(chunk)
buff.close()
