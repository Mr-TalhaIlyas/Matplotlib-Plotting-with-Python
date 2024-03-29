import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
# for magic line control form spyder or vs code instead of jupyter
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')
# turn on or off the interactive plotting
plt.ion()

def save_plots(epoch, dr_loss, df_loss, dr_acc, df_acc, g_loss, x):

    #f, axe = plt.subplots(figsize = (5,3))
    f, axs = plt.subplots(3, 1, figsize = (6,3))
    axs[0].plot(x, dr_loss, 'b', label='d-real')
    axs[0].plot(x, df_loss, 'g-.', label='d-fake')
    axs[0].get_xaxis().set_visible(False)
    axs[0].legend()
    # # plot discriminator accuracy
    axs[1].plot(x, dr_acc, 'r', label='acc-real')
    axs[1].plot(x, df_acc, 'c-.', label='acc-fake')
    axs[1].get_xaxis().set_visible(False)
    axs[1].legend()

    axs[2].plot(x, g_loss, 'm', label='gen')
    axs[2].legend()

    # save plot to file
    f.savefig(f"/home/user01/data/talha/gan_1/plots/mnist_{epoch}.png")
    plt.show()
    #plt.close()
    # update the plot in same window
    f.canvas.draw()
    f.canvas.flush_events()
        

    return None#f

def figure_to_array(fig):
    """
    convert matplot figure to array
    shape: height, width, layer
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)

def plot_hists(image):
    # trurn off the the interactive plotting
    plt.ioff()

    fig = plt.figure()
    _ = plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    _ = plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    _ = plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    _ = plt.xlabel('Intensity Value')
    _ = plt.ylabel('Count')
    _ = plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.close(fig)
    return figure_to_array(fig)


# def get_barplot(preds, typ):
    
#     if typ == 'g_model':
#         dicts = dict_c
#     elif typ == 't_model':
#         dicts = dict_b
#     y = np.squeeze(preds)
#     x = np.arange(len(y))
    
#     fig = plt.figure()
#     p = sns.barplot(x,y)
#     p.set_xticks(range(len(y)),labels=list(dicts.keys()),  rotation=45, ha="right")
#     plt.ylabel('Score')
#     fig.tight_layout()
#     plt.close(fig)
    
#     fig.canvas.draw()
#     return cv2.resize(np.array(fig.canvas.renderer._renderer), (512,256))

# def get_barplot_s(preds, typ):
    
#     if typ == 'g_model':
#         dicts = dict_sc
#     elif typ == 't_model':
#         dicts = dict_sb
#     y = np.squeeze(preds)
#     x = np.arange(len(y))
    
#     fig = plt.figure()#figsize=(8,4)
#     p = sns.barplot(x,y)
#     p.set_xticks(range(len(y)),labels=list(dicts.keys()),  rotation=45, ha="right")
#     plt.ylabel('Score')
#     fig.tight_layout()
#     plt.close(fig)
    
#     fig.canvas.draw()
#     return cv2.resize(np.array(fig.canvas.renderer._renderer), (256,256))
