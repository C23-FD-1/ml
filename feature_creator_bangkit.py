import numpy as np
import pandas as pd

# pylint: disable= invalid-name
def create(df: pd.DataFrame) -> pd.DataFrame:
    X = df.copy()

    # is kyc user
    X["is_verified"] = X["is_verified"]

    # account lifetime to incidents
    X["trx_date"] = X["trx_date"].astype("datetime64[ns]")
    X["pii_registereddate"] = X["pii_registereddate"].astype("datetime64[ns]")
    X["pii_account_lifetime"] = (
        X["trx_date"] - X["pii_registereddate"]
    ).dt.days

    # if pii_account_lifetime within 2 weeks OK, else None (invalid)
    pii_account_lifetime_conditions = [
        (X["pii_account_lifetime"] < -14),
        (X["pii_account_lifetime"] >= -14) & (X["pii_account_lifetime"] < 0),
        (X["pii_account_lifetime"] >= 0),
    ]
    pii_account_lifetime_choices = [np.nan, 0, X["pii_account_lifetime"]]
    X["pii_account_lifetime"] = np.select(
        pii_account_lifetime_conditions,
        pii_account_lifetime_choices,
        default=np.nan,
    )

    # age --> addjust it to given dataset!
    X["pii_birthday"] = pd.to_datetime(
        X["pii_birthday"], dayfirst=True, errors="coerce"
    )
    X["pii_age"] = (pd.Timestamp.today() - X["pii_birthday"]).dt.days // 365

    # feature creation
    X["count_trx_per_lifetime"] = X["dormancy_count_trx"] / (
        X["pii_account_lifetime"] + 0.000001
    )
    X["max_gmt_pay_diff_days_per_lifetime"] = X[
        "dormancy_max_gmt_pay_diff_days"
    ] / (X["pii_account_lifetime"] + 0.000001)
    X["freq_x2x_per_lifetime"] = X["aqc_freq_x2x"] / (
        X["pii_account_lifetime"] + 0.000001
    )
    X["dormancy_max_gmt_pay_diff_days_per_count_trx"] = (
        X["dormancy_max_gmt_pay_diff_days"] / X["dormancy_count_trx"]
    )

    return X
