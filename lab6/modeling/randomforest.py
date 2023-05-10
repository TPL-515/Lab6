from dagster import asset, get_dagster_logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from lab6.crud.sqlite import read_data
import pandas as pd
import numpy as np
from joblib import dump, load

# Get our Logger
logger = get_dagster_logger()


@asset(description="This allows the user to train a model and choose what to name it.")
def train(read_data):
    
    logger.info('begin training a new model')
    labels = np.array(read_data['label'])
    features = np.array(read_data[['feature1', 'feature2']])

    rfmodel = RandomForestClassifier(n_estimators=10)
    rfmodel.fit(features, labels)
    dump(rfmodel, 'rfmodel1.joblib')

@asset(description="This allows the user to make a prediction on the data using the existing model")
def predict(read_data):

    logger.info('making predictions on data')
    labels = np.array(read_data['label'])
    features = np.array(read_data[['feature1', 'feature2']])

    rfmodel = load('rfmodel1.joblib')
    preds = rfmodel.predict(features)
    acc = accuracy_score(labels, preds)
    print(acc)
    return