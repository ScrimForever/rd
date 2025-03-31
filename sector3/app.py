import numpy as np
import pandas as pd

def lambda_handler(event, context):
    array = np.array([1, 2, 3])
    df = pd.DataFrame({'numbers': array})
    return {
        "statusCode": 200,
        "body": df.to_json()
    }
