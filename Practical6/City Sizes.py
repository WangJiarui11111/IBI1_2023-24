uk_cities=[0.56,0.62,0.04,9.7] #Make a uk_cities list
china_cities=[0.58,8.4,22.2,29.9] #Make a china_cities list
uk_cities.sort() #Sort the UK list
china_cities.sort() #Sort the China list
print(uk_cities) #print the uk_cities list
print(china_cities) #print the china_cities list
cities=uk_cities+china_cities
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun'] #Set the font
cities=["Edinburgh", "Glasgow", "Stirling", "London"] #input x_data
population=[0.04,0.56,0.62,9.7] #input y_data
std_err = [1, 1, 1, 1, 1]
width = 30 #The maximum value of y-axis
plt.figure()
plt.bar(x=cities, height=population, width=0.7, color='cadetblue',ec='black') #set the style of the bar graph
plt.xlabel(cities)
plt.ylabel("population")
plt.title("Cities in the UK in 2024 are of varying populations") #Make a title
plt.show() #show the graph
plt.clf() 
plt.rcParams['font.sans-serif']=['SimSun'] #Set the font
cities=["Haining", "Hangzhou", "Shanghai", "Beijing"] #input x_data
population=[0.58,8.4,22.2,29.9] #input y_data
std_err = [1, 1, 1, 1, 1]
width = 30 #The maximum value of y-axis
plt.bar(x=cities, height=population, width=0.7, color='cadetblue',ec='black') #set the style of the bar graph
plt.xlabel(cities)
plt.ylabel("population")
plt.title("Cities in the China in 2024 are of varying populations") #Make a title
plt.show() #show the graph
plt.clf()