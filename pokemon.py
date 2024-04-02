#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
percorso_file_csv = "C:\\Users\\davide\\Downloads\\pokemons (1).csv"
df = pd.read_csv(percorso_file_csv)
print(df.head())


# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

percorso_file_csv = "C:\\Users\\davide\\Downloads\\pokemons (1).csv"
df = pd.read_csv(percorso_file_csv)

# Scatter plot
sns.scatterplot(x='atk', y='def', data=df)
plt.title('Pokemon Attack vs Defense')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.show()


# In[ ]:





# In[ ]:




