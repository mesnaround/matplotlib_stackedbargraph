### Stacked bar graph
Uses:
 * Python3
 * matplotlib
 * numpy

I was looking around for a solution to create a stacked bar graph that contained multiple categories for each year. I found two matplotlib options:
 1. https://gist.github.com/ctokheim/6435202a1a880cfecd71
 2. https://github.com/minillinim/stackedBarGraph

The first made use of seaborn, which I didn't want to use if possible. It also didn't stack the bars on top of each other like I wanted. 

I didn't use the second because I didn't need a full blown class. 

So I decided to make my own.

This is useful if you have a dataframe with some x axis value like year, a categorical column, and associated numeric value for each categorical observation. Refer to the sample dataframe in the code.
