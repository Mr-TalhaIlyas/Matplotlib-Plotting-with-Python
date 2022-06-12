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
       

    return None#f

def figure_to_array(fig):
    """
    convert matplot figure to array
    shape: height, width, layer
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer._renderer)
