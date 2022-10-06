import pandas as pd 
import numpy as np 

# Read Past World Cup Winners Excel Data 
# This will be our training data.
WC_win_data = pd.read_excel('2007.xlsx')
# print(WC_win_data)

# Now, calculate the metrics 
# Note, we use the Ceiling function to round up the average age, average experience, etc. 

# Calculate Average Age 
ave_age = np.ceil(np.average(WC_win_data['Player_Age']))
print(ave_age)

# Calculate Average T20I Experience 
ave_T20I_exp = np.ceil(np.average(WC_win_data['T20IExp']))
print(ave_T20I_exp)

# Calculate Average International Experience 
ave_int_exp = np.ceil(np.average(WC_win_data['IntExp']))
print(ave_int_exp)

# Calculate Total Number of Left Handy Batters
total_left = np.sum(WC_win_data['L'])
print(total_left)

# Calculate Total Number of Right Handy Batters
total_right = np.sum(WC_win_data['R'])
print(total_right)

# Calculate Total Number of Bowling Options 
total_bowling_options = np.sum(WC_win_data['BO'])
print(total_bowling_options)

# Calculate Total Number of Wicketkeeping Optiosn 
total_wicketkeepers = np.sum(WC_win_data['WK'])
print(total_wicketkeepers)