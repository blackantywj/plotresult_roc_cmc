import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as sm
a = np.loadtxt('tpr.csv', dtype=np.float64)
b = np.loadtxt('fpr.csv', dtype=np.float64)
roc_auc = sm.auc(b, a)

plt.plot(b, a, 'b', label='AIAF+AFW = %0.4f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
print(a)
print(b)
plt.show()
