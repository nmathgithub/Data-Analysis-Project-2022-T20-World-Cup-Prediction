# This is the main stack file from which we run other functions 
import pandas as pd 
import numpy as np

from read_WC_data import Squad_Metrics 

# Assemble Training Data 
ave_age_07, ave_T20I_exp_07, ave_int_exp_07, total_left_07, total_right_07, total_wicketkeepers_07, total_bowling_options_07 = Squad_Metrics('2007.xlsx')