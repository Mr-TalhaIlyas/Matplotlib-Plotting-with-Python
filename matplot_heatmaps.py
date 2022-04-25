def plot_confusion_matrix(cm, x_labels, y_labels, normalize = True, show_text = True, \
                          my_cmap = 'Greens', threshold=None, textcolors=("black", "white"),
                          plt_clrbar=True, valfmt="{x:.2f}", **textkw):
    '''
    Parameters
    ----------
    cm : a nxn dim numpy array.
    class_names: a list of class names (str type)
    normalize: whether to normalize the values
    show_text: whether to show value in each block of the matrix, If matrix is large like 10x10 or 20x20 it's better to set it to false
               because it'll be difficult to read values but you can see the network behaviour via color map.
    show_fpfn: whether to show false positives on GT axis and false negatives on Pred axis. FN -> not detected & FP -> wrong detections
    Returns
    -------
    fig: a plot of confusion matrix along with colorbar
    '''
    
    conf_mat = cm

    
    
    c_m = conf_mat
    
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
                    text = ax.text(j, i, valfmt(c_m[i, j]), ha="center", va="center", \
                                   color=textcolors[int(im.norm(c_m[i, j]) > threshold)], fontsize=20)
    
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
