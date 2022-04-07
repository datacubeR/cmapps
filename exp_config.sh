dvc exp run --queue -S featurize.rul_clip=120
dvc exp run --queue -S featurize.rul_clip=90
dvc exp run --queue -S featurize.rul_clip=70
dvc exp run --queue -S featurize.rul_clip=50
dvc exp run --queue -S featurize.rul_clip=30
dvc exp run --queue -S featurize.rul_clip=10

dvc exp run --run-all