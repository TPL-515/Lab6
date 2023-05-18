from dagster import asset, get_dagster_logger, Output
from sklearn.metrics import accuracy_score
from lab6.models.randomforest import train, predict
from lab6.assets.dataingest import pull_data
import pandas as pd
import numpy as np

# Get our Logger
logger = get_dagster_logger()

##########################################################
################# Insert Code Below ######################
##########################################################