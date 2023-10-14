#print(x.loc['mean', ['sepal length (cm)','target']])
#print(x.iloc[3])
#print(corr_matr.iloc[:,2])

import pandas as pd
import numpy  as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin
import scipy.stats

iris = load_iris()

iris_pd=pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

iris_pd = iris_pd.rename(columns={'sepal length (cm)': 'sl', 'sepal width (cm)': 'sw', 'petal length (cm)': 'pl', 'petal width (cm)': 'pw'})
#print(iris_pd)
#print(iris_pd['sepal length (cm)'])

print(iris_pd)
print(iris_pd.describe())

corr_matr = iris_pd.corr()
print(corr_matr)
pcorr_matr = iris_pd.pcorr()
print(pcorr_matr)

kstest_res = [ scipy.stats.kstest(iris_pd.iloc[:,i], 'norm') for i in range(len(iris_pd.iloc[0]))]
for elem in kstest_res:
    print(f'Значение статистики: {elem.statistic}, pvalue: {elem.pvalue}')



iris_pd.boxplot()
plt.show()
sns.heatmap(corr_matr, annot= True, vmin=-1, vmax=1)
plt.show()
sns.heatmap(pcorr_matr, annot= True, vmin=-1, vmax=1)
plt.show()


iris_pd.iloc[:,:-1].hist()
plt.show()