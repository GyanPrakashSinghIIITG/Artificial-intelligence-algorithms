from __future__ import print_function
import numpy
import random

    
init_prob = 1
Threshold = .60
gcount=0
dec_prob=.40
clst1 = numpy.empty(100,int)
clst2 = numpy.empty(100,int)
mylist = list(range(100))
clustcent1 = numpy.empty(50,int)
clustcent2 = numpy.empty(50,int)
totfitness = numpy.empty(100,int)
random.shuffle(mylist)

#print(*mylist, sep='\n') 
fl1= open('gps', 'w')
fl1.write("initial dataset\n")
count=0
while count < 100 :
 t=mylist[count]
 fl1.write("%d" %(t))
 fl1.write('\n')
 count = count + 1
fl1.close()
globalclustcent1=0
globalclustcent2=0

def main():
    global globalclustcent1
    global globalclustcent2
    myselection()
    print("\n--------Final cluster Centers:---------\n")
    print( globalclustcent1)
    print( globalclustcent2)

    


#fitness function intra cluster distance need to be minimized
def myselection():
    global init_prob
    global Threshold
    global gcount
    global clustcent1
    global clustcent2
    global globalclustcent1
    global globalclustcent2
    global totfitness
    global dec_prob
    # Random selection criteria
    while init_prob > Threshold :
        if gcount == 0 :
            clstc1=random.randint(1,50)
            globalclustcent1=clstc1
            clustcent1[gcount]=clstc1
            clstc2=random.randint(50,100)
            globalclustcent2=clstc2
            clustcent2[gcount]=clstc2
            calcluster(clstc1,clstc2)
        else:
            clstc1=random.randint(1,50)
            clustcent1[gcount]=clstc1
            clstc2=random.randint(1,50)
            clustcent2[gcount]=clstc2
            calcluster(clstc1,clstc2)
            if totfitness[gcount-1] > totfitness[gcount-2] : 
                t=random.random()
                if t < dec_prob :
                    globalclustcent1=clstc1            #bad movement with some probability
                    globalclustcent2=clstc2
                    dec_prob = dec_prob - .02
                else:
                    globalclustcent1=clustcent1[gcount-2]
                    globalclustcent2=clustcent2[gcount-2]
            else:
                globalclustcent1=clustcent1[gcount-1]
                globalclustcent2=clustcent2[gcount-1]
        init_prob = init_prob - .05
 
     
def calcfitness(c1,c2,lc1,lc2):
    global gcount
    global totfitness
    sum1=0
    sum2=0
    m1=0
    m2=0
    while m1 < lc1 :
        sum1 = sum1 + abs(clst1[m1] - c1)
        m1 = m1 + 1

    while m2 < lc2 :
        sum2 = sum2 + abs(clst2[m2] - c2)
        m2 = m2 + 1
    totfitness[gcount]=sum1+sum2
    print("C1 \t C2 \t Totalfitness")
    print(" %d \t %d \t %d \t " %(c1,c2,totfitness[gcount]))
    gcount = gcount + 1
    


def calcluster(c1,c2):
    count1=0
    count2=0
    lcount=0

    while lcount < 100:
        t1 = abs(mylist[lcount] - c1)
        t2 = abs(mylist[lcount] - c2)
        if t2 > t1:
            clst1[count1] = mylist[lcount]
            count1 =+ 1
        elif t1 > t2 :
            clst2[count2]=mylist[lcount]
            count2 =+ 1
        lcount = lcount + 1
    calcfitness(c1,c2,count1,count2)

if __name__ == "__main__":
    main()
