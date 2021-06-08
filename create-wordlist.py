import datetime
from tkinter import *
import os
import itertools
#---------------------------
#date functions
def weekdayFromInt(weekday):
    if weekday == 0:
        return "Monday"
    if weekday == 1:
        return "Tuesday"
    if weekday == 2:
        return "Wednesday"
    if weekday == 3:
        return "Thursday"
    if weekday == 4:
        return "Friday"
    if weekday == 5:
        return "Saturday"
    if weekday == 6:
        return "Sunday" 
def multipleDateFormats(date):
    x=0
    day=''
    month=''
    year=''
    dates=[]
    for c in date:
        if(c=='/'):
            x=x+1
        elif(x<1):
            day=day+c
        elif(x<2):
            month=month+c
        else:
            year=year+c
    lasttwo=year[2]+year[3]
    datentime=datetime.datetime(int(year),int(month),int(day))
    dates.append(day+month)
    dates.append(day+year)
    dates.append(month+year)
    dates.append(day+month+year)
    dates.append(month+day)
    dates.append(year+month+day)
    dates.append(day+month)
    dates.append(day+lasttwo)
    dates.append(month+lasttwo)
    dates.append(day+month+lasttwo)
    dates.append(month+day)
    dates.append(lasttwo+month+day)
    wkday=weekdayFromInt(datentime.weekday())
    l=len(dates)
    for i in range(0,l):
        dates.append(wkday+dates[i])
        dates.append(dates[i]+wkday)
    dates.append(day+'/'+month)
    dates.append(day+'/'+lasttwo)
    dates.append(month+'/'+lasttwo)
    dates.append(day+'/'+month+'/'+lasttwo)
    dates.append(month+'/'+day)
    dates.append(lasttwo+'/'+month+'/'+day)
    dates.append(day)
    dates.append(month)
    dates.append(year)
    return dates
#-----------------------------------------
#pre
details=[]
form=Tk()
inputs=Frame(form)
inputs.grid(row=0,column=1)
headings=Frame(form)
headings.grid(row=0,column=0)
dates=Frame(form)
dates.grid(row=0,column=3)
dateheading=Frame(form,height=1)
dateheading.grid(row=0,column=2)
#----------------------------
#getting UI ready
titles=['First name','Last name','Pet name', 'Mothers name', 'Fathers name','Address']
titles.extend(['School','College','Girlfriend/Boyfriend','Hometown','Known password'])
count=0
for i in titles:
    Label(headings,text=i).grid(row=count,column=0)
    Entry(inputs).grid(row=count,column=1)
    count=count+1
Label(dateheading,text="Add significant\n dates(Birthdays, \nanniversaries, etc)\n[DD/MM/YYYY]",height=4).grid(row=1,column=2)
Entry(dates).grid(row=1,column=3)
def addMore():
    Entry(inputs).grid(column=1)
def addDates():
    Entry(dates).grid(column=3)
"""Label(headings,text="How many permutations\n of inputs would\n you like?\neg:inputs=(a,b,c),\n permutations = 2.\n output = (ab,bc,ca,ac,cb,ba)\nDefault is 2").grid(column=0)
permentry=Entry(headings).grid(column=0)"""
#------------------------------------
#doing the main stuff
def main():    
    datelist=[]
    for child in inputs.winfo_children():
        ip=child.get()
        if(not ip==''):
            details.extend(ip.split())
    for child in dates.winfo_children():
        ip=child.get()
        if(not ip==''):
            datelist.extend(multipleDateFormats(ip))
    """perms=permentry.get()
    if(not perms==''):
        permutationtimes=int(perms)"""
    details.extend(datelist)
    dets=list(set(details))
    #print(dets)
    #please edit this value if you would like permutations with more than 2 elements. Note: this may drastically increase compuation time.
    permutationtimes=2
    for perm in itertools.permutations(dets,permutationtimes):
        s=''
        for string in perm:
            s=s+string            
        dets.append(s)
    dets.sort()
    filelocn='C:\Users\Aditya\john\run\wordlist'
    fileformat='.lst'
    if(os.path.isfile(filelocn+fileformat)):
        j=1
        while(os.path.isfile(filelocn+str(j)+fileformat)):
            j=j+1
        os.rename(filelocn+fileformat,filelocn+str(j)+fileformat)
    with open(filelocn+fileformat,'w') as file:
        for p in dets:
            file.write('%s\n' % p)
    file.close()
    form.destroy()
#--------------------------
#end of program
Button(headings,text='Add more information',command=addMore).grid(column=0)
Button(dateheading,text='Add more dates',command=addDates).grid(column=2)
Label(form,text="PLEASE ENTER AS MUCH INFORMATION THAT YOU ARE AWARE OF",fg='red').grid(column=1)
Button(form,text='Submit',command=main,width=10,height=5,fg='red').grid(column=1)
form.mainloop()
#------------------------
