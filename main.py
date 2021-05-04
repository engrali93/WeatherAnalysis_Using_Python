import pandas as pd 
import numpy as np 
import sklearn as sk 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# read the final data set
data = pd.read_csv("dataFinal.csv")

X = data.drop(['PrecipitationSumInches'], axis=1)

Y= data['PrecipitationSumInches']

Y =  Y.values.reshape(-1, 1)

day_index = 800
days = [i for i in range(Y.size)]
clf = LinearRegression()
clf.fit(X,Y)



plt.scatter(days, Y, color='g')
plt.scatter(days[day_index], Y[day_index], color='r')
plt.title('Precipitation level')
plt.xlabel('Days')
plt.ylabel('Precipitation in inches')
plt.show()

x_f = X.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent', 
                'SeaLevelPressureAvgInches', 'VisibilityAvgMiles',
                'WindAvgMPH'], axis=1)

print('Precipitation vs Selected Attributes Graph: ')

for i in range(x_f.columns.size):
    plt.subplot(3,2, i+1)
    plt.scatter(days, x_f[x_f.columns.values[i][:100]], color= 'g')
    plt.scatter(days[day_index], x_f[x_f.columns.values[i]]
                [day_index], color= 'r')
    plt.title(x_f.columns.values[i])
 
# plot the graph with a few features vs precipitation    
plt.show()    
    
