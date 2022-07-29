rm -f dvc.yaml

dvc run --no-exec -n featurize \
-d src/01-featurize.py \
-d src/utils.py \
-p import,featurize \
-o assets/features \
python src/01-featurize.py

dvc run --no-exec -n train \
-d src/02-train.py \
-d assets/features \
-p train \
-o assets/models \
-M assets/val_metrics.json \
python src/02-train.py

dvc run --no-exec -n evaluate \
-d assets/features \
-d assets/models \
-d src/utils.py \
-d src/03-evaluate.py \
-M assets/test_metrics.json \
python src/03-evaluate.py