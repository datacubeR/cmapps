dvc exp run --queue -S featurize.lags=[1,2,3,4,5]
dvc exp run --queue -S featurize.lags=[1,2,3,4,5,6,7,8,9]
dvc exp run --queue -S featurize.lags=[1,2,3,4,5,10,20,30]
dvc exp run --queue -S featurize.lags=[1,2,3,4,5,10,20]
dvc exp run --queue -S featurize.lags=[1,3,6,9,12,15]


dvc exp run --run-all

echo "## Resultados del Experimento" > report.md
dvc exp show --only-changed --drop 'assets|src' --no-pager --md > report.md