import csv
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


yearList = []
providerList = []
cityList = []
AGFSList = []
condenseProviderList = []
condenseCityList = []


def getData():
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


def condenseProviders():
    compare = providerList[0]
    condenseProviderList.append(compare)
    for provider in providerList:
        if provider != compare:
            condenseProviderList.append(provider)
            compare = provider


def condenseCities():
    compare = cityList[0]
    condenseCityList.append(compare)
    for city in cityList:
        if city != compare:
            condenseCityList.append(city)
            compare = city
    

def providerAverageAGFS():
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


def cityAverageAGFS():
    average = []
    for city in condenseCityList:
        i = 0
        temp = []
        for c in cityList:
            if c == city:
                temp.append(AGFSList[i])

            i += 1

        average.append(sum(temp) / len(temp))

    return(average)


def yearAverageAGFS():
    yearlyAverages = []
    for year in ['2016', '2017', '2018', '2019']:
        average = []
        for provider in condenseProviderList:
            i = 0
            temp = []
            for p in providerList:
                if p == provider and yearList[i] == year:
                    temp.append(AGFSList[i])
                
                i += 1

            average.append(sum(temp) / len(temp))

        yearlyAverages.append(average)
    
    return(yearlyAverages)


def recommendProvider(averages):
    maxIndex = 0
    max = averages[0]
    index = 0
    for a in averages:
        if a > max:
            max = a
            maxIndex = index

        index += 1

    return condenseProviderList[maxIndex], max


def recommendCity(averages):
    maxIndex = 0
    max = averages[0]
    index = 0
    for a in averages:
        if a > max:
            max = a
            maxIndex = index

        index += 1

    return condenseCityList[maxIndex], max


def timeComparison(initialAverage, finalAverage):
    averageDif = []
    index = 0
    for initial in initialAverage:
        dif = finalAverage[index] - initial
        averageDif.append(dif)
        index += 1

    return averageDif


def timeRegression(a0, a1, a2, a3):
    regression = []
    index = 0
    for provider in condenseProviderList:
        diffs = []
        dif1 = a1[index] - a0[index]
        dif2 = a2[index] - a1[index]
        dif3 = a3[index] - a2[index]
        diffs.append(dif1)
        diffs.append(dif2)
        diffs.append(dif3)
        regression.append(diffs)
        index += 1
    
    return regression


def plotProviderAverageAGFS(average):
    fig, ax = plt.subplots(figsize =(15, 10))
    ax.barh(condenseProviderList, average)

    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')   
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(b = True, color ='black', linestyle ='-.', linewidth = 0.5, alpha = 0.3)
    ax.invert_yaxis()
    
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
    
    ax.set_title('Healthcare Providers Average AGFS', loc ='center', )
    ax.set_xlabel('Average AGFS (%)')
    ax.set_ylabel('Healthcare Providers')
    plt.show()


def plotCityAverageAGFS(average):
    fig, ax = plt.subplots(figsize =(13, 10))
    ax.barh(condenseCityList, average)

    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')   
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(b = True, color ='black', linestyle ='-.', linewidth = 0.5, alpha = 0.3)
    ax.invert_yaxis()
    
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
    
    ax.set_title('Citys Average AGFS', loc ='center', )
    ax.set_xlabel('Average AGFS (%)')
    ax.set_ylabel('City')
    plt.show()


def plotYearlyAverageAGFS(yearlyAverages):
    index = 0
    for average in yearlyAverages:
        fig, ax = plt.subplots(figsize =(15, 10))
        ax.barh(condenseProviderList, average)

        for s in ['top', 'bottom', 'left', 'right']:
            ax.spines[s].set_visible(False)
        
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')   
        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)
        ax.grid(b = True, color ='black', linestyle ='-.', linewidth = 0.5, alpha = 0.3)
        ax.invert_yaxis()
        
        for i in ax.patches:
            plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
        
        if index == 0:
            ax.set_title('Healthcare Providers Average AGFS in 2016', loc ='center', )
        elif index == 1:
            ax.set_title('Healthcare Providers Average AGFS in 2017', loc ='center', )
        elif index == 2:
            ax.set_title('Healthcare Providers Average AGFS in 2018', loc ='center', )
        else:
            ax.set_title('Healthcare Providers Average AGFS in 2019', loc ='center', )
        
        ax.set_xlabel('Average AGFS (%)')
        ax.set_ylabel('Healthcare Providers')
        plt.show()
        index += 1


def plotTimeComparison(averageDif):
    fig, ax = plt.subplots(figsize =(13, 10))
    ax.barh(condenseProviderList, averageDif)

    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')   
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(b = True, color ='black', linestyle ='-.', linewidth = 0.5, alpha = 0.3)
    ax.invert_yaxis()
    
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')
    
    ax.set_title('Citys Average AGFS', loc ='center', )
    ax.set_xlabel('Average AGFS (%)')
    ax.set_ylabel('City')
    plt.show()


def plotRegression(regressions):
    index = 0
    for r in regressions:
        plt.plot(r, label=condenseProviderList[index])
        index += 1

    plt.title('AGFS Regression Between 2016 and 2019')
    plt.ylabel('AGFS Change (%)')
    plt.xlabel('Year')
    plt.legend(loc='upper right')
    plt.show()


def plotAGFSOverTime(yearAverage):
    index = 0
    for provider in condenseProviderList:
        AGFS = []
        AGFS.append(yearAverage[0][index])
        AGFS.append(yearAverage[1][index])
        AGFS.append(yearAverage[2][index])
        AGFS.append(yearAverage[3][index])
        plt.plot(['2016', '2017', '2018', '2019'], AGFS, label=provider)
        index += 1
    
    plt.title('AGFS of Healthcare Providers Between 2016 and 2019')
    plt.ylabel('AGFS (%)')
    plt.xlabel('Year')
    plt.legend(loc='upper right')
    plt.show()


def runProviderAverage():
    providerAverage = providerAverageAGFS()
    plotProviderAverageAGFS(providerAverage)


def runCityAverage():
    cityAverage = cityAverageAGFS()
    plotCityAverageAGFS(cityAverage)


def runYearAverage():
    yearAverage = yearAverageAGFS()
    plotYearlyAverageAGFS(yearAverage)


def runAverageDif():
    yearAverage = yearAverageAGFS()
    averageDif = timeComparison(yearAverage[0], yearAverage[3])
    plotTimeComparison(averageDif)


def runRecommendations():
    providerAverage = providerAverageAGFS()
    cityAverage = cityAverageAGFS()
    providerRec = recommendProvider(providerAverage)
    cityRec = recommendCity(cityAverage)
    print(providerRec[0], "with", providerRec[1], "% AGFS")
    print(cityRec[0], "with", cityRec[1], "% AGFS")


def runRegression():
    yearAverage = yearAverageAGFS()
    regressions = timeRegression(yearAverage[0], yearAverage[1], yearAverage[2], yearAverage[3])
    plotRegression(regressions)


def runPlotAGFS():
    yearAverage = yearAverageAGFS()
    plotAGFSOverTime(yearAverage)


def initialize():
    getData()
    condenseProviders()
    condenseCities()



if __name__ == "__main__":
    initialize()
    runProviderAverage()
    runCityAverage()
    runYearAverage()
    runAverageDif()
    runRecommendations()
    runRegression()
    runPlotAGFS()