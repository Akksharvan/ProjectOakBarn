import pandas
from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split

data = pandas.read_csv('/Users/akksharvan/workspace/Project-Oak-Barn/Version 1/data/27519.csv')
parameters = ['beds', 'full_bath', 'living_area_above_ground', 'living_area', 'year_built']

X = data[parameters]
y = data["sold_price_per_sq_ft"]

X_train, X_valid, y_train, y_valid = train_test_split(X, y)

my_model = XGBRegressor(n_estimators = 1000, learning_rate = 0.05)
my_model.fit(X_train, y_train, early_stopping_rounds = 5, eval_set=[(X_valid, y_valid)], verbose=False)

my_model.save_model('/Users/akksharvan/workspace/Project-Oak-Barn/Version 1/models/xgb_model.model')