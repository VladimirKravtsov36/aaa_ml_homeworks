import matplotlib.pyplot as plt
import numpy as np
import datetime

np.random.seed(42)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15,10))
fig.suptitle('Plot examples', fontsize=20)

ax1.set_title('Scatter plot example')
norm_dist = np.random.multivariate_normal([20, 10], [[1, 0.7], [0.7, 1]],
                                          size=1000)
ax1.scatter(norm_dist[:, 0], norm_dist[:, 1], edgecolors='black')

ax2.set_title('Hist plot example')
geom_dist = np.random.geometric(p=0.1, size=3000)
ax2.hist(geom_dist, bins=40, color='r')

ax3.set_title('Line plot example')
x = np.arange(0.001, 6, 0.01)
ax3.plot(x, np.log(x), c='black', label='log(x)')
ax3.plot(x, np.log(2*x), c='r', label='log(2x)')
ax3.legend()

ax4.set_title('Bar plot example')
bars = np.random.normal(loc=5, size=14)
start_date = datetime.date.fromisoformat('2021-01-14')
dates = [start_date - datetime.timedelta(days=x) for x in range(14)]
ax4.bar(dates, bars)
ax4.set_xticks(dates)
ax4.set_xticklabels(dates, rotation=90)

plt.show()
