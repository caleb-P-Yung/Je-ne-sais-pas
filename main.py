import tensorflow as tf
import numpy as np
import pandas as pd

titanic = pd.read_csv("data/test.csv")
print(titanic.iloc[9])