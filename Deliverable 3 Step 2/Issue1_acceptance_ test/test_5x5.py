import numpy as np
import matplotlib.pyplot as plt

plt.figure()
for i in range(25):
    ax= plt.subplot(5,5 ,i+1)
    im=ax.imshow(np.random.normal(size=100).reshape([10,10]))
    plt.tight_layout()
    plt.title(i)
plt.savefig('imshow_5x5.png')