import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

data_frame = pd.read_csv("./csv/911.csv")

data_frame.info()
data_frame.head(5)

data_frame['zip'].value_counts().head(5)
data_frame['twp'].value_counts().head(5)

data_frame['Reason'] = data_frame('title').apply(lambda title: title.split(':')[0])

data_frame['Reason'].value_counts()

print(data_frame)