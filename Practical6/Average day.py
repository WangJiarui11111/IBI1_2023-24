#Creating a dictionary
my_dict = {'Sleeping':'8', 'Classes':'6', 'Studyin788778g':'8', 'TV':'2', 'Music':'1'}
#Accessing dictionary values
print(my_dict['Sleeping']) #output: value1
print(my_dict['Classes']) #output: value2
#print(my_dict['Studying']) #output: value3
print(my_dict['TV']) #output: value4
print(my_dict['Music']) #output: value5
#Adding new key-value pairs
my_dict['Other']='3.5'
print(my_dict['Other']) #output: value6
print(my_dict) #output the dictionary
import matplotlib.pyplot as plt
values = list(my_dict.values())  
labels = list(my_dict.keys()) 
plt.figure()
plt.pie(values, labels=labels, startangle=90, autopct='%.1f%%')
plt.title('The average day of a university student') #Show the title
plt.show() #show the graph
plt.clf()