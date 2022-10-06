import pandas as pd 
import numpy as np 

# Create Function to read file and analyze metrics.

def Squad_Metrics(team_file): 
    # Read Past World Cup Winners Excel Data 
    # This will be our training data.
    team_data = pd.read_excel(team_file)
    # print(WC_win_data)

    # Now, calculate the metrics 
    # Note, we use the Ceiling function to round up the average age, average experience, etc. 

    # Calculate Average Age 
    ave_age = np.ceil(np.average(team_data['Player_Age']))
    # print(ave_age)

    # Calculate Average T20I Experience 
    ave_T20I_exp = np.ceil(np.average(team_data['T20IExp']))
    # print(ave_T20I_exp)

    # Calculate Average International Experience 
    ave_int_exp = np.ceil(np.average(team_data['IntExp']))
    # print(ave_int_exp)

    # Calculate Total Number of Left Handy Batters
    total_left = np.sum(team_data['L'])
    # print(total_left)

    # Calculate Total Number of Right Handy Batters
    total_right = np.sum(team_data['R'])
    # print(total_right)

    # Calculate Total Number of Bowling Options 
    total_all_round_options = np.sum(team_data['AR'])
    # print(total_all_round_options)

    # Calculate Total Number of All-Round Options 
    total_bowling_options = np.sum(team_data['BO'])
    # print(total_bowling_options)

    # Calculate Total Number of Wicketkeeping Optiosn 
    total_wicketkeepers = np.sum(team_data['WK'])
    # print(total_wicketkeepers)

    return ave_age, ave_T20I_exp, ave_int_exp, total_left, total_right, total_wicketkeepers, total_bowling_options, total_all_round_options