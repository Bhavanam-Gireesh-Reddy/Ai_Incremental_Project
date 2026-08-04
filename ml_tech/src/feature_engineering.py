import pandas as pd
import numpy as np
import os
 
class FeatureEngineering:
 
    def save_df(self, df, filename):
        df.to_csv(f"ml_tech/reports/{filename}", index=False)
 
    def create_features(self, df):
 
        df["BalanceSalaryRatio"] = (
            df["Balance"] /
            (df["EstimatedSalary"] + 1)
        )
 
 
        df["CreditScoreAgeRatio"] = (
            df["CreditScore"] /
            (df["Age"] + 1)
        )
 
 
        df["ProductsPerTenure"] = (
            df["NumOfProducts"] /
            (df["Tenure"] + 1)
        )
 
 
        return df
 
    def remove_correlated_features(
        self,
        df,
        threshold=0.90
    ):
 
        numeric_df = df.select_dtypes(
            include=["int64", "float64"]
        )
 
        corr_matrix = numeric_df.corr().abs()
 
        upper_triangle = corr_matrix.where(
            np.triu(
                np.ones(corr_matrix.shape),
                k=1
            ).astype(bool)
        )
 
        columns_to_drop = [
            column
            for column in upper_triangle.columns
            if any(upper_triangle[column] > threshold)
        ]
 
        df = df.drop(columns=columns_to_drop)
 
 
        df.to_csv("ml_tech/reports/updated_df.csv", index=False)
 
        return df