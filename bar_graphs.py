import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 600

# Creating dataframe
exam_data = {'name': ['Train', 'Validation', 'Test'],
            'Ripe': [1373, 134, 390],
            'Unripe': [595, 76, 151],
            'Green': [2078, 556, 391]}
df = pd.DataFrame(exam_data, columns = ['name', 'Ripe', 'Unripe', 'Green'])
print(); print(df)

# Setting the positions and width for the bars
pos = list(range(len(df['Ripe'])))
width = 0.15

# Plotting the bars
fig, ax = plt.subplots(figsize=(7,5))

# Creating a bar with Maths_score data
plt.bar(pos, df['Ripe'], width, alpha=0.5, color='r', edgecolor='white')
#plt.show()

# Creating a bar with Science_score data,
plt.bar([p + width for p in pos], df['Unripe'], width, alpha=0.5, color='c', edgecolor='white')
#plt.show()

# Creating a bar with French_score data,
plt.bar([p + width*2 for p in pos], df['Green'], width, alpha=0.5, color='g', edgecolor='white')
#plt.show()

# Setting the y axis label
ax.set_ylabel('Number of Instances')

# Setting the chart's title
ax.set_title('SS1K Dataset')

# Setting the position of the x ticks
ax.set_xticks([p + 1 * width for p in pos])

# Setting the labels for the x ticks
ax.set_xticklabels(df['name'])

# Setting the x-axis and y-axis limits
#plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['Ripe'] + df['Unripe'] + df['Green'])] )

# Adding the legend and showing the plot
plt.legend(['Ripe', 'Unripe', 'Green'], # legends dict
           loc='lower left',            # location of legend
           bbox_to_anchor=(0, -.17, 1, 5), # offset in above defines location
           ncol=3,                         # number of coloumns for legends
           mode="expand")                  # expand legends along the x-axis
plt.grid(alpha=0.3, axis='y')
plt.show()