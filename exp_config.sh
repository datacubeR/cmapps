dvc exp run --queue -S train.rul_clip=125
dvc exp run --queue -S train.rul_clip=120
dvc exp run --queue -S train.rul_clip=90
dvc exp run --queue -S train.rul_clip=70
dvc exp run --queue -S train.rul_clip=50
dvc exp run --queue -S train.rul_clip=30
dvc exp run --queue -S train.rul_clip=10

dvc exp run --run-all

# echo "## Resultados del Experimento" > report.md
# dvc exp show --only-changed --drop 'assets|src' --no-pager --md > report.md