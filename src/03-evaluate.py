import json

import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
from utils import plot_oof
from config import Config

Config.IMAGE_PATH.mkdir(parents=True, exist_ok=True)

X_test = pd.read_csv(Config.FEATURES_PATH / 'test_features.csv')
y_test = pd.read_csv(Config.FEATURES_PATH / 'test_labels.csv')

model = joblib.load(Config.MODELS_PATH / 'model.joblib')
y_pred = model.predict(X_test)

#======================================================
# Metrics
#======================================================

test_metrics = dict(test = dict(test_mae = mean_absolute_error(y_test, y_pred),
                                test_rmse = mean_squared_error(y_test, y_pred, squared=False),
                                test_r2 = r2_score(y_test, y_pred))
                    )

with open(Config.TEST_METRICS_PATH, 'w') as outfile:
    json.dump(test_metrics, outfile)
    
#======================================================
# Other Evaluation Curves
#======================================================

plot_oof(y_test, y_pred, s = 10, path = Config.IMAGE_PATH / 'F_vs_t.png')

