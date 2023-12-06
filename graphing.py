from school_funding_sources import *
import matplotlib.pyplot as plt

years = [year for year in sorted(fed_perc_us)]

plt.figure()
plt.plot(years, [state_perc_ca[year] for year in years], linestyle='-', c='b', label='State')
plt.plot(years, [local_perc_ca[year] for year in years], linestyle='-', c='r', label='Local')
plt.plot(years, [fed_perc_ca[year] for year in years], linestyle='-', c='g', label='Fed')
plt.xlabel("Year")
plt.ylabel("% School Funding by Source")
plt.title("California")
plt.grid(zorder=1)
plt.legend()
plt.axvspan(1977.9, 1978.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 13", (1978.2, 15))
plt.axvspan(2012.9, 2013.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 30", (2013.2, 15))
plt.axvspan(1987.9, 1988.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 98", (1982, 51))
plt.axvspan(1989.9, 1990.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Start of Recession", (1990.2, 45.5))
plt.axvspan(1993.9, 1994.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("End of Recession", (1994.2, 40.5))
plt.show()