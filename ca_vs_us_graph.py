from school_funding_sources import *
import matplotlib.pyplot as plt

years = [year for year in sorted(fed_perc_us)]
prop_tax_years = [year for year in sorted(prop_tax_us)]

plt.figure()
plt.plot(years, [local_perc_ca[year] for year in years], linestyle='-', c='c', label='All Local Sources (CA)')
plt.plot(years, [local_perc_us[year] for year in years], linestyle='-', c='m', label='All Local Sources (US)')
plt.plot(prop_tax_years, [prop_tax_ca[year] for year in prop_tax_years], linestyle='--', c='c', label='Property Tax (CA)')
plt.plot(prop_tax_years, [prop_tax_us[year] for year in prop_tax_years], linestyle='--', c='m', label='Property Tax (US)')
plt.title("Percent of Public Education Funds by Origin by Year")
plt.xlabel("End of Academic Year")
plt.ylabel("% of All Funding Originating from a Given Source")
plt.grid(zorder=1)
plt.legend()
plt.show()