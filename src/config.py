from pathlib import Path

import yaml

with open('params.yaml') as f:
    params = yaml.safe_load(f)

class Config:
    RANDOM_SEED = params['base']['random_seed']
    ASSETS_PATH = Path('assets')
    DATA_PATH = ASSETS_PATH / 'CMAPSSData'
    TRAIN_FILE =  DATA_PATH/ params['import']['train_name']
    TEST_FILE = DATA_PATH / params['import']['test_name']
    RUL_FILE = DATA_PATH / params['import']['rul_name']
    FEATURES_PATH = ASSETS_PATH / 'features'
    MODELS_PATH = ASSETS_PATH / 'models'
    METRICS_PATH = ASSETS_PATH / 'train_metrics.json'
    VAL_METRICS_PATH = ASSETS_PATH / 'val_metrics.json'
    TEST_METRICS_PATH = ASSETS_PATH / 'test_metrics.json'