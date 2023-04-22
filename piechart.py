import matplotlib.pyplot as plt
import numpy as np

percentile = np.array([62,5,4,2,1,26])
Causes = ["Chronic Diseases", "Unintentional Injuries", "Alzheimers", "Influenza and Pneumonia",
          "Sepsis", "Others"]
explode = ([0.2,0,0,0,0,0])
plt.axis("equal")
plt.pie(percentile, labels=Causes, explode=explode,
        radius=1.5, shadow=True, autopct='%.1f%%',startangle=70)
plt.title("Causes of deaths in Ohio")
plt.legend()
plt.show()