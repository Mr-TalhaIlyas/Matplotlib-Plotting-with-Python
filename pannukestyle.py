
'''
Pnnukae style plot
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

mpl.rcParams['figure.dpi'] = 500

# Data remains the same
data = {'Macro Class': ['crop']*10 + ['weed']*22,
        'Micro Class': ['bean', 'corn', 'foxtail-millet', 'great-millet', 'green-gram', 'peanut', 'perilla', 'proso-millet', 'red-bean', 'sesame', 'asian-flatsedge', 'bloodscale-sedge', 'cockspur-grass',
                        'cooper-leaf', 'early-barnyard-grass', 'fall-panicum', 'finger-grass', 'goosefoot', 'green-foxtail', 'henbit', 'indian-goosegrass', 'livid-pigweed', 'nipponicus-sedge', 'poa-annua',
                        'purslane', 'redroot-pigweed', 'smooth-pigweed', 'white-goosefoot', 'korean-dock', 'asiatic-dayflower', 'ILMCW', 'RFMCW'],
        'Samples': [6260, 6130, 5841, 6765, 5447, 6966, 5016, 6249, 6459, 5078, 12783, 6285, 9296, 4948, 210, 9330, 9207, 6110, 7594, 7540, 9933, 7540, 5445, 210, 5656, 7540, 7540, 6862, 6018, 6018, 16222, 7280],
        '0°': [1083, 521, 186, 727, 780, 512, 614, 226, 991, 858, 3219, 1572, 3709, 1276, 59, 3740, 3710, 2644, 2343, 3016, 3272, 3016, 1362, 60, 2262, 3016, 3016, 2814, 1527, 1527, 3930, 0],
        '45°': [3449, 3875, 3678, 3964, 3050, 4057, 2868, 3908, 3581, 2806, 6434, 3141, 3755, 2544, 76, 3755, 3662, 2609, 3601, 3016, 4536, 3016, 2721, 75, 2262, 3016, 3016, 2805, 3054, 3054, 7860, 0],
        '90°': [1728, 1734, 1977, 2074, 1617, 2391, 1534, 2115, 1887, 1414, 3129, 1572, 1832, 1128, 75, 1835, 1835, 857, 1650, 1508, 2125, 1508, 1362, 75, 1131, 1508, 1508, 1243, 1437, 1437, 4432, 7280]}

df = pd.DataFrame(data)

df = df.melt(id_vars=['Macro Class', 'Micro Class'], var_name='Angle', value_name='Angle_Samples')
# df = df.sort_values('Micro Class', ascending=False)
# plt.style.use('bmh')
sns.set(style="ticks")
sns.set_palette("Set2")
plt.figure(figsize=(8, 15))

grouped = df.groupby(['Macro Class', 'Micro Class', 'Angle']).sum().reset_index()
grouped = grouped.sort_values(by='Micro Class', ascending=False)
# Normalize data
grouped['Normalized_Angle_Samples'] = grouped.groupby(['Macro Class', 'Micro Class'], group_keys=False)['Angle_Samples'].apply(lambda x: x / x.sum())

# Plot the stacked bar chart
left = np.zeros(len(grouped['Micro Class'].unique()))
edgecolor = 'white'  # Set edge color to white

angle_sums = grouped.groupby('Angle')['Angle_Samples'].sum()

# Plot the stacked bar chart
left = np.zeros(len(grouped['Micro Class'].unique()))
edgecolor = 'white'  # Set edge color to white

for angle in ['0°', '45°', '90°']:
    angle_samples = grouped[grouped['Angle'] == angle]['Normalized_Angle_Samples'].values
    angle_sum = angle_sums[angle]
    label = f'{angle} ({format(angle_sum, "," )})'
    plt.barh(grouped['Micro Class'].unique(), angle_samples, left=left, label=label, edgecolor=edgecolor, height=1)
    left += angle_samples

# Customize the chart
# plt.ylabel('Micro Class')
plt.xlabel('Percentage of Samples')
# plt.title('Sample Distribution by Macro Class, Micro Class, and Angle (Normalized)')

total_samples = grouped.groupby(['Macro Class', 'Micro Class'])['Angle_Samples'].sum().reset_index()
total_samples = total_samples.sort_values(by='Micro Class', ascending= False)
# Modify class labels with the total number of samples
y_labels = [f'{label} ({format(int(total_samples.iloc[i]["Angle_Samples"]/2), ",")})' for i, label in enumerate(grouped['Micro Class'].unique())]
# y_labels = [f'{label} ({total_samples.iloc[i]["Samples"]})' for i, label in enumerate(grouped['Micro Class'].unique())]
plt.yticks(np.arange(len(y_labels)), y_labels, rotation=0, va='center')
plt.legend(title='Capture Angle', loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3)
plt.ylim(-0.5, len(grouped['Micro Class'].unique()) - 0.5)
plt.xlim(0, 0.5)
# Show the plot
plt.tight_layout()

plt.gca().xaxis.set_visible(False)
plt.show()
