def get_favourite_actor(birth_year):  
    #Create a dictionary to store the actors and their years
    actors = {'Roger Moore':(1973,1986), 'Timothy Dalton':(1987,1994), 'Pierce Brosnan':(1995,2005), 'Daniel Craig':(2006,2021) }    
    turn_18_year = birth_year + 18  
    for actor,(start_year, end_year) in actors.items():
        #Limit the turn_18_year in the range between start year and end year  
        if turn_18_year >= start_year and (turn_18_year<=end_year):  
            return actor  
    return "No favourite Bond actor found"   
#For example:  
birth_year = 1964
favourite_actor = get_favourite_actor(birth_year)  
#Print the favourite actor
print(favourite_actor)