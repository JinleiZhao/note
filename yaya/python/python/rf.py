



from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(random_state=RSEED)
tree.fit(x,y)

print(f'Model Accuracy:{tree.score(x,y)}')


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, 
                               bootstrap = True,
                               max_features = 'sqrt')
# Fit on training data
model.fit(train, train_labels)

#actual class predictions
rf_predictions = model.predict(test)
# Probabilities for each class
rf_probs = model.predict_proba(test)[:, 1]


from sklearn.metrics import roc_auc_score
# Calculate roc auc
roc_value = roc_auc_score(test_labels, rf_probs)

#特征重要性
import pandas as pd
# Extract feature importances
fi = pd.DataFrame({'feature': list(train.columns),
                   'importance': model.feature_importances_}).\
                    sort_values('importance', ascending = False)
