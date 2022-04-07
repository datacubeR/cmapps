import pandas as pd
from config import Config
import yaml
from utils import add_rul

with open('params.yaml') as f:
    params = yaml.safe_load(f)['featurize']

#======================================================
# Importing files
#======================================================

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

col_names = params['index_names'] + params['setting_names'] + params['sensor_names']

df_train = pd.read_csv(Config.TRAIN_FILE, sep = '\s+', header = None, names = col_names)
df_test = pd.read_csv(Config.TEST_FILE, sep = '\s+', header = None, names = col_names)
rul_test = pd.read_csv(Config.RUL_FILE, sep = '\s+', header = None, names = ['rul'])


#======================================================
# Defining features
#======================================================

to_keep = params['to_keep']
df_train = add_rul(df_train)
train_features = df_train[to_keep]
train_labels = df_train.rul.clip(upper = params['rul_clip'])

test_features = df_test.groupby('unit_nr').last()[to_keep]
test_labels = rul_test

#======================================================
# Export Files
#======================================================

train_features.to_csv(Config.FEATURES_PATH / 'train_features.csv', index = None)
train_labels.to_csv(Config.FEATURES_PATH / 'train_labels.csv', index = None)

test_features.to_csv(Config.FEATURES_PATH / 'test_features.csv', index = None)
test_labels.to_csv(Config.FEATURES_PATH / 'test_labels.csv', index = None)


