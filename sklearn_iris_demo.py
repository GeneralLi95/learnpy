# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause
#以上为官方作者信息

#iris鸢尾花数据集包含3个不同品种的鸢尾花（Setosa，Versicolour，and Virginica）数据，花瓣和萼片长度，存储在一个150*4的 numpy.ndarry中
#150行4列，150行指150多花，4列分别是Sepal Length，Sepal Width, Petal Length and Petal Width
#sklearn 官方demo

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   #
from sklearn import datasets
from sklearn.decomposition import PCA  #PCA 主成分分析

#导入数据
iris = datasets.load_iris()
X = iris.data[:,:2]  #指选择第一个和第三个特征作为输入
y = iris.target   # 输出

x_min,x_max = X[:,0].min()-.5, X[:,0].max()+.5
y_min,y_max = X[:,1].min()-.5, X[:,1].max()+.5

plt.figure(2,figsize=(8,6))
plt.clf()

#绘制训练点
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.Set1,edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')#以花瓣长度和宽度为横纵坐标绘制一个图

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

#为了更好了解维度关系
#绘制一个3维的PCA
fig = plt.figure(1,figsize=(8,6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0],X_reduced[:, 1], X_reduced[:, 2],c=y, cmap=plt.cm.Set1, edgecolor='k', s=40)


ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2ed eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])


plt.show()