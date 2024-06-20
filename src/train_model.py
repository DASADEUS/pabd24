import argparse
import logging
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from joblib import dump

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/train_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

TRAIN_DATA = 'data/proc/train.csv'
MODEL_SAVE_PATH = 'models/my_model_regression_v01.joblib'


def main(args):
    df_train = pd.read_csv(TRAIN_DATA)
    x_train = df_train[['total_meters']]
    y_train = df_train['price']

    model = RandomForestRegressor(
        n_estimators=500,  # Количество деревьев
        max_depth=10,      # Максимальная глубина деревьев
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1          # Параллельное выполнение
    )

    model.fit(x_train, y_train)
    dump(model, args.model)
    logger.info(f'Saved model to {args.model}')

    r2 = model.score(x_train, y_train)
    logger.info(f'R2 = {r2:.3f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='Model save path',
                        default=MODEL_SAVE_PATH)
    args = parser.parse_args()
    main(args)