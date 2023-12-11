import pandas as pd
import string

# this looks at the correlation between meadian household income of districts and their
# average expenditure per student

# pps = per pupil/ADA (ADA = average daily attendance) spending
# https://www.cde.ca.gov/ds/fd/ec/currentexpense.asp
df_pps = pd.read_excel('data/currentexpense2122.xlsx')
df_pps.columns = list(string.ascii_uppercase)[0:len(df_pps.columns)]
df_pps = df_pps[['C', 'F']]
df_pps.columns = ['Name', 'Expenditures_pp']
df_pps.drop(range(10), axis=0, inplace=True)
df_pps.reset_index(drop=True, inplace=True)
for ind in df_pps.index:
    name = df_pps['Name'][ind]
    name = name.replace(" Unified", "").replace(" Elementary", "").replace(" High", "")
    df_pps['Name'][ind] = name

# mhi = median houselhold income (field DP03_0062E of the American Community Survey (ACS) by the Census Bureau)
# https://data.census.gov/table?g=040XX00US06,06$9500000,06$9600000,06$9700000&d=ACS%205-Year%20Estimates%20Data%20Profiles
df_mhi = pd.read_csv('data/ACSDP5Y2022.DP03-Data.csv')
df_mhi = df_mhi[['NAME', 'DP03_0062E']]
df_mhi.columns = ['Name', 'MHI']
df_mhi.drop(range(2), axis=0, inplace=True)
df_mhi.reset_index(drop=True, inplace=True)
df_mhi.drop((980), axis=0, inplace=True)

# get r^2

# df21 = pd.read_excel('data/currentexpense2021.xlsx')
# df21.columns = list(string.ascii_uppercase)[0:len(df21.columns)]
# df21.drop(range(10), axis=0, inplace=True)
# df21.reset_index(drop=True, inplace=True)

# df = pd.read_excel('data/currentexpense2122.xlsx')
# df.columns = list(string.ascii_uppercase)[0:len(df.columns)]
# df.drop(range(10), axis=0, inplace=True)
# # df.drop(df[df['E']<100].index, inplace=True)
# df.reset_index(drop=True, inplace=True)