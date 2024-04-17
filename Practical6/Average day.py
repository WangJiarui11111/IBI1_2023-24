#Creating a dictionary
my_dict = {'Sleeping':'8', 'Classes':'6', 'Studying':'8', 'TV':'2', 'Music':'1'}
#Accessing dictionary values
print(my_dict['Sleeping']) #output: value1
print(my_dict['Classes']) #output: value2
print(my_dict['Studying']) #output: value3
print(my_dict['TV']) #output: value4
print(my_dict['Music']) #output: value5
#Adding new key-value pairs
my_dict['Other']='3.5'
print(my_dict['Other']) #output: value6
print(my_dict) #output the dictionary
import matplotlib.pyplot as plt
#Labels and values
activity_labels=["Sleeping","Classes","Studying","TV","Music","Other"]
time_hours=[8,6,3.5,2,1,3.5]
Sleeping_and_else=[0,0,0,0,0,0]
plt.figure()
plt.pie(time_hours, labels=activity_labels, startangle=90, explode= Sleeping_and_else, autopct='%.1f%%')
plt.title('The average day of a university student') #Show the title
plt.show() #show the graph
plt.clf()