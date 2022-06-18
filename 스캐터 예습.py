import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'],
            alpha=0.4, s=100 * df['petal width (cm)'], c=df['target'],
            cmap=plt.cm.get_cmap('prism', df['target'].nunique()), edgecolors='black')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
cb = plt.colorbar(label='species')
cb.set_ticks([0, 1, 2])
cb.set_ticklabels(["setosa", "versicolor", "virginica"])
plt.show()