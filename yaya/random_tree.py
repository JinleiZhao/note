from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
import os
import shutil
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import time

wine = load_wine()

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

df = pd.read_excel('随机森林数据.xlsx') #, header=None
df.columns = ['time','background','body','eye','lefteye','righteye','face','mouth','nose','class']

df_data=df.iloc[:,0:-1].values
df_target = df.iloc[:,-1].values

dir_name = 'random_data'
if not os.path.isdir(dir_name):
    os.makedirs(dir_name)
    try:
        Xtrain, Xtest, Ytrain, Ytest = train_test_split(df_data, df_target, test_size=.3)
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
    Xtrain, Xtest, Ytrain, Ytest = [np.loadtxt(os.path.join(dir_name, str(i)+'.txt')) for i in range(4)]

#决策树和随机森林的结果比对
'''
rfc_l = []
clf_l = []
for i in range(10):
    rfc = RandomForestClassifier()
    rfc_s = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    rfc_l.append(rfc_s)
    clf = DecisionTreeClassifier()
    clf_s = cross_val_score(clf, Xtrain, Ytrain, cv=10).mean()
    clf_l.append(clf_s)
plt.plot(range(1,11), rfc_l, label='random')
plt.plot(range(1,11), clf_l, label='desic')
plt.legend()
plt.savefig('result_random/random_desic_cmp.png')
plt.show()
plt.close()
'''
#random_status 决策树随机选项
'''
super_s = []
for i in range(200):
    rfc = RandomForestClassifier(random_state=i+1)
    rfc_s = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    super_s.append(rfc_s)
print(max(super_s), super_s.index(max(super_s))+1)
plt.figure(figsize=(20,5))
plt.plot(range(1,201), super_s)
plt.savefig('result_random/random_random_status.png')
plt.show()
plt.close()
#0.9400000000000001 60
'''

#n_estimators 随机森林树的数量
'''
super_s = []
for i in range(200):
    rfc = RandomForestClassifier(n_estimators=i+1, n_jobs=-1, random_state=60)
    rfc_s = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    super_s.append(rfc_s)
print(max(super_s), super_s.index(max(super_s))+1)
plt.figure(figsize=(20,5))
plt.plot(range(1,201), super_s)
plt.savefig('result_random/random_super_n_estimators.png')
plt.show()
plt.close()
#0.9400000000000001 10
'''

score_l = []

# rfc = RandomForestClassifier()
# # rfc_cvs = cross_val_score(rfc, df_data, df_target, cv=10).mean()
# # print('result before', rfc_cvs)

#max_depth
'''
for i in range(1, 15):
    rfc = RandomForestClassifier(n_estimators=10
                                 ,n_jobs=-1
                                 ,random_state=60
                                 ,max_depth=i
                                 )
    rfc_cvs = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    score_l.append(rfc_cvs)
print(max(score_l), score_l.index(max(score_l))+1)
plt.figure(figsize=(20,5))
plt.plot(range(1,15), score_l)
plt.savefig('result_random/data_max_depth.png')
plt.show()
plt.close()
#0.9400000000000001 4  若加上max_deth参数准确率降低 图像在左边
'''

#min_samples_leaf
'''
param_grid = {"min_samples_leaf":np.arange(1,20,1)}
rfc = RandomForestClassifier(n_estimators=178,
                             random_state=136,
                             n_jobs=-1)
gs = GridSearchCV(rfc, param_grid, cv=10)
gs.fit(df_data, df_target)
print(gs.best_params_)
print(gs.best_score_)
#0.7743055555555556  1

#use plt
for i in range(1, 21):
    rfc = RandomForestClassifier(n_estimators=10
                                 ,n_jobs=-1
                                 ,random_state=60
                                 ,min_samples_leaf=i
                                 ,max_depth=4
                                 )
    rfc_cvs = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    score_l.append(rfc_cvs)
print(max(score_l), score_l.index(max(score_l))+1)
plt.figure(figsize=(20,5))
plt.plot(range(1,21), score_l)
plt.savefig('result_random/min_samples_leaf.png')
plt.show()
plt.close()
#0.9400000000000001 1
'''
#min_samples_split
'''
param_grid = {"min_samples_split":np.arange(2,10,1)}
rfc = RandomForestClassifier(n_estimators=178,
                             random_state=136,
                             n_jobs=-1,
                             min_samples_leaf=1
                             )
gs = GridSearchCV(rfc, param_grid, cv=10)
gs.fit(df_data, df_target)
print(gs.best_params_)
print(gs.best_score_)
#0.75 19
#0.7743055555555556  2

#use plt
for i in range(2, 31):
    rfc = RandomForestClassifier(n_estimators=10
                                 ,n_jobs=-1
                                 ,random_state=60
                                 ,min_samples_leaf=1
                                 ,min_samples_split=i
                                 ,max_depth=4
                                 )
    rfc_cvs = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    score_l.append(rfc_cvs)
print(max(score_l), score_l.index(max(score_l))+2)
plt.figure(figsize=(20,5))
plt.plot(range(2,31), score_l)
plt.savefig('result_random/min_samples_split.png')
plt.show()
plt.close()
#0.9400000000000001 2
'''
#max_features
'''
param_grid = {"max_features":np.arange(1,6,1)}
rfc = RandomForestClassifier(n_estimators=178,
                             random_state=136,
                             n_jobs=-1,
                             min_samples_leaf=1,
                             min_samples_split=2,
                             )
gs = GridSearchCV(rfc, param_grid, cv=10)
gs.fit(df_data, df_target)
print(gs.best_params_)
print(gs.best_score_)
#0.7743055555555556  2

#use plt
for i in range(1, 8):
    rfc = RandomForestClassifier(n_estimators=10
                                 ,n_jobs=-1
                                 ,random_state=60
                                 ,min_samples_leaf=1
                                 ,min_samples_split=2
                                 ,max_features=i
                                 ,max_depth=4
                                 )
    rfc_cvs = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    score_l.append(rfc_cvs)
print(max(score_l), score_l.index(max(score_l))+1)
plt.figure(figsize=(20,5))
plt.plot(range(1,8), score_l)
plt.savefig('result_random/max_features.png')
plt.show()
plt.close()
#0.9400000000000001 3
'''
#criterion
'''
param_grid = {"criterion":['gini','entropy']}
rfc = RandomForestClassifier(n_estimators=54,
                             random_state=173,
                             n_jobs=-1,
                             min_samples_leaf=1,
                             min_samples_split=2,
                             max_features=3,
                             max_depth=6
                             )
gs = GridSearchCV(rfc, param_grid, cv=10)
gs.fit(df_data, df_target)
print(gs.best_params_)
print(gs.best_score_)
#0.7743055555555556 gini
'''
#use plt
for i in ['gini','entropy']:
    rfc = RandomForestClassifier(n_estimators=10
                                 ,n_jobs=-1
                                 ,random_state=60
                                 ,min_samples_leaf=1
                                 ,min_samples_split=2
                                 ,max_features=3
                                 ,max_depth=4
                                 #,criterion='gini'
                                 ,criterion=i
                                 )
    rfc_cvs = cross_val_score(rfc, Xtrain, Ytrain, cv=10).mean()
    score_l.append(round(rfc_cvs,2))
print(max(score_l), ['gini','entropy'][score_l.index(max(score_l))], score_l)
# plt.figure(figsize=(20,5))
# plt.plot(['gini','entropy'], score_l)
# plt.savefig('result_random/criterion.png')
# plt.show()
# plt.close()
#0.9100000000000001 gini
sr = zip(['gini','entropy'],score_l)
sr = list(zip(*sr))
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置字体为黑体
plt.title('gini&entropy')
r = plt.bar(range(2), sr[1], color='rgb',tick_label=sr[0],width=0.2)
for i,value in zip(r, sr[1]):
    plt.text(i.get_xy()[0]+i.get_width()/2, i.get_height() + 1/pow(10, len(str(value).split('.')[-1]))/10, '%s'%value, ha='center')
plt.legend()
plt.savefig('result_random/criterion.png')
plt.close()

rfc = RandomForestClassifier(n_estimators=10
                             ,n_jobs=-1
                             ,random_state=60
                             ,min_samples_leaf=1
                             ,min_samples_split=2
                             ,max_features=3
                             ,max_depth=4
                             ,criterion='gini'
                             )
#sco = cross_val_score(rfc, Xtest, Ytest, cv=10).mean()
# print(rfc)
rfc_c = rfc.fit(Xtrain, Ytrain)
sco = rfc.score(Xtest, Ytest)
print(rfc_c.feature_importances_)
feature_names = ['time','background','body','eye','lefteye','righteye','face','mouth','nose']
eigenvalue = list(zip(feature_names,rfc_c.feature_importances_))
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
plt.savefig('result_random/eigenvalueSort_random.png')
plt.close()

