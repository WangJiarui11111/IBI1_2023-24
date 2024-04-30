# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
# Define the basic varialbes of the model
N=10000 # Population size
susceptible=N-1
infected=1
recovered=0
beta=0.3 #  Infection probability 
gamma=0.05 # Recovery probability
time_max=1000
# Create arrays for each of those variables 
susceptible_list=[susceptible]
infected_list=[infected]
recovered_list=[recovered]
# Time loop:
for t in range(time_max-1):
    # Pick susceptible individuals at random to become infected
        # Actual probability of infection
    infected_probability=beta* infected/N
    chosen_susceptibles=np.random.choice(range(2),susceptible,p=[1-infected_probability,infected_probability])

    susceptible -= sum(chosen_susceptibles)
    infected += sum(chosen_susceptibles)

    chosen_infected=np.random.choice(range(2),infected,p=[1-gamma,gamma]) 
    infected -= sum(chosen_infected)
    recovered += sum(chosen_infected)

    susceptible_list.append(susceptible)  
    infected_list.append(infected)  
    recovered_list.append(recovered) 

    susceptible = max(0, susceptible)  
    infected = max(0, infected) 
# Plot the results 
plt.figure(figsize=(6, 4),dpi=150)  
plt.plot(range(time_max),susceptible_list, label='Susceptible')  
plt.plot(range(time_max),infected_list, label='Infected')  
plt.plot(range(time_max),recovered_list, label='Recovered')  
plt.xlabel('Time')  
plt.ylabel('Number of People')  
plt.title('SIR Model')  
plt.legend()  
plt.show()
plt.clf()
