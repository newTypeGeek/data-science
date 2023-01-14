import pandas as pd
import numpy as np

data = {
    'col_1': [1, 2, 3, 4],
    'col_2': [5, 6, np.nan, 8],
    'col_3': [np.inf, 10, 11, 12],
    'col_4': [True, False, False, None]
}

df = pd.DataFrame(data)
print(df)


# np.nan and None are written as empty string
with open("data_nan_as_empty.csv", "w") as f:
    df.to_csv(f, index=False)


# np.nan and None are written as NaN indicated by na_rep field
with open("data_nan_as_NaN.csv", "w") as f:
    df.to_csv(f, index=False, na_rep='NaN')
