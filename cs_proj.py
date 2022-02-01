import pickle
import sys
import csv
from random import shuffle

list4=["Adm.no","Name                ","Sec","Marks","Remarks"]
ans_hist = []
def prnt(rec,heading):
    print()
    for k in heading:
        print(k,end="\t")
    print("\n----------------------------------------------------------------------")
    for i in rec:
        for j in i:
            print(j,end="\t")
        if i[3]>=90:
            rem="Excellent"
        elif i[3]>=80:
            rem="Good"
        elif i[3]>=70:
            rem="Average"
        elif i[3]>=50:
            rem="Below average"
        else:
            rem="Needs improvement"
        print(rem,end="")
        print()

def runpy(ch=9):
    print('''
-----------------------------------------------------------
Which operation do you wat to perform ?

1. Write
2. Read
3. Append
4. Search
5. Update
6. Delete
7. Sort
8. Filter
9. Create csv file
10.Exit
-----------------------------------------------------------
''')
    ch=int(input("Enter Your choice :"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        append()
    elif ch==4:
        global user
        user=1
        search()
    elif ch==5:
        update()
    elif ch==6:
        delete()
    elif ch==7:
        sort()
    elif ch==8:
        Filter()
    elif ch==9:
        csvfile()
    elif ch==10:
        sys.exit()
    else:
        print("\nWrong choice entered. Please !! Enter a valid choice.")




def write():
    f=open("stdetails.dat",'wb')
    rec=[]
    ch='y'
    while ch in 'Yy':
        roll=int(input('Enter Admission no.:'))
        name=input('Enter Name(max 13 characters):')
        sec=input('Enter Section:')
        mrk=int(input("Enter marks in percent(0 to 100):"))
        while True:
            if mrk>=0 and mrk<=100:
                break
            mrk=int(input('Pleas enter Marks in percent (0 to 100):'))
        
        lst=[roll,name.capitalize()+" "*(20-len(name)),sec.upper(),mrk]
        rec.append(lst)
        ch=input('Do you want to Continue? :')
        if ch in 'Nn':
            break
    pickle.dump(rec,f)
    f.close()
    
    print('\nData written succesfully !!..')
    
def read():
    f=open("stdetails.dat",'rb')
    rec=pickle.load(f)
    prnt(rec,list4)

    f.close()
    print('\nData read succesfully !!..')
    ch=input("Want to read again?(y/n): ")
    if ch in "Yy":
        read()
 

def append():

    f=open("stdetails.dat",'rb+')
    data=pickle.load(f)
    ch='y'
    while ch in 'Yy':
        roll=int(input('Enter Admission no.:'))
        name=input('Enter Name(max 13 character):')
        sec=input('Enter Section:')
        mrk=int(input("Enter marks in percent(0 to 100):"))
        while True:
            if mrk>=0 and mrk<=100:
                break
            mrk=int(input('Pleas enter Marks in percent (0 to 100):'))
        lst=[roll,name.capitalize()+" "*(20-len(name)),sec.upper(),mrk]
        data.append(lst)
        ch=input('Do you want to Continue? :')
        if ch in 'Nn':
            break    
    f.seek(0)
    pickle.dump(data,f)
    f.close()
    print('\nData appended succesfully !!..')
    
    
def search():
     f=open("stdetails.dat",'rb')
     rec=pickle.load(f)
     roll=int(input('Enter Admission no. to search :'))
     flag=0
     for i in rec:
         if i[0]==roll:
             print('\nRequired data :')
             prnt([i],list4)
             flag=1
     if flag==0:
         print(" no. does not exist in file.")
     else:
         print('\nData searched succesfully !!..')
     if user==1:
         ch=input("Want to search more?(y/n): ")
         if ch in "Yy":
             search()
    
     f.close()
    
     
def update():#update fxn fixed
    f=open("stdetails.dat",'rb+')
    rec=pickle.load(f)
    roll=int(input('Enter Admission no. to update :'))

    r=0
    l=[]
    while r==0:
        for i in rec:
            l+=[i[0]]
        if roll in l:
            r=1
            pass
        
        else:
        
                print("\nNo such Admission no.exist")
                roll=int(input('Please! Enter a valid Roll no. to update :'))
    f.seek(0)#line added            
    res=0
    while res==0:
        ch=int(input('What do you want to update?\n1.Name\n2.Sec\n3.Marks\nEnter your choice :'))
        if ch in (1,2,3):
            for i in rec:
                if ch==1:
                    n=input('Enter updated name :')
                    n=n.capitalize()+" "*(20-len(n))
                    j=1
                    #i[1]=name.capitalize()
                elif ch==2:
                    n=input('Enter Section:')
                    j=2
                    #i[2]=sec.upper()
                elif ch==3:
                    n=int(input("Enter updated marks (0 to 100):"))
                    while True:
                        if n>=0 and n<=100:
                            break
                        n=int(input('Pleas enter Marks in percent (0 to 100):'))
                    j=3
                    #i[3]=mrk
                break
            for i in range(len(rec)):
                if rec[i][0]==roll:
                    pos=f.tell()
                    #print(rec)
                    rec[i][j]=n
            res=11
        else:
            print('Please Enter a vaild choice....')
            res=0
    f.seek(pos)
    pickle.dump(rec,f)
    f.close()
    print('\nData updated succesfully !!..')

def delete():
    f=open("stdetails.dat",'rb+')
    rec=pickle.load(f)
    roll=int(input('Enter Admission no. to Delete :'))
    flag=0
    for i in rec:
        if i[0]==roll:
            rec.remove(i)
            flag=1
    #if flag==0:
    #    print("Admission no. does not exist in file.")
    f.seek(0)
    pickle.dump(rec,f)
    f.close()
    if flag==0:
        print("Admission no. does not exist in file.")
    else:
        print('\nData deleted succesfully !!..')

def sort():
    f=open("stdetails.dat",'rb')
    rec=pickle.load(f)
    ch=int(input('On what basis do you want to search ?\n1.Name\n2.Sec\n3.Marks\nEnter your choice :'))
    if ch not in (1,2,3):
        print('\nYour choice is invalid.')
        runpy()
    ch2=int(input('\nHow do you want to sort ?\n1.Ascending\n2.Descending\nEnter your choice :'))
    if ch2 not in (1,2):
        print('\nYour choice is invalid.')
        runpy()
    for i in range(len(rec)):
        rec[i].insert(0,rec[i][ch])
    rec.sort()
    
    for i in range(len(rec)):
        rec[i].pop(0)
    if ch2==2:
        rec=rec[::-1]
    
    prnt(rec,list4)#needs better presentation...done
    ch=input("Want to sort again?(y/n): ")
    if ch in "Yy":
        sort()
def Filter():
    f=open("stdetails.dat",'rb')
    rec=pickle.load(f)
    ch=int(input('On what basis do you want to filter ?\n1.Name\n2.Sec\n3.Marks\nEnter your choice :'))
    if ch not in (1,2,3):
        print('\nYour choice is invalid.')
        runpy()
   
            
    l=[]
    if ch==1:
            name=input('Enter the name to be filtered :')
            name=name.capitalize()+" "*(20-len(name))
    if ch==2:
            sec=input('Enter the section to be filtered :')
    if ch==3:
            mrk=int(input('Enter the marks to be filtered :'))
    
    
    for i in rec:
        if ch==1:           
            if i[1]==name:
                l+=[i]
                            
        elif ch==2:      
            if i[2]==sec.upper():
              l+=[i]
                
        elif ch==3:            
            if i[3]==mrk:
                l+=[i]
    
    if len(l)==0:
        print('\nNo such records were found ....')
        
    else:    
        print('\nFiltered data is shown below ....')
        prnt(l,list4)
    if input("Want to filter again?(y/n) : ") in "yY":
        Filter()

def csvfile():
    f1=open("stdetails.dat","rb")
    f=open("csvfile.csv","w")
    stwriter=csv.writer(f)
    rec=pickle.load(f1)
    stwriter.writerow(list4)
    for i in rec:
        stwriter.writerow(i)
    print("File created successfully...")
    
def ans(given,correct):
    if given.lower()==correct:
        return 10
    return -5

def question(list2):
    #list1=pickle.load(a)
    shuffle(list2)
    score=0
    
    for i in list2:
        print("Question:")
        print(i[:-1])
        print()
        response=input("Enter your response: ")
        print("\n")
        res = ans(response,i[-1])
        score=score+res

        ans_hist.append(res == 10)
        
    return score
    

print(''' Hey There!! You are welocomed to ''')
ch=int(input('How would you like to login..\n\n1.Administrator \n2.Student \n\nEnter your choice :'))
res=0
if ch==1:
    while res==0:
        pas=input("Enter Administrator Password :")
        if pas=="cvsec5":
            while True:
                runpy()

        else:
            print('\nWrong Password !! Please recheck and try again...')          
            
            
if ch==2:
    while True:
        
        choice=input("1. Search your details\n2. GK quiz\nEnter choice:")
        if choice=="1":
            user=0
            search()
            break
        elif choice=="2":
            r=int(input("Enter your reg. no: "))
            f=open("stdetails.dat",'rb')
            rec=pickle.load(f)
            while True:
                flag=0
                mainf=0
                for i in rec:
                    if r in i:
                        flag=1
                        mainf=1
                        print("Welcome",i[1])
                        print("Each question has 10 marks and -5 for wrong\nWarm up test started...")
                if flag==0:
                    r=int(input("Data not found, enter again : "))
                #test code
                if flag==1:
                    l=['What is the capital of India?\n\na)Delhi\nb)Mumbai\nc)Ranchi\nd)Chennaia', 'What is capital of Italy?\n\na)Venice\nb)Rome\nc)Washington DC\nd)Berlinb', 'Which Country won the cricket World cup 2011?\n\na)New Zeland\nb)Engalnd\nc)India\nd)Australiac', 'How many medals did India win in Tokyo olympics 2021?\n\na)3\nb)10\nc)5\nd)7d']
                    m=question(l)
                    print("You got ",m," marks...\n")
                    print("Amalysis:")
                    count=1
                    for j in ans_hist:
                            if j:
                                print("Question", count, ": Correct")
                            else:
                                print("Question", count, ": Incorrect")
                            count += 1
                if mainf==1:
                    break
                            
                
            break
        else:
            print("Wrong choice entered!!!")
        
    sys.exit()
