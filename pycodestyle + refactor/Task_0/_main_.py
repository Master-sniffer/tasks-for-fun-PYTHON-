import numpy as np
import pandas as pd
import datetime
import data_examples
import feature_engineering
import pipeline


if __name__ == '__main__':
    print(pipeline.predict_cao(
        data_examples.CHARGE_CHEMISTRY,
        data_examples.LIMESTONE_CONSUMPTIONS,
        data_examples.CHARGE_CONSUMPTIONS,
        data_examples.COKE_CONSUMPTIONS,
        data_examples.COKE_SIEVING,
        data_examples.LIMESTONE_CAO))
