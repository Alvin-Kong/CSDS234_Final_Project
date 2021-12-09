import csv
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

filepath = 'data/hedis.csv'

yearList = []
providerList = []
cityList = []
AQFSList = []
condenseProviderList = []
condenseCityList = []


def getData():
    # may need to change below to work for your file path (../data/hedis.csv)
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in reader:
            year = row[0]
            provider = row[1].split("-")[0]
            city = row[1].split("-")[1]
            AGFS = float(row[2].split("%")[0])
            
            yearList.append(year)
            providerList.append(provider)
            cityList.append(city)
            AQFSList.append(AGFS)


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
    

def providerAverageAQFS():
    average = []
    for provider in condenseProviderList:
        i = 0
        temp = []
        for p in providerList:
            if p == provider:
                temp.append(AQFSList[i])
            
            i += 1

        average.append(sum(temp) / len(temp))
    
    return(average)


def cityAverageAQFS():
    average = []
    for city in condenseCityList:
        i = 0
        temp = []
        for c in cityList:
            if c == city:
                temp.append(AQFSList[i])

            i += 1

        average.append(sum(temp) / len(temp))

    return(average)


def yearAverageAQFS():
    yearlyAverages = []
    for year in ['2016', '2017', '2018', '2019']:
        average = []
        for provider in condenseProviderList:
            i = 0
            temp = []
            for p in providerList:
                if p == provider and yearList[i] == year:
                    temp.append(AQFSList[i])
                
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


def plotProviderAverageAQFS(average):
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
    
    ax.set_title('Healthcare Providers Average AQFS', loc ='center', )
    ax.set_xlabel('Average AQFS (%)')
    ax.set_ylabel('Healthcare Providers')
    plt.show()


def plotCityAverageAQFS(average):
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
    
    ax.set_title('Citys Average AQFS', loc ='center', )
    ax.set_xlabel('Average AQFS (%)')
    ax.set_ylabel('City')
    plt.show()


def plotYearlyAverageAQFS(yearlyAverages):
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
            ax.set_title('Healthcare Providers Average AQFS in 2016', loc ='center', )
        elif index == 1:
            ax.set_title('Healthcare Providers Average AQFS in 2017', loc ='center', )
        elif index == 2:
            ax.set_title('Healthcare Providers Average AQFS in 2018', loc ='center', )
        else:
            ax.set_title('Healthcare Providers Average AQFS in 2019', loc ='center', )
        
        ax.set_xlabel('Average AQFS (%)')
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
    
    ax.set_title('Healthcare Providers Average AQFS Difference From 2016 to 2019', loc ='center', )
    ax.set_xlabel('Average AQFS Difference (%)')
    ax.set_ylabel('Healthcare Provider')
    plt.show()


def plotRegression(regressions):
    index = 0
    for r in regressions:
        plt.plot(['1', '2', '3'], r, label=condenseProviderList[index])
        index += 1

    plt.title('AQFS Regression Between 2016 and 2019')
    plt.ylabel('AQFS Change (%)')
    plt.xlabel('Year')
    plt.legend(loc='lower right', ncol=7)
    plt.show()


def plotAQFSOverTime(yearAverage):
    index = 0
    for provider in condenseProviderList:
        AGFS = []
        AGFS.append(yearAverage[0][index])
        AGFS.append(yearAverage[1][index])
        AGFS.append(yearAverage[2][index])
        AGFS.append(yearAverage[3][index])
        plt.plot(['2016', '2017', '2018', '2019'], AGFS, label=provider)
        index += 1
    
    plt.title('AQFS of Healthcare Providers Between 2016 and 2019')
    plt.ylabel('AQFS (%)')
    plt.xlabel('Year')
    plt.legend(loc='lower right', ncol=7)
    plt.show()


def runProviderAverage():
    providerAverage = providerAverageAQFS()
    plotProviderAverageAQFS(providerAverage)


def runCityAverage():
    cityAverage = cityAverageAQFS()
    plotCityAverageAQFS(cityAverage)


def runYearAverage():
    yearAverage = yearAverageAQFS()
    plotYearlyAverageAQFS(yearAverage)


def runAverageDif():
    yearAverage = yearAverageAQFS()
    averageDif = timeComparison(yearAverage[0], yearAverage[3])
    plotTimeComparison(averageDif)


def runRecommendations():
    providerAverage = providerAverageAQFS()
    cityAverage = cityAverageAQFS()
    providerRec = recommendProvider(providerAverage)
    cityRec = recommendCity(cityAverage)
    print()
    print("Recommendations:")
    print("Healthcare Provider:", providerRec[0], "with", providerRec[1], "% AQFS")
    print("Region:", cityRec[0], "with", cityRec[1], "% AGFS")


def runRegression():
    yearAverage = yearAverageAQFS()
    regressions = timeRegression(yearAverage[0], yearAverage[1], yearAverage[2], yearAverage[3])
    plotRegression(regressions)


def runPlotAQFS():
    yearAverage = yearAverageAQFS()
    plotAQFSOverTime(yearAverage)


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
    runPlotAQFS()