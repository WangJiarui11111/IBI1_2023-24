# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
# Define the basic varialbes of the model
N=10000 # Population size
beta=0.3 #  Infection probability 
gamma=0.05 # Recovery probability
time_max=1000
vaccination_percentages = [0.1, 0.2, 0.3, 0.4, 0.5,0.6,0.7,0.8,0.9,1.0]
infected_lists=[] 
recovered_list=[]
# Percentage loop
for vaccination_percentage in vaccination_percentages:  
    # Adjust the initial susceptible and vaccinated population  
    susceptible = N - int(vaccination_percentage * N)  
    vaccinated = int(vaccination_percentage * N)  
    infected = 1  if susceptible>0 else 0
    recovered = 0
    # Time loop:
    infected_list=[infected]
    for t in range(time_max-1):
    # Pick susceptible individuals at random to become infected
        # Actual probability of infection
        infected_probability=beta* infected/(N-vaccinated) if susceptible>0 else 0
        new_infections=np.random.choice(range(2), size=susceptible, p=[1-infected_probability, infected_probability]).sum()
        susceptible -= new_infections
        infected+= new_infections
        recovered_probability=gamma
        new_recoveries=np.random.choice(range(2),size=infected,p=[1-gamma,gamma]).sum()
        infected-= new_recoveries
        recovered+= new_recoveries
        recovered_list.append(recovered)
        infected_list.append(infected)
    infected_lists.append(infected_list)
# Plot the results    
colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_percentages)))  # Use different colors for each line  
plt.figure(figsize=(6, 4),dpi=150)
for i,  infected_list in enumerate(infected_lists):  
    plt.plot(range(time_max), infected_list, color=colors[i], label=f' {vaccination_percentages[i]*100}%')   
plt.xlabel('Time')  
plt.ylabel('Number of People')  
plt.title('SIR Model with Different Vaccination Rates')  
plt.legend()  
plt.show()
plt.clf()
