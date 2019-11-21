
#导入数据
import pandas
patients = pandas.read_csv("sj.csv")
patients.head(5)


#切分训练集测试集
from sklearn.model_selection import train_test_split
patients_data=patients.loc[:,'distance':'proportion']
patients_target=patients.loc[:,'warning']
data_train,data_test,target_train,target_test=train_test_split(patients_data,patients_target,test_size=0.1,random_state=42)


#找到最有用的几个属性
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
predictors = ["distance", "duration", "total_time", "outdoor", "angle", "proportion"]

selector = SelectKBest(f_classif, k=5)
selector.fit(data_train, target_train)

scores = -np.log10(selector.pvalues_)

plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()


#根据上面的代码更改属性
predictors_best = ["distance", "total_time", "angle", "proportion"]
data_train = data_train[predictors_best]
data_test = data_test[predictors_best]


#参数组合遍历找最优
from sklearn.model_selection import GridSearchCV
tree_param_grid = { 'min_samples_split': list((2,3,4)),'n_estimators':list((3,5,10,15,20,25,30,35,40,45,50))}
grid = GridSearchCV(RandomForestClassifier(),param_grid=tree_param_grid, cv=kf)#(算法，调节参数（用字典形式），交叉验证次数)
grid.fit(data_train, target_train)#训练集
grid.cv_results_ , grid.best_params_, grid.best_score_#得分，最优参数，最优得分


#随机森林
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=1, n_estimators=35, min_samples_split=2, min_samples_leaf=2)
#交叉验证
kf = model_selection.KFold(n_splits=3)
scores = model_selection.cross_val_score(rf, data_train, target_train, cv=kf)
print(scores.mean())
