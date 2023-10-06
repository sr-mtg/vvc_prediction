from VCA_data_frame import X
print(X.corr())

import matplotlib.pyplot as plt

#Plot the Pearson correlation matrix
plt.imshow(X.corr(), cmap="Blues")
plt.xticks(range(X.shape[1]), X.columns, fontsize=14, rotation=45)
plt.yticks(range(X.shape[1]), X.columns, fontsize=14)
plt.colorbar()
plt.show()