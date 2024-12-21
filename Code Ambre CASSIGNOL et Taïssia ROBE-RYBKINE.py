#open files (input + output)
fIN  = open('data_real.csv', 'r')
fOUT = open('separateFecal.csv', 'w')


# skip first line
line = fIN.readline()

# browse all other lines
while line != '':
    # get next line
    line = fIN.readline()
    # if we encountered the last line
    if line == '':
        # exit the loop
        break
    #split
    valueList=line.split(';')
    
    #convert one column into a variable sample
    sample=str(valueList[2])
    #keep only data for fecal
    if sample=='fecal':
        line2=';'.join(valueList)
        fOUT.write(line2)
        

fIN.close()
fOUT.close()


#represent graph
import matplotlib.pyplot as plt
import math


figure, axes = plt.subplots()

axes.set_title('live bacteria in fecal')
axes.set_xlabel('washout day')
axes.set_ylabel('log10(live bacteria/wet g)')



graph = 'fecal'

for mouse in range(17, 33):
    xVal = []
    yVal = []

    # fill data from file
    fIN = open('separateFecal.csv', 'r')
    line = fIN.readline()

    while line != '':
        line = fIN.readline()
        if line == '':
            break 
        # split line
        valueList = line.split(';')
        # retrieve data
        sampleType = valueList[2]
        mouseID    = int(valueList[4].replace('ABX', ''))
        treatment  = valueList[5]    
        day        = int(valueList[7])
        bacteria   = math.log(float(valueList[8]))/math.log(10)


        # filter lines
        if mouseID == mouse and sampleType == graph :
            xVal.append(day)
            yVal.append(bacteria)
            

    fIN.close()

    axes.plot(xVal, yVal)





figure.savefig('Fecal graph.png', dpi=300)






#open files (input + output)
fIN  = open('data_real.csv', 'r')
fOUT = open('separateCecal.csv', 'w')


# skip first line
line = fIN.readline()

# browse all other lines
while line != '':
    # get next line
    line = fIN.readline()
    # if we encountered the last line
    if line == '':
        # exit the loop
        break
    #split
    valueList=line.split(';')
    
    #convert one column into a variable
    sample=str(valueList[2])
    #keep only mice for cecal
    if sample=='cecal':
        line3=';'.join(valueList)
        fOUT.write(line3)
        

fIN.close()
fOUT.close()


#represent graph
import matplotlib.pyplot as plt
import math


xVal = []
yVal = []
xVal2= []
yVal2= []



# fill data from file
fIN = open('separateCecal.csv', 'r')
line = fIN.readline()

count = 0
while line != '':
    line = fIN.readline()
    if line == '':
        break 
    #split
    valueList = line.split(';')
    #retrieve data
    treatment = valueList[5]
    bacteria = math.log(float(valueList[8]))/math.log(10)
    #if treatment used is ABX, variable equals 1. All the data with treated mice will be represented with an abscissa of 1
    
    if treatment == 'ABX':
        treatment = 1
        xVal.append(treatment)
        yVal.append (bacteria)
    
    #else, variable equals 2. All the data with mice without ABX will be reresented with an abscissa of 2
        
    else:
        treatment = 2
        xVal2.append(treatment)
        yVal2.append (bacteria)
        
        
    count = count+1       

fIN.close()


figure, axes = plt.subplots()

axes.set_title('live bacteria in Cecal')
axes.set_xlabel('X values')
axes.set_ylabel('Y values')

axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Cecal graph.png', dpi=300)


figure, axes = plt.subplots()

axes.set_title('live bacteria in Cecal')
axes.set_ylabel('Y values')


axes.violinplot([yVal, yVal2])



plt.xlabel("treatment used")
plt.ylabel("log10(live bacteria/wet g)")
#only ABX will be visible. Try to put a legend in the graph but fail because of a lack of color
plt.legend(['placebo'],fontsize='medium')
plt.legend(['ABX'],fontsize='small')

figure.savefig('Cecal graph.png', dpi=300)






#open files (input + output)
fIN  = open('data_real.csv', 'r')
fOUT = open('separateIleal.csv', 'w')


# skip first line
line = fIN.readline()

# browse all other lines
while line != '':
    # get next line
    line = fIN.readline()
    # if we encountered the last line
    if line == '':
        # exit the loop
        break
    #split
    valueList=line.split(';')
    
    #convert one column into a variable sample
    sample=str(valueList[2])
    #keep only data for cecal
    if sample=='ileal':
        line3=';'.join(valueList)
        fOUT.write(line3)
        

fIN.close()
fOUT.close()


#represent graph


xVal = []
yVal = []
xVal2= []
yVal2= []


# fill data from file
fIN = open('separationIleal.csv', 'r')
line = fIN.readline()

count = 0
#browse lines
while line != '':
    line = fIN.readline()
    #if blank
    if line == '':
        break 
    #split
    valueList = line.split(';')
    #retrieve data 
    treatment = valueList[5]
    #calculate log10 of live bacteria in ileal
    bacteria = math.log(float(valueList[8]))/math.log(10)
    #if treatment used is ABX, variable equals 1. Like so, all the data with treated mice will be represented in an abscissa of 1
    
    if treatment == 'ABX':
        treatment = 1
        xVal.append(treatment)
        yVal.append (bacteria)
    #else, variable equals 2. All the data with mice without ABX will be represented with an abscissa of 2
        
    else:
        treatment = 2
        xVal2.append(treatment)
        yVal2.append (bacteria)
        
        
    count = count+1       

fIN.close()


figure, axes = plt.subplots()

axes.set_title('Ileal live bacteria')
axes.set_xlabel('X values')
axes.set_ylabel('Y values')

axes.plot(xVal, yVal)
axes.plot(xVal2, yVal2)

figure.savefig('Ileal graph.png', dpi=300)


figure, axes = plt.subplots()

axes.set_title('Ileal live bacteria')
axes.set_ylabel('Y values')


axes.violinplot([yVal, yVal2])


plt.xlabel("treatment")
plt.ylabel("log10(live bacteria/wet g)")
#only ABX will be visible in the graph. Try to put a legend in the graph but fail
plt.legend(['placebo'],fontsize='medium')
plt.legend(['ABX'],fontsize='small')

figure.savefig('Ileal graph.png', dpi=300)


   
