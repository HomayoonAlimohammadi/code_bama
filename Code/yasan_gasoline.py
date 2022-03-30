gas_usage_per_100km = float(input('Enter Gasoline usage per 100km: '))

total_distance = 1000 * 2 # km
gas_needed = total_distance / 100 * gas_usage_per_100km # litre

'''
Instagram: @code_bama
'''

if gas_needed >= 60:
    total_cost = ((gas_needed-60) * 3000) + (60 * 1500) 
else:
    total_cost = gas_needed * 1500 

print('Total Cost would be:', total_cost)