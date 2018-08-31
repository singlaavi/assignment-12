#Q.1- Print the Current Day
import datetime as d
date=d.date.today()
print('DATE IS:',date)
print('WEEKDAY IS:',date.strftime("%A"))


#Q.2- Use Webbrowser Module in Python
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=rfscVS0vtbw")


#Q.3- Rename All the Files in a Directory And Convert Them Into .jpg File Format

import os,sys
folder = r'C:\Users\AVI\Desktop\ASSIGNMENTS\assignment-12'
for file in os.listdir(folder):
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)
