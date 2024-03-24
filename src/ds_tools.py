import numpy as np
import pandas as pd
import datetime as dt
import numba
import os
import tqdm


class ktools:
    @staticmethod
    def inspect_columns(df):
        result = pd.DataFrame({
            'unique': df.nunique() == len(df),
            'nunique': df.nunique(),
            'null_count': df.isna().sum(),
            'null_pct': round((df.isnull().sum() / len(df)) * 100, 4),
            '1st_row': df.iloc[0],
            'random_row': df.iloc[np.random.randint(low=0, high=len(df))],
            'last_row': df.iloc[-1],
            'dtype': df.dtypes
        })
        return result