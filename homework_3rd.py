import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(211)

ax1.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax1.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax1.set_xlim(0.0, 4.5)
plt.title('ax1')
ax2 = fig.add_subplot(212)
t = np.arange(0., 5., 0.2)
ax2.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
plt.title('ax2')

plt.suptitle('HW')
plt.show()
