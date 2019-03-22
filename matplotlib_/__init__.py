import numpy as np
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12   # large, med, small = 22, 16, 12

params = {
    'axes.titlesize':large,
    'legend.fontsize':med,
    'figure.figsize':(16,10),
    'axes.labelsize':med,
    'axes.titlesize':med,
    'xtick.labelsize':med,
    'ytick.labelsize':med,
    'figure.titlesize':large
}

plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style('white')
# %matplotlib inline


print(mpl.__version__)
print(sns.__version__)