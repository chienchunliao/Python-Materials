# -*- coding: utf-8 -*-
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
import pandas as pd
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('winequality-red.csv')
df = df.iloc[:,1:]
x = df.drop('quality', axis=1)
y = df['quality']

model = LogisticRegression()

#%% Forward Selection: forward=True, floating=False
'''
estimator: sklearn model
k_features: 1. n ----> select n features from current features
           2. (min, max) ------> 在 min & max 間選performance最好的k個features的model
scoring: 1. {'accuracy'(default), 'f1', 'precision', 'recall', 'roc_auc'} for classifiers
         2. {'r2'(default), 'mean_absolute_error', 'mean_squared_error'/'neg_mean_squared_error', 'median_absolute_error'} for regressors
cv: numbers of fold used in cross-validation
n_jobs: numbers of processors to used. -1: use all processors

'''
## select 4 features
sfs = SFS(estimator=model,
          k_features = 4,
          forward=True, 
          floating=False, 
          scoring='f1',
          cv=0,
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)

## select best k feature between 2 to 10
sfs = SFS(estimator=model,
          k_features = (2,10),
          forward=True, 
          floating=False, 
          scoring='f1',
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)


#%% Backward Selection: forward=False, floating=False
sfs = SFS(estimator=model,
          k_features = 4,
          forward=False, 
          floating=False, 
          scoring='f1',
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)

## select best k feature between 2 to 10
sfs = SFS(estimator=model,
          k_features = (2,10),
          forward=False, 
          floating=False, 
          scoring='f1',
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)

#%% Stepwise Selection: forward=True, floating=True
sfs = SFS(estimator=model,
          k_features = 4,
          forward=True, 
          floating=True, 
          scoring='f1',
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)

## select best k feature between 2 to 10
sfs = SFS(estimator=model,
          k_features = (2,10),
          forward=True, 
          floating=True, 
          scoring='f1',
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
## print out what features are selected
#print(sfs.k_feature_names_)

#%% Create AIC & BIC for feature selection
from sklearn.metrics import make_scorer
from sklearn.metrics import log_loss
def aic_formula(y_true, y_pred, n_feature):
    aic = 2*n_feature - 2*log_loss(y_true, y_pred)
    return aic
AIC = make_scorer(aic_formula, 
                  greater_is_better=False,
                  needs_proba=True, 
                  n_feature=4)
sfs = SFS(estimator=model,
          k_features = (2,10),
          forward=True, 
          floating=True, 
          scoring=AIC,
          cv=0, 
          n_jobs=1)
sfs.fit(x,y)
print(sfs.k_feature_names_)
    
