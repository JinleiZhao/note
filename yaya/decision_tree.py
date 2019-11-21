#coding=utf-8
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz
from matplotlib.pylab import plt
import os
import shutil
import seaborn as sb
from sklearn.datasets import load_iris

df = pd.read_excel('data.xlsx', header=None)
df.columns = ['back','body','face','eye','mouth','nosePer','class']
#df.rename(columns={0:'back', 1:'body',2:'face', 3:'eye',
#                   4:'mouth', 5:'nosePer', 6:'class'}, inplace = True)
#df_isdata = DataFrame(df.iloc[:,0:-1])
'''
sb.pairplot(df
            ,diag_kind = 'kde'
            ,vars = df.columns[:6]
            ,hue = 'class')
plt.savefig('result/pairpots.png')
#plt.show()
plt.close()
plt.figure(figsize=(10,10))
for index, columns in enumerate(df.columns):
    if columns == 'class':
        continue
    plt.subplot(2, 3, index+1)
    sb.violinplot(x='class', y = columns, data=df)
#plt.show()
plt.savefig('result/pinao.png')
plt.close()
'''
df_data=df.iloc[:,0:-1].values
df_target = df.iloc[:,-1].values

'''
from sklearn.datasets import  load_wine
wine = load_wine()
#data = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)],axis=1)
df_data = wine.data
df_target = wine.target
'''
Xtrain, Xtest, Ytrain, Ytest = train_test_split(df_data, df_target, test_size=0.3)

dir_name = 'random_data'
if not os.path.isdir(dir_name):
    os.makedirs(dir_name)
    try:
        for i,data in enumerate((Xtrain, Xtest, Ytrain, Ytest)):
            file_name = os.path.join(dir_name,str(i) + '.txt')
            f_ = open(file_name, 'w')
            f_.close()
            if i >=2:
                np.savetxt(file_name,data, fmt='%d')
            else:
                np.savetxt(file_name,data)
    except Exception as e:
        print(e)
        shutil.rmtree(dir_name)
else:
    print('here!!!')
    Xtrain, Xtest, Ytrain, Ytest = [np.loadtxt(os.path.join(dir_name, str(i)+'.txt')) for i in range(4)]

result = []
# for i in range(15,20):
#    test = []
#     for j in range(1,15):
clf = tree.DecisionTreeClassifier(random_state=60
                                 ,min_samples_leaf=1
                                 ,min_samples_split=2
                                 #,max_features=3
                                 ,max_depth=4
                                 ,criterion='gini'
                                 )
clf = clf.fit(Xtrain,Ytrain)
sco = clf.score(Xtest,Ytest)
    # result.append(sco)
#    test.append(sco)
#     result.append(test)
# for i,test in enumerate(result):
#     plt.plot(range(1,15),test, label='max_depth=%s'%(i+1))
# plt.plot(range(15,20), result)
# plt.legend()
# plt.xlabel('min_samples_leaf')
# plt.savefig('result/choice.png')
# plt.show()
# plt.close()

feature_name = ['time','background','body','eye','lefteye','righteye','face','mouth','nose']
dot_data  = tree.export_graphviz(clf
                                 ,feature_names=feature_name
                                 ,class_names=['正常儿童','自闭症儿童']
                                 #,class_names= ['0','1','2']
                                 ,filled=True
                                 ,rounded=True
                                 )
graph = graphviz.Source(dot_data.replace('helvetica','"Microsoft YaHei"'))
graph.render(filename='decision', directory='result_random', format='png', cleanup=True, quiet=True) #保存
#graph.view(filename='result',cleanup=True,quiet=True)

eigenvalue = list(zip(feature_name,clf.feature_importances_))
eigenvalue = sorted(eigenvalue, key=lambda x:x[1], reverse=True)
value_label = list(zip(*eigenvalue))
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体为黑体
plt.title('准确率-%s'%sco)
r = plt.bar(range(len(eigenvalue)), value_label[1], color='rgb',tick_label=value_label[0])
totol_eigenvalue = 0
for i,value in zip(r, value_label[1]):
    totol_eigenvalue += value
    plt.text(i.get_xy()[0]+i.get_width()/2, i.get_height() + 1/pow(10, len(str(value).split('.')[-1]))/10, '%s'%value, ha='center')
plt.legend()
plt.savefig('result_random/eigenvalueSort.png')
plt.close()
#plt.show()