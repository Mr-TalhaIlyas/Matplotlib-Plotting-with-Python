import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import cv2
import os, glob, imageio
import random 
from tqdm import tqdm
import xmltodict
import seaborn as sns
mpl.rcParams['figure.dpi'] = 300
#%%
##################################################################
# For single group bar chart
##################################################################
random.seed = 42
#classes = [ "mitosis", "non_mitosis","apoptosis","tumor","non_tumor", "lumen", "non_lumen"]
classes = [ "blossom_end_rot", "graymold","powdery_mildew","spider_mite","spotting_disease"]

xml_filepaths = glob.glob( os.path.join( 'D:/cw_projects/paprika/new_mod/no_spider/test/' , '*.xml' ) )
all_classes = []
for filepath in tqdm(xml_filepaths, desc='Converting'):
 
    full_dict = xmltodict.parse(open( filepath , 'rb' ))
    obj_boxnnames = full_dict[ 'annotation' ][ 'object' ]
    
    if obj_boxnnames != None:
        for i in range(len(obj_boxnnames)):
            
            try:
                all_classes.append(full_dict[ 'annotation' ][ 'object' ][i]['name'])
            except KeyError:
                all_classes.append(full_dict[ 'annotation' ][ 'object' ]['name'])

count = []
for i in range(len(all_classes)):
    count.append(classes.index(all_classes[i]))

class_in, counts = np.unique(count, return_counts=True)

cc = np.zeros((len(classes)))
for i,j in enumerate(class_in):
    cc[j] = counts[i]

x = np.arange(len(classes))

rgb = []
for i in range(len(classes)):
    rgb.append((random.random(), random.random(), random.random()))
plt.bar(x, cc, color=rgb)#['b', 'g', 'r', 'c', 'm', 'y', 'teal', 'gray'])
classes= [ "blossom_end_rot", "graymold","powdery_mildew","spider_mite","cercospora"]
plt.xticks(np.arange(len(classes)), classes, rotation=45, ha="center")
plt.ylabel('Number of Instances')
#%%
##################################################################
# For multi group bar chart
##################################################################


classes = [ "blossom_end_rot", "graymold","powdery_mildew","spider_mite","spotting_disease"]

directory = glob.glob('D:/cw_projects/paprika/new_mod/no_spider/splits/*')

all_counts = []
for path in directory:
    
    xml_filepaths = glob.glob( os.path.join( path , '*.xml' ) )
    all_classes = []
    
    for filepath in tqdm(xml_filepaths, desc='Converting'):
     
        full_dict = xmltodict.parse(open( filepath , 'rb' ))
        obj_boxnnames = full_dict[ 'annotation' ][ 'object' ]
        
        if obj_boxnnames != None:
            for i in range(len(obj_boxnnames)):
                
                try:
                    all_classes.append(full_dict[ 'annotation' ][ 'object' ][i]['name'])
                except KeyError:
                    all_classes.append(full_dict[ 'annotation' ][ 'object' ]['name'])
    
    count = []
    for i in range(len(all_classes)):
        count.append(classes.index(all_classes[i]))
    
    class_in, counts = np.unique(count, return_counts=True)
    
    cc = np.zeros((len(classes)))
    for i,j in enumerate(class_in):
        cc[j] = counts[i]
    
    all_counts.append(cc)



all_counts = np.asarray(all_counts).astype(np.uint16)

#all_counts = all_counts / np.max(all_counts)
# Creating dataframe
exam_data = {'name': ['Test', 'Train', 'Val'],
            'blossom_end_rot': [],
            'graymold': [],
            'powdery_mildew': [],
            'spider_mite': [],
            'cercospora': []}


for idx, i in enumerate(list(exam_data.keys())[1:]):
    exam_data[i] = all_counts[:,idx]

#%
df = pd.DataFrame(exam_data, columns = ['name', "blossom_end_rot", "graymold","powdery_mildew","spider_mite","cercospora"])
print(); print(df)

# Setting the positions and width for the bars
pos = list(range(len(df['blossom_end_rot'])))
width = 0.1

# Plotting the bars
fig, ax = plt.subplots(figsize=(8,5))

# Creating a bar with Maths_score data
plt.bar(pos, df['blossom_end_rot'], width, alpha=0.5, color='b')
#plt.show()

# Creating a bar with Science_score data,
plt.bar([p + width for p in pos], df['graymold'], width, alpha=0.5, color='g')
#plt.show()

# Creating a bar with French_score data,
plt.bar([p + width*2 for p in pos], df['powdery_mildew'], width, alpha=0.5, color='r')
#plt.show()

plt.bar([p + width*3 for p in pos], df['spider_mite'], width, alpha=0.5, color='c')

plt.bar([p + width*4 for p in pos], df['cercospora'], width, alpha=0.5, color='m')


# Setting the y axis label
ax.set_ylabel('Number of Instances')

# Setting the chart's title
ax.set_title('Data Splits')

# Setting the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Setting the labels for the x ticks
ax.set_xticklabels(df['name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
#plt.ylim([0, max(df['blossom_end_rot'] + df['graymold'] + df['powdery_mildew'] + df['spider_mite'] + df['cercospora'])] )
plt.ylim([0, np.max(all_counts)])

# Adding the legend and showing the plot
plt.legend(["blossom_end_rot", "graymold","powdery_mildew","spider_mite","cercospora"], loc='upper left')
#plt.grid()
plt.show()