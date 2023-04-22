# create a plot with matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

web_customers = np.array([123, 645, 950, 1290, 1630, 1450, 1034, 1295, 465, 205, 80])
time_hrs = np.array([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
style.use('ggplot')
plt.plot(time_hrs, web_customers, label='web traffic', color='b', linestyle='--',
         linewidth=1.0)
plt.title('Website Traffic')
plt.xlabel('Time')
plt.ylabel('Users')
plt.legend()
plt.show()
