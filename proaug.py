
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

T=100
# t=0

alpha = 0.2
beta = 0.3
gamma = 0.4 

lamb = 20

x = min(alpha, beta, gamma)
ta = 80

func = lambda alpha, lamb, t: min(alpha, (alpha*t/lamb))
 
a,b,c,i, r = [],[],[],[], []
for t in range(T):
    
    a.append(func(alpha, lamb, t))
    b.append(func(beta, 2*lamb, t))
    c.append(func(gamma, 3*lamb, t))
    
    i.append(1-max(func(alpha, lamb, t),func(beta, 2*lamb, t),func(gamma, 3*lamb, t)))
    r.append((a[t]+b[t]+c[t]))

# plt.figure()
xs = np.arange(T)
plt.plot(xs, np.tile(alpha, T), alpha=0.7, color='lightgray', ls='--')
plt.plot((lamb, lamb), (0.0, 1.0), alpha=0.7, color='lightgray', ls='--')
plt.text(lamb-3, alpha+0.007, r'$\alpha$')
plt.text(lamb-1, -0.04, r'$\lambda$')
plt.plot(a,label='Geometric', ls='--')

plt.plot(xs, np.tile(beta, T), alpha=0.7, color='lightgray', ls='--')
plt.plot((2*lamb, 2*lamb), (0.0, 1.0), alpha=0.7, color='lightgray', ls='--')
plt.text(2*lamb-3, beta+0.007, r'$\beta$')
plt.text(2*lamb-1, -0.04, r'$2 \lambda$')
plt.plot(b, label='Noise', ls='-.')

plt.plot(xs, np.tile(gamma, T), alpha=0.7, color='lightgray', ls='--')
plt.plot((3*lamb, 3*lamb), (0.0, 1.0), alpha=0.7, color='lightgray', ls='--')
plt.text(3*lamb-3, gamma+0.007, r'$\gamma$')
plt.text(3*lamb-1, -0.04, r'$3 \lambda$')
plt.plot(c, label='Collage', ls=':')

# plt.plot(xs, np.tile(alpha, T), alpha=0.7, color='lightgray')
# plt.text(lamb-3, alpha+0.007, r'$\alpha$')
plt.plot(i, label='Identity', ls='-')
