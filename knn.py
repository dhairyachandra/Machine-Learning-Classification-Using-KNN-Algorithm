import math
    
File = 'dataset.txt'

fin = open(File,'r')

raw_data = fin.read()

dataset = raw_data.split()

datalist = []

for rec in dataset:
    reclist = rec.split(',')

    if reclist[4] == 'Iris-setosa':
        reclist[4] = '1'
    elif reclist[4] == 'Iris-versicolor':
        reclist[4] = '2'
    else:
        reclist[4] = '3'

    datalist.append(reclist)

train = datalist[:40] + datalist[50:90] + datalist[100:140]
test = datalist[40:50] + datalist[90:100] + datalist[140:149]

accuracy = 0

for testcase in test:
        
    sl = float(testcase[0])
    sw = float(testcase[1])
    pl = float(testcase[2])
    pw = float(testcase[3])

    dist = []

    REC = []


    for rec in train:
        a = (float(rec[0])-sl)**2
        b = (float(rec[1])-sw)**2
        c = (float(rec[2])-pl)**2
        d = (float(rec[3])-pw)**2
            
        REC.append(rec + [str(math.sqrt(a+b+c+d))])
           
           
    REC = sorted (REC,key = lambda l:l[5])
            
        
    k = 3

    p1 = 0
    p2 = 0
    p3 = 0

    for i in range (0,k):
        if REC[i][4]=='1':
            p1+=1
        elif REC[i][4]=='2':
            p2+=1
        else:
            p3+=1

    if(p1>p2):
        if p1>p3:
            code = 1
        else:
            code = 3
    else:
        if p2>p3:
            code = 2
        else:
            code = 3

    if testcase[4]==str(code):
        accuracy += 1

        
accuracy = accuracy / float(len(test))
    
accuracy = accuracy * 100

print '\nThis Time Accuracy Is : ' + str(accuracy) + '%'
    


