import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change the working directory to where the dalys-rate-from-all-causes.csv file is stored.
os.chdir("C:\\Users\\wangj\\Desktop\\data")
#Using pandas library to read the content of the .csv file into a dataframe object and name it as dalys_data.
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
#Showing the fourth column from every 10th row, stating from the first row to the first 100 rows(inclusive).
print(dalys_data.iloc[0:101:10,3])
#Using a Boolean to show DALYs for all rows corresponding to Afghanistan.
#"Afghanistan" in "Entity" is true, others are false.
Afghanistan=dalys_data["Entity"]=="Afghanistan"
print(dalys_data.loc[Afghanistan,"DALYs"])
#Compute the mean DALYs in China.
China=dalys_data["Entity"]=="China"
China_dalys=dalys_data.loc[China,"DALYs"]
mean_china_dalys=np.mean(China_dalys)
print(mean_china_dalys)
#Select the DALYs in China in 2019 from the file.
China=dalys_data["Entity"]=="China"
Year=dalys_data["Year"]=="2019"
dalys_in_2019=dalys_data.loc[(dalys_data["Entity"]=="China")&(dalys_data["Year"]==2019), "DALYs"].values
print(dalys_in_2019)
#Compare the DALYs in China in 2019 with the mean.
if mean_china_dalys < dalys_in_2019:
    print("The DALYs in China in 2019 was greater than the mean")
else:
     print("The DALYs in China in 2019 was less than the mean")
#Select China years data.
china_data_year=dalys_data.loc[China,"Year"]
#Select China DALYs data.
china_data_dalys=dalys_data.loc[China,"DALYs"]
#Create a plot showing the DALYs over time in China.
plt.plot(china_data_year, china_data_dalys, 'b+')
plt.title("The DALYs over time in China") #Show the title
plt.xlabel("Year")
plt.xticks(china_data_year, rotation=90)
plt.ylabel("DALYs")
plt.show()
plt.clf()
#Solving the question I have asked in the other file.
#Select all the DALYs data in 2019.
dalys_in_2019=dalys_data[dalys_data["Year"]==2019]
is_low_dalys=dalys_in_2019["DALYs"]<18000
low_dalys_places=dalys_data.loc[dalys_in_2019.index[is_low_dalys],["Entity","DALYs"]]
print(low_dalys_places)