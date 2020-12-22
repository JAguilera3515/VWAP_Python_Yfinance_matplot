import pandas as pd
import yfinance as Stock
import matplotlib.pylab as plt
import numpy.matlib as np
from datetime import datetime

stock1 = input('Enter first Stock Letters: ')
stock1 = stock1.upper()
stock2 = input('Enter second Stock Letters: ')
stock2 = stock2.upper()

#--This is to get the current date added everytime
CurrentDay = datetime.today().strftime('%Y-%m-%d')
CurrentDay = list(CurrentDay)
tmpC = CurrentDay[9]
tmp = int(tmpC) + 1
if tmp > 9:
    CurrentDay[9] = '0'
    tmp = int(CurrentDay[8]) + 1
    CurrentDay[8] = str(tmp)
else:
    CurrentDay[9] = str(tmp)
CurrentDay = "".join(CurrentDay)
#-----------

MS = Stock.Ticker(stock1)
MST = MS.history(period='1d', start='2020-06-06', end= CurrentDay)#'2020-08-06')
APL = Stock.Ticker(stock2)
Apple = APL.history(period='1d', start='2020-06-06', end= CurrentDay)#'2020-08-06')

ARRAYAP = {}
CloseA = []

ArrayV = {}
Close = []
for i in range(len(MST['Close'])):

    CloseA.append(Apple['Close'][i])
    Price = (Apple['High'][i] + Apple['Low'][i] + Apple['Close'][i])/3
    
    VWAP = (np.cumsum(Price * Apple['Volume'][i])) / np.cumsum(Apple['Volume'][i])
    ARRAYAP[Apple.index[i]] = VWAP
    Price = 0
    VWAP = 0
    #-----------------------------------------------------
    #Eq for VWAP 
    #Price = (High + Low + Close)/3 
    Close.append(MST['Close'][i])
    Price = (MST['High'][i] + MST['Low'][i] + MST['Close'][i])/3
    
    VWAP = (np.cumsum(Price * MST['Volume'][i])) / np.cumsum(MST['Volume'][i])
    ArrayV[MST.index[i]] = VWAP
keys = ArrayV.keys()
values = ArrayV.values()


plot1 = plt.figure(1)
plt.plot(keys,values,label="VWAP")
plt.plot(keys,Close,label="Closing Price")
plt.title(label=stock1,loc='center')
plt.legend(loc="upper left")
plt.xlabel('Dates')
plt.ylabel('Price')
plt.xticks(rotation=20)


keys2 = ARRAYAP.keys()
values2 = ARRAYAP.values()

plot2 = plt.figure(2)
plt.plot(keys2,values2,label="VWAP")
plt.plot(keys2,CloseA,label="Closing Price")
plt.title(label=stock2,loc='center')
plt.legend(loc="upper left")
plt.xlabel('Dates')
plt.ylabel('Price')
plt.xticks(rotation=20)

plt.show()