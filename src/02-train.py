from config import Config
import pandas as pd

import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import json
import yaml
import logging

log = logging.getLogger("Training")
Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

with open('params.yaml') as f:
    params = yaml.safe_load(f)['train']

train_features = pd.read_csv(Config.FEATURES_PATH / 'train_features.csv')
train_labels = pd.read_csv(Config.FEATURES_PATH / 'train_labels.csv')
print(train_features.shape)
print(train_labels.shape)

if params['standardize']:
    model = Pipeline([('scaler', StandardScaler()),
                    ('model', LinearRegression())])
else:
    model = LinearRegression()

#======================================================
# Validation Metrics
#======================================================
folds = KFold(n_splits=params['n_split'], 
                shuffle=True, 
                random_state=Config.RANDOM_SEED)

mae = np.zeros(params['n_split'])
rmse = np.zeros(params['n_split'])
r2 = np.zeros(params['n_split'])

for fold_, (train_idx, val_idx) in enumerate(folds.split(X = train_features, y = train_labels)):
    log.info(f'Training Fold: {fold_}')
    
    X_train, X_val = train_features.iloc[train_idx], train_features.iloc[val_idx]
    y_train, y_val = train_labels.iloc[train_idx], train_labels.iloc[val_idx]
    
    model.fit(X_train, y_train.clip(upper = params['rul_clip']))
    val_preds = model.predict(X_val)
    val_mae = mean_absolute_error(y_val, val_preds)
    val_rmse = mean_squared_error(y_val, val_preds, squared=False)
    val_r2 = r2_score(y_val, val_preds)
    
    mae[fold_] = val_mae
    rmse[fold_] = val_rmse
    r2[fold_] = val_r2
    log.info(f'Validation MAE for Fold {fold_}: {val_mae}')
    log.info(f'Validation RMSE for Fold {fold_}: {val_rmse}')
    log.info(f'Validation R2 for Fold {fold_}: {val_r2}')


val_metrics = dict(validation = dict(val_mae = mae.mean(), 
                                    val_rmse = rmse.mean(), 
                                    val_r2 = r2.mean())
                    )

log.info('Saving Validation Metrics')
with open(Config.VAL_METRICS_PATH, 'w') as outfile:
    json.dump(val_metrics, outfile)
    
#======================================================
# Retrain Model
#======================================================
log.info('Model Retraining')
model.fit(train_features, train_labels.clip(upper = params['rul_clip']))
joblib.dump(model, Config.MODELS_PATH / params['model_name'])