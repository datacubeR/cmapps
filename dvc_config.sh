rm -f dvc.yaml

dvc run --no-exec -n featurize \
-d src/01-featurize.py \
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
-d src/03-evaluate.py \
-o assets/images \
-M assets/test_metrics.json \
python src/03-evaluate.py