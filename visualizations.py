"""import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Create a kernel density estimate plot without filling
sns.kdeplot(data, fill=True)

# Show the plot
plt.show()"""

"""import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Create a kernel density estimate plot with a custom color palette
sns.kdeplot(data, fill=True, color='purple')  # Change 'Blues' to your desired palette

# Show the plot
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=5000)
sns.distplot(x[x<10], kde=False)

plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
