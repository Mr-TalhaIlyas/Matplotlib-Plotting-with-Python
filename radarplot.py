import matplotlib.pyplot as plt
import numpy as np
import squarify
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 500
age_in_weeks = np.array(['w0', 'w1', 'w10', 'w11', 'w12', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9'])
number_of_samples = np.array([17379, 29719, 2006, 1913, 826, 29672, 27386, 29490, 17914, 10068, 4676, 3484, 2279])

# Sort age_in_weeks based on the integer value after 'w'
sorted_indices = np.argsort([int(a[1:]) for a in age_in_weeks])

# Apply sorted_indices to age_in_weeks and number_of_samples
age_in_weeks_sorted = age_in_weeks[sorted_indices]
number_of_samples_sorted = number_of_samples[sorted_indices]

# Calculate proportions
total_samples = np.sum(number_of_samples_sorted)
proportions = number_of_samples_sorted / total_samples * 100
proportion_labels = [f'{age}\n({prop:.2f}%)' for age, prop in zip(age_in_weeks_sorted, proportions)]

# Assign a unique color to each rectangle using a colormap
# colors = plt.cm.viridis(np.linspace(0, 1, len(age_in_weeks_sorted)))
colors = plt.cm.tab20(np.linspace(0, 1, len(age_in_weeks_sorted)))

# Create a treemap
fig, ax = plt.subplots(figsize=(10, 13))
squarify.plot(sizes=number_of_samples_sorted, label=proportion_labels, alpha=0.8, color=colors)
# ax.set_title('Proportion of Samples by Age in Weeks (Treemap)')
ax.axis('off')  # Remove axis for better visualization
plt.show()
#%%

import seaborn as sns      
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 500
data = {'Product': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 
                    'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13'],
        '0°': [6399, 10025, 8364, 7690, 7404, 4049, 1722, 623, 584, 560, 560, 560, 184],
        '45°': [7242, 12446, 14333, 12529, 14345, 9177, 6590, 2827, 2471, 1528, 1304, 1233, 572],
        '90°': [3738, 7248, 6975, 7167, 7741, 4688, 2656, 1226, 429, 191, 142, 120, 70]
        }

plt.figure(figsize=(6, 6))
plt.style.use('fivethirtyeight')
sns.set(style="ticks")
# Convert data to a suitable format for plotting
product_data = {k: v for k, v in data.items() if k != 'Product'}
product_labels = data['Product']

# Compute the number of variables
num_vars = len(product_labels)

# Compute the angle of each axis in the plot
angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
angles += angles[:1]

# Prepare the radar plot
ax = plt.subplot(111, polar=True)

# Set the angle of the first axis
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Set the labels for each angle
plt.xticks(angles[:-1], product_labels)

# Draw the y-axis labels (radial ticks)
ax.set_rlabel_position(0)
max_val = max([max(values) for values in product_data.values()])
yticks = np.linspace(0, max_val, 5)
plt.yticks(yticks, map(lambda x: f'{int(x)}', yticks), color="black", size=7)
plt.ylim(0, max_val)

# Plot data
for label, values in product_data.items():
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=label)
    ax.fill(angles, values, alpha=0.25)

ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1))
plt.show()
