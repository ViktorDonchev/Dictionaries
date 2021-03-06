import pprint

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [
    ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
    ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
    ['The Bahamas', 'Northeastern United States'], 
    ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
    ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
    ['Jamaica', 'Yucatn Peninsula'], 
    ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
    ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
    ['Bermuda', 'New England', 'Atlantic Canada'], 
    ['Lesser Antilles', 'Central America'], 
    ['Texas', 'Louisiana', 'Midwestern United States'], 
    ['Central America'], 
    ['The Caribbean', 'Mexico', 'Texas'], 
    ['Cuba', 'United States Gulf Coast'], 
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
    ['Mexico'], 
    ['The Caribbean', 'United States East coast'], 
    ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
    ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
    ['The Caribbean', 'United States East Coast'], 
    ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
    ['Central America', 'Yucatn Peninsula', 'South Florida'], 
    ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
    ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
    ['Bahamas', 'United States Gulf Coast'], 
    ['Cuba', 'United States Gulf Coast'], 
    ['Greater Antilles', 'Central America', 'Florida'], 
    ['The Caribbean', 'Central America'], 
    ['Nicaragua', 'Honduras'], 
    ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
    ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
    ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
    ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']
    ]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def updated_damages(damages):
    updated_damages_list = []
    for damage in damages:
        if "M" in damage:
            updated_damages_list.append(float(damage.strip("M")) * 1000000)
        elif "B" in damage:
            updated_damages_list.append(float(damage.strip("B")) * 1000000000)
        elif damage == "Damages not recorded":
            updated_damages_list.append(damage)
        else:
            updated_damages_list.append(float(damage))  
    return updated_damages_list

# test function by updating damages
updated_damages = updated_damages(damages)
# 2 
# Create a Table
def dict_data_on_hurricanes(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    nums = len(names)

    for num in range(nums):
        hurricanes[names[num]] = {"Name": names[num], "Month": months[num], "Year": years[num], "Max Sustained Winds": max_sustained_winds[num], "Areas Affected": areas_affected[num], "Damage": damages[num], "Deaths": deaths[num]}

    return hurricanes

# Create and view the hurricanes dictionary

hurricanes_dictionary = dict_data_on_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#pprint.pprint(hurricanes_dictionary)
# 3
# Organizing by Year
def data_by_year(hurricanes):
    new_dict = {}
    for value in hurricanes.values():
        new_dict[value.get("Year", None)] = value

    return new_dict
    

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = data_by_year(hurricanes_dictionary)
#pprint.pprint(hurricanes_by_year)

# 4
# Counting Damaged Areas
def counting_area(hurricanes):
    newList = []
    newListNums = []

    for val1 in hurricanes:
        for val2 in val1:
            if val2 not in newList:
                newList.append(val2)

    for kek in range(len(newList)):
        newListNums.append(0)

    #print(newListNums)

    new_dict = {key : value for key, value in zip(newList, newListNums)}
    #pprint.pprint(new_dict)

    for val1 in hurricanes:
        for val in val1:
            new_dict.keys() == val
            new_dict[val] += 1

    return new_dict

# create dictionary of areas to store the number of hurricanes involved in
hurricanes_areas_affected = counting_area(areas_affected)
#pprint.pprint(hurricanes_areas_affected)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(hurricanes):
    emptyList = []

    for values in hurricanes.values():
        emptyList.append(values)
    
    max_value = max(emptyList)
    name = ""

    for key, values in hurricanes.items():
        if values == max_value:
            name = key
    
    #print(f"Area with largest amount of hurricanes: {name}, value: {max_value}")



# find most frequently affected area and the number of hurricanes involved in
max_hurricane_count(hurricanes_areas_affected)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(names, deaths):
    deadlyDict = {key:value for key, value in zip(names, deaths)}
    
    max_deaths = max(deaths)
    name = ""

    for key, values in deadlyDict.items():
        if values == max_deaths:
            name = key

    #print(f"Deadliest Hurricane: {name}")

# find highest mortality hurricane and the number of deaths
deadliest_hurricane(names, deaths)

# 7
# Rating Hurricanes by Mortality
def mortality_rating(names, deaths):
    mortalityDict = {key:value for key, value in zip(names, deaths)}

    mortality_hurricane = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: []
    }

    newDict = {}
    for key, value in mortalityDict.items():
        if(value==0):
            mortality_hurricane[0].append(key)
        elif(value>0 and value<=100):
            mortality_hurricane[1].append(key)
        elif(value>100 and value<=500):
            mortality_hurricane[2].append(key)
        elif(value>500 and value<=1000):
            mortality_hurricane[3].append(key)
        else:
            mortality_hurricane[4].append(key)

    #pprint.pprint(mortality_hurricane)
    
mortality_rating(names, deaths)

# categorize hurricanes in new dictionary with mortality severity as key
#done

# 8 Calculating Hurricane Maximum Damage
def highest_damage(names, damages):
    deadlyDict = {key:value for key, value in zip(names, damages)}
    
    damages_clean = [value for value in damages if value != 'Damages not recorded']
    max_damage = max(damages_clean)
    name = ""

    for key, values in deadlyDict.items():
        if values == max_damage:
            name = key
    
    #print(f"Highest damage {name}")

# find highest damage inducing hurricane and its total cost
highest_damage(names, updated_damages)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def cost(names, damages):
    mortalityDict = {key:value for key, value in zip(names, damages)}

    mortality_hurricane = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: []
    }

    newDict = {}

    for key, value in mortalityDict.items():
        if value != 'Damages not recorded':
            val = float(value)
            if(val==0):
                mortality_hurricane[0].append(key)
            elif(val>0 and val<=100000000):
                mortality_hurricane[1].append(key)
            elif(val>100 and val<=1000000000):
                mortality_hurricane[2].append(key)
            elif(val>500 and val<=10000000000):
                mortality_hurricane[3].append(key)
            else:
                mortality_hurricane[4].append(key)

    pprint.pprint(mortality_hurricane)
    
cost(names, updated_damages)