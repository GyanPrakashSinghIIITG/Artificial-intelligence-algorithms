import numpy
import random
import shutil

a = numpy.empty(150,float)
b = numpy.empty(150,float)

def main():
    count=0
    flname= open('IRIS.csv', 'r')
    shutil.copy2('/home/gyan/Desktop/Evaluation/ga/IRIS.csv','/home/gyan/Desktop/Evaluation/ga/myoutput.txt')
    line = flname.readline()
    while line:
       ## print(line)
        t1=calcfitness(line,count) 
        #print( " Initfitval: %f" %t1 )
        line = flname.readline()
        count +=1
    stor1=myselection()
    m1=0
    mysum=0
    print("sr.no \t initialfit \t finalfit")
    for m1 in range (0,150,1):
        print(" %d \t %f \t %f" %(m1,a[m1],b[m1]))
        mysum=mysum+b[m1]
    print("initial total fitness is %f\n"%stor1)
    print("Final total fitness is %f\n"%mysum)
    flname.close()

def calcfitness(line,count):
    inputline=line
    #print(inputline)
    a1=float(inputline.split(',')[0])
    a2=float(inputline.split(',')[1])
    a3=float(inputline.split(',')[2])
    a4=float(inputline.split(',')[3])
    a[count]= float(a1+a2+a3+a4)
    b[count]= a[count]
    return(a[count])


def myselection():
    # Roulette-wheel selection criteria
    # pi= fi/summation(fi) for i=1 to i=n
    totalfit=0
    temp1 = 0
    while temp1 < 150:
        totalfit = totalfit + a[temp1]
        temp1 += 1
    #print("initial total fitness is  %f" % totalfit )
    # for 300 iterations
    itr = 0
    for itr in range (0,300,1):
        rnum1=random.randint(1,int(totalfit))
        rnum2=random.randint(1,int(totalfit))
        #print("rand1 is %d" % rnum1)
        #print("rand2 is %d" % rnum2)
        sum1=0
        pind1=0
        temp2=0
        for temp2 in range(150):
            if sum1 > rnum1:
                break
            else: 
                sum1=sum1+a[pind1]
                pind1 +=1
                continue 
        #print("pind1 is %d" % pind1)     
        sum2=0
        pind2=0
        temp3=0
        for temp3 in range(150):
            if sum2 > rnum2:
                break
            else: 
                sum2=sum2+a[pind2]
                pind2 +=1
                continue  
        #print("pind2 is %d" % pind2) 
        Mycrossover(pind1,pind2) 
    return totalfit

     
def Mycrossover(pindex1,pindex2):
    #print("inside crossover")
    #my cross over point is after 2 columns of rows of dataset
    filetemp=open('myoutput.txt','r')
    lines=filetemp.readlines()
    a1= lines[pindex1-1] #line starts from zero
    a2= lines[pindex2-1]
    x1=float(a1.split(',')[0])
    x2=float(a1.split(',')[1])
    x3=float(a1.split(',')[2])
    x4=float(a1.split(',')[3])
    x5=float(a2.split(',')[0])
    x6=float(a2.split(',')[1])
    x7=float(a2.split(',')[2])
    x8=float(a2.split(',')[3])
    b[pindex2-1]=x3+x4+x5+x6
    b[pindex1-1]=x1+x2+x7+x8   
    filetemp.close()

if __name__ == "__main__":
    main()
