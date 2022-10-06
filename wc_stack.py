# This is the main stack file from which we run other functions 
import pandas as pd 
import numpy as np

from read_WC_data import Squad_Metrics 

# Assemble Training Data 
# 2007 Data 

# Squad_Metrics returns 
# ave_age, ave_T20I_exp, ave_int_exp, total_left, total_right, total_wicketkeepers, total_bowling_options

squad_metrics_2007 = Squad_Metrics('2007.xlsx')
print(squad_metrics_2007)
squad_metrics_2009 = Squad_Metrics('2009.xlsx')
print(squad_metrics_2009)
squad_metrics_2010 = Squad_Metrics('2010.xlsx')
print(squad_metrics_2010)
squad_metrics_2012 = Squad_Metrics('2012.xlsx')
print(squad_metrics_2012)
squad_metrics_2014 = Squad_Metrics('2014.xlsx')
print(squad_metrics_2014)
squad_metrics_2016 = Squad_Metrics('2016.xlsx')
print(squad_metrics_2016)
squad_metrics_2021 = Squad_Metrics('2021.xlsx')
print(squad_metrics_2021)