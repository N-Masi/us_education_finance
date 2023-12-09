from school_funding_sources import *
import matplotlib.pyplot as plt

years = [year for year in sorted(fed_perc_us)]

plt.figure()
plt.plot(years, [state_perc_ca[year] for year in years], linestyle='-', c='b', label='State')
plt.plot(years, [local_perc_ca[year] for year in years], linestyle='-', c='r', label='Local')
plt.plot(years, [fed_perc_ca[year] for year in years], linestyle='-', c='g', label='Federal')
plt.xlabel("End of Academic Year")
plt.ylabel("% School Funding Coming From a Given Source")
plt.title("Funding Sources of California's Public Primary and Secondary Schools by Year")
plt.grid(zorder=1)
plt.legend()
plt.axvspan(1977.9, 1978.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 13", (1978.2, 14))
plt.axvspan(2012.9, 2013.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 30", (2013.2, 16))
plt.axvspan(1987.9, 1988.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Prop 98", (1984.75, 51))
plt.axvspan(1989.9, 1990.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Start of Recession", (1990.2, 45.5))
plt.axvspan(1993.9, 1994.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("End of Recession", (1994.2, 40.5))
plt.axvspan(1975.9, 1976.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Serrano II", (1972, 17.5))
plt.axvspan(1970.9, 1971.1, zorder=1, color='gray', alpha=0.7)
plt.annotate("Serrano I", (1967.25, 21))
plt.show()