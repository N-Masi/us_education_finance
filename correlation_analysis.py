import pandas as pd
import string
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import math

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
    district = df_pps['Name'][ind]
    if not ('San Lorenzo' in district):
        district = "".join(["(?=.*"+s+")" for s in district.split(" ")])
    df_pps['Name'][ind] = district

# mhi = median houselhold income (field DP03_0062E of the American Community Survey (ACS) by the Census Bureau)
# Districts with mutliple entries for broken up schools within were only looked at on the district level.
# In a few cases, the CA Dept. of Educ. reported expenditures for combined elementary and high districts but the ACS
# had reported median incomes for these districts separately, because the median incomes differed these instances were excluded
# from the data (removed from the Excel files in the /data folder).
# https://data.census.gov/table?g=040XX00US06,06$9500000,06$9600000,06$9700000&d=ACS%205-Year%20Estimates%20Data%20Profiles
df_mhi = pd.read_csv('data/ACSDP5Y2022.DP03-Data.csv')
df_mhi = df_mhi[['NAME', 'DP03_0062E']]
df_mhi.columns = ['Name', 'MHI']
df_mhi.drop(range(2), axis=0, inplace=True)
df_mhi.reset_index(drop=True, inplace=True)
df_mhi.drop((934), axis=0, inplace=True)

# get data and print r^2
x = []
y = []
for ind in df_pps.index:
    district = df_pps['Name'][ind]
    mhi = df_mhi[df_mhi['Name'].str.contains(district)]['MHI']
    if len(mhi) > 1: raise Exception("district name mismatch for district:", district)
    if mhi.iloc[0] == '250,000+': mhi.iloc[0] = '250000'
    if mhi.iloc[0] != '-':
        x.append(float(mhi.iloc[0]))
        y.append(df_pps['Expenditures_pp'][ind])
logy = [math.log(yy) for yy in y]
print("Linear regression: r =", pearsonr(x, y)[0], "and r^2 =", pearsonr(x, y)[0]**2)
print("Log regression: r =", pearsonr(x, logy)[0], "and r^2 =", pearsonr(x, logy)[0]**2)

# plot figure - figure out two panels in the same
fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0].set_title("Education Expenditures of Districts by Median Household Income", pad=20)
axs[0].scatter(x, y, zorder=2)
axs[0].grid(zorder=1)
axs[0].set_ylabel("Expenditures Per Pupil", labelpad=5)
axs[1].scatter(x, logy, zorder=2)
axs[1].grid(zorder=1)
axs[1].set_xlabel("Median Household Income", labelpad=10)
axs[1].set_ylabel("Log of Expenditures Per Pupil", labelpad=17)
plt.show()
