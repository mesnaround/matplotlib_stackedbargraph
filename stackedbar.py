import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create some fake data
categories = ['lights','fridge','washer','car','heat','food']
import random
months = [1,2,3,4,5,6,7,8,9,10,11,12]

data = []
for month in months:
  for cat in categories:
    data.append((month, cat, random.random()*500))

df = pd.DataFrame(data, columns = ['month','category','energy'])

# Add two dicts together, do not need to have the exact same keys, create new key if not present in other
def add_dicts(d1, d2):
    d3 = d2.copy()
    for k1 in d1.keys():
        d3[k1] = d3.get(k1, 0) + d1[k1]
    return d3


fig, ax = plt.subplots(figsize=(10,7))
color_idx = 0
# These are just some random colors I assembled.
colors=['#55aadd','#fccf40','#e63920','#310000','#0000ff','#85bf4f','#251fcc','g','b','r']
mnths = df.month.unique()

# This is the dictionary that keeps the running tally for each x value
margin_dict = dict((el,0) for el in df.month.unique())

for cat in df.category.unique():
    tmp_df = df[df['category']==cat].loc[:,['month','energy']]
    
    # Add missing mnths to series with 0 height to facilitate the stacked bar plot
    missing_rows = [[yr, 0] for yr in [y for y in mnths if not tmp_df.month.isin([y]).any()]]
    tmp_df = tmp_df.append(pd.DataFrame(missing_rows, columns = ['month','energy']), ignore_index=True)
    
    # Group by before plotting
    x = tmp_df.groupby(['month']).energy.sum()
    
    bottom_margin = np.array([margin_dict[key] for key in sorted(margin_dict)])
    
    ax.bar(x.index, x, 0.6, align='center', color=colors[color_idx], bottom=bottom_margin)
    
    # Add two dictionaries together and keep track of tops of each bar to position the stacking
    margin_dict = add_dicts(x.to_dict(), margin_dict)

    # Custom color index
    color_idx += 1
    if len(colors) == color_idx:
        color_idx = 0
        
ax.set_ylim(0, 3000)
ax.grid()
ax.legend(df.category.unique())
plt.savefig('test.png')


