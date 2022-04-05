from config import Config

#======================================================
# create folder structure
#======================================================

Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)
Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)
