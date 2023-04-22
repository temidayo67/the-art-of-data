#plotting histograms from sklearn dataset
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt 
from matplotlib import style
boston_real_estate_data = load_boston()
#print(boston_real_estate_data.DESCR())
x_axis = boston_real_estate_data.data
y_axis = boston_real_estate_data.target
style.use('ggplot')
plt.figure(figsize=(7,7))
plt.hist(y_axis, bins =50)
plt.xlabel('force in 1000g')
plt.ylabel('number of house')
plt.show()
