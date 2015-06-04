import math

print(' =====you need to type in current population, birth rate and years===== \n\n')

current_population = int(input('please type in current population: '))
rate = int(input('please type in the increasing rate(per 1000): '))
years = int(input('please type in how many years: '))
#water_consumption_per_person = int(input('please type in the amount of water consumption per person per day: '))

future_population = current_population*(rate/1000+1)**years
#future_total_water_consumption = future_population*water_consumption_per_person

print(future_population)
#print(future_total_water_consumption)
input()
