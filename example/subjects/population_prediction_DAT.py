import math
import re
filename = 'DAT.txt'
fr = open(filename,'r')
lines = fr.read()

field_1 = 'population: '
field_2 = 'growth rate: '
field_3 = 'years: '
target = '([0-9\.\-])'
pattern = re.compile(field_1+target)
#pattern = re.compile(field_1+target+field_2+target+field_3+target)
match = pattern.search(lines)

print(lines)
print(match.group())


#print(' =====you need to type in current population, birth rate and years===== \n\n')

#current_population = int(input('please type in current population: '))
#rate = int(input('please type in the increasing rate(per 1000): '))
#years = int(input('please type in how many years: '))
#water_consumption_per_person = int(input('please type in the amount of water consumption per person per day: '))

#future_population = current_population*(rate/1000+1)**years
#future_total_water_consumption = future_population*water_consumption_per_person

#print(future_population)
#print(future_total_water_consumption)
input()
