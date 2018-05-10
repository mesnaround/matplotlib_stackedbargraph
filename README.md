### Stacked bar graph
Uses:
 * Python3
 * matplotlib
 * numpy

I was looking around for a solution to create a stacked bar graph that contained more than 3 categories for each year. The example I found in the matplotlib documents did not work for more than 3 categories. I found two matplotlib options:
 1. https://gist.github.com/ctokheim/6435202a1a880cfecd71
 2. https://github.com/minillinim/stackedBarGraph

The first made use of seaborn, which I didn't want to use if possible. It also didn't stack the bars on top of each other like I wanted. 

I didn't use the second because I didn't need a full blown class. 

So I decided to make my own.

This is useful if you have a dataframe with some x axis value like year, a categorical column, and associated numeric value for each categorical observation. Refer to the sample dataframe in the code.

### What doesn't work
This is what I guessed would simply work, but it does not. I don't know why.

```
# This doesn't work for more than 3 categories
colors=['#55aadd','#fccf40','#e63920','#310000','#0000ff','#85bf4f','#251fcc','g','b','r']
idx = 0
fig, ax = plt.subplots(figsize=(9,7))
# Dataframe df has columns: year, category, amount
for cat in df.category.unique():
    x = df[df['category']==cat].groupby(['year']).amount.sum()
    ax.bar(x.index, x, color = colors[idx])
    idx += 1
ax.grid()
ax.legend(df.category.unique())
```
