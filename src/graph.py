import csv
import matplotlib.pyplot as plt
import numpy as np


yearList = []
providerList = []
cityList = []
AGFSList = []
condenseProviderList = []


def condense():
    compare = providerList[0]
    condenseProviderList.append(compare)
    for provider in providerList:
        if provider != compare:
            condenseProviderList.append(provider)
            compare = provider
    

def averageAGFS():
    average = []
    for provider in condenseProviderList:
        i = 0
        temp = []
        for p in providerList:
            if p == provider:
                temp.append(AGFSList[i])
            
            i += 1

        average.append(sum(temp) / len(temp))
    
    return(average)


def plotAverageAGFS(averages):
    # fig = plt.figure()
    # plt.bar(condenseProviderList, averages)
    # plt.title('Healthcare Providers Average AGFS')
    # plt.ylabel('Average AGFS')
    # plt.xlabel('Healthcare Provider')
    # plt.yticks(np.arange(0, 101, 10))
    # plt.show()
    fig, ax = plt.subplots(figsize =(15, 10))
    ax.barh(condenseProviderList, averages)

    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')   
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(b = True, color ='black', linestyle ='-.', linewidth = 0.5, alpha = 0.2)
    ax.invert_yaxis()
    
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
    
    ax.set_title('Healthcare Providers Average AGFS', loc ='center', )
    ax.set_xlabel('Average AGFS')
    ax.set_ylabel('Healthcare Providers')
    plt.show()


# may need to change below to work for your file path (../data/hedis.csv)
with open('data/hedis.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in reader:
        year = row[0]
        provider = row[1].split("-")[0]
        city = row[1].split("-")[1]
        AGFS = float(row[2].split("%")[0])
        
        yearList.append(year)
        providerList.append(provider)
        cityList.append(city)
        AGFSList.append(AGFS)
        
condense()
averages = averageAGFS()
plotAverageAGFS(averages)