# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:47:27 2022

@author: talha
"""
#%%
import numpy as np
import matplotlib.ticker as ticker
import matplotlib, copy
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 700
dsa = np.array([[0.92, 0, 0, 0, 0.0, 0.0, 0.02],
                [0, 0.88, 0.0, 0.0, 0.0, 0.0, 0.03],
                [0, 0, 0.83, 0,0, 0, 0.09],
                [0, 0.0, 0., 0.89, 0, 0.0, 0.06],
                [0, 0.03, 0.0, 0, 0.91,0, 0.65],
                [0, 0.0, 0.0, 0.0, 0.0, 0.89, 0.16],
                [0.08, 0.08, 0.17, 0.11, 0.08, 0.11, 0]])

ddl = np.array([[0.893, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0.075, 0.727, 0.018, 0, 0, 0, 0, 0, 0, 0, 0],
                [0.004, 0.003, 0.862, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.0028, 0.542, 0.005, 0, 0, 0.014, 0.007, 0.155, 0],
                [0, 0, 0.001, 0.004, 0.793, 0, 0, 0.001, 0.001, 0.038, 0],
                [0, 0, 0, 0, 0, 0.541, 0.031, 0, 0.001, 0, 0],
                [0, 0, 0, 0, 0, 0.003, 0.592, 0, 0, 0, 0],
                [0, 0, 0.001, 0, 0, 0, 0.005, 0.602, 0.084, 0.203, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.893, 0.035, 0.007],
                [0, 0, 0, 0, 0, 0, 0, 0 , 0.17, 0.892, 0],
                [0, 0, 0, 0 ,0 , 0, 0, 0, 0, 0.079, 0.872]
    ])
label = ['br1', 'br2',  'br3', 'gm1', 'gm2', 'pm1',  'pm2', 'cp1', 'cp2', 'cp3', 'cp4']
label2 = ['BlosssomEndRot', 'Graymold', 'PowderyMildew', 'SpiderMite', 'Cercospora', 'Snails&Slugs', 'BG FN']
label3 = ['BlosssomEndRot', 'Graymold', 'PowderyMildew', 'SpiderMite', 'Cercospora', 'Snails&Slugs', 'BG FP']
#%%
def plot_confusion_matrix(cm, x_labels, y_labels, normalize = True, show_text = True, \
                          my_cmap = 'BuPu', threshold=None, textcolors=("black", "white"),
                          plt_clrbar=True, valfmt="{x:.2f}", v_thresh=0.01, **textkw):
    '''
    Parameters
    ----------
    cm : A mxn array conataining data to be ploted
    x_labels : labels to be shown on x-axis
    y_labels : labels to be shown on y-axis
    normalize : Whether to normalize the data array between [0, 1]. The default is True.
    show_text : Whether to show text or not. The default is True.
    my_cmap : Colormap used for plotting. The default is 'BuPu'.
    threshold : Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.
    textcolors : A pair of colors.  The first is used for values below a threshold,
        the second for those above. The default is ("black", "white").
    v_thresh :threshold on values to be shown on heatmap.
    plt_clrbar : whether to plot colorbar or not. The default is True.
    valfmt : The format of the annotations inside the heatmap. The default is "{x:.2f}".
    **textkw : All other arguments are forwarded to each call to `text` used to create
        the text labels.
    '''  
    
    c_m = cm
    
    if normalize:
        row_sums = c_m.sum(axis=1)
        c_m = c_m / row_sums[:, np.newaxis]
        c_m = np.round(c_m, 3)
        
        
    fig, ax = plt.subplots(figsize=(len(x_labels)+3, len(x_labels)+3))
    im = ax.imshow(c_m, cmap = my_cmap) 
    
    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(cm.max())/2.
        
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(y_labels)))
    ax.set_yticks(np.arange(len(x_labels)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(y_labels, fontsize = 20)
    ax.set_yticklabels(x_labels, fontsize = 20)
    # create a white grid
    #ax.set_xticks(np.arange(cm.shape[1]+1)-.5, minor=True)
    #ax.set_yticks(np.arange(cm.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    #ax.tick_params(which="minor", bottom=False, left=False)
    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")#ha=right
    
    if show_text:
        for i in range(len(x_labels)):
            for j in range(len(y_labels)):
                if c_m[i,j] > 0.01:
                    #kw.update(color=textcolors[int(im.norm(c_m[i, j]) > threshold)])
                    ax.text(j, i, valfmt(c_m[i, j]), ha="center", va="center", fontsize=20, \
                            color=textcolors[int(im.norm(c_m[i, j]) > threshold)])
    
    #ax.set_title("Normalized Confusion Matrix")
    fig.tight_layout()
    plt.xlabel('Predicted Labels', fontsize=20)
    plt.ylabel('True Labels', fontsize=20)
    if plt_clrbar:
        sm = plt.cm.ScalarMappable(cmap=my_cmap, norm=plt.Normalize(vmin=0, vmax=1))
        sm._A = []
        plt.colorbar(sm)
    plt.show() 
    return fig     
#%
plot_confusion_matrix(ddl, x_labels=label, y_labels=label, normalize = False, 
                      show_text = True, my_cmap = 'BuPu', plt_clrbar=False, valfmt="{x:.2f}")
