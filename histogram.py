nb_bins = 256
count_r = np.zeros(nb_bins)
count_g = np.zeros(nb_bins)
count_b = np.zeros(nb_bins)

root = './'
for image in os.listdir(root):  
  if image.endswith('.jpeg'):
    x = io.imread(root+image)
    hist_r = np.histogram(x[0], bins=nb_bins, range=[0, 255])
    hist_g = np.histogram(x[1], bins=nb_bins, range=[0, 255])
    hist_b = np.histogram(x[2], bins=nb_bins, range=[0, 255])
    count_r += hist_r[0]
    count_g += hist_g[0]
    count_b += hist_b[0]

bins = hist_r[1]
fig = plt.figure()
plt.bar(bins[:-1], count_r, color='r', alpha=0.33)
plt.bar(bins[:-1], count_g, color='g', alpha=0.33)
plt.bar(bins[:-1], count_b, color='b', alpha=0.33)
