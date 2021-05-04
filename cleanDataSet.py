#Cleaning the data

#Import the libraries
import pandas as pd 
import numpy as np 

# read data in pandas
data = pd.read_csv("data_weather.csv")


# delete unwanted columns in the data set
data = data.drop(['Events', 'Date', 'SeaLevelPressureHighInches', 'SeaLevelPressureLowInches']
                 , axis = 1)

data = data.replace('T', 0.0)
data = data.replace('-', 0.0)

data.to_csv('dataFinal.csv')
