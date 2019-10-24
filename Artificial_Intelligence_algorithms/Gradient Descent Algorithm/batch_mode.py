from __future__ import print_function
import numpy
import sys
#sys.tracebacklimit = 0

def main():
    w0,w1,w2,alpha=.1,.1,.1,.1
    twodarr=[[]]
    fl=open("input.txt","r")
    num_lines = sum(1 for line in open("input.txt","r"))
    print("-------initial Parameters------\n")
    print("W0= %f \t W1= %f \t W2= %f \t Alpha= %f \n" %(w0,w1,w2,alpha))
    print("")
    count=1
    line=fl.readline()#skiped first input line
    trnsample=num_lines-1
    #print(trnsample)
    h = numpy.empty(trnsample,float)
    while count<=num_lines:
        line=fl.readline()
        inputline=line.strip()
        mylist=inputline.split(",")   #access from 2nd line
        count1=count-1
        twodarr.insert(count1,mylist)
       # print()
        count=count+1

    ''' for r in twodarr:
        for c in r:
            print(c ,end=" ")
        print()
    '''
    fl.close()
    MAXITR=10  #Max iterations
    trnstep=1
    while trnstep<=MAXITR:
        print("******* %dth Training Step(iteration) *******\n"%trnstep)
        sample=1
        while sample<= trnsample:    #Hypothesis and Weight values calculation
            print("For %dth training sample:"%sample)
            h[sample-1]=(w0*float(twodarr[sample-1][0]))+(w1*float(twodarr[sample-1][1]))+(w2*float(twodarr[sample-1][2]))
            print("h(x) is %f "%(h[sample-1]))
            if sample==trnsample: #update wi's only for last sample
                w0part,w1part,w2part=0.0,0.0,0.0 
                for j in range (1,trnsample):   # previous wi's contribution to last sample
                    w0part=w0part+(float(twodarr[j-1][3])-h[j-1])*float(twodarr[j-1][0])
                    w1part=w1part+(float(twodarr[j-1][3])-h[j-1])*float(twodarr[j-1][1])
                    w2part=w2part+(float(twodarr[j-1][3])-h[j-1])*float(twodarr[j-1][2])
                w0=w0+(alpha*((float(twodarr[sample-1][3])-h[sample-1])*float(twodarr[sample-1][0])+w0part))
                w1=w1+(alpha*((float(twodarr[sample-1][3])-h[sample-1])*float(twodarr[sample-1][1])+w1part))
                w2=w2+(alpha*((float(twodarr[sample-1][3])-h[sample-1])*float(twodarr[sample-1][2])+w2part))
                print("W0=%f W1=%f W2=%f"%(w0,w1,w2))
            sample=sample+1
            print()
        #Error Function calculation    
        errsum=0
        for i in range(1,trnsample+1,1):
            errsum=errsum+pow((float(twodarr[i-1][3])-h[i-1]),2)
        err_funct=0.5*errsum
        print("Total Error = %f\n"%(err_funct))
        if err_funct<2:
            break
        trnstep=trnstep+1
        print("----------------------------------------------------------")
    print("\n Polinomial generated for fitting the curve of form (Y=w0+w1x1+w2x2) in BATCH MODE is:\n")
    print("Y=(%f)+(%fx1)+(%fx2)"%(w0,w1,w2))


if __name__ == "__main__":
    main()