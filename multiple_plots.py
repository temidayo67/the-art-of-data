#creating multiplots
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
web_monday = np.array([123,645,950,1290,1630,1450,1034,1295,465,205,80])
web_tuesday = np.array([95,680,889,1145,1670,1323,1119,1265,510,310,110])
web_wednesday = np.array([105,630,700,1000,1520,1124,1239,1380,580,610,270])
time_hrs = np.array([7,8,9,10,11,12,13,14,15,16,17])
style.use('ggplot')
plt.plot(time_hrs,web_monday,label='monday', color= 'b',linestyle='--',linewidth=1.0)
plt.plot(time_hrs,web_tuesday,label='tuesday', color= 'r',linestyle='--',linewidth=1.5)
plt.plot(time_hrs,web_wednesday,label='wednesday', color= 'g',linestyle='--',linewidth=2.0)
plt.title('Website Traffic')
plt.xlabel('Time')
plt.ylabel('Users')
plt.legend()
plt.show()