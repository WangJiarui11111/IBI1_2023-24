#Calculate the number of days required to exceed 0.9 density.
i=0
j=0.05
#The density is 90 at the beginning.
while j<=0.9:
    i=i+1
#Increase in days.
    j=2*j
#The cell line doubles in density every 24 hrs.
    print(str(i)+" "+str(j))
#The density reaches 80% at the end of the forth day, and 90% and exceeds during the fifth day.
#So I can only leave the laboratory for a maximum of 4 days.


