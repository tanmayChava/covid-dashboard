def add_feactures(df):
    df =df.copy()

    # Per Million  Metrices

    df["cases_per_million"] = (df["total_cases"] / df["population"]) * 106

    # Rolling average (7-day)
    df["new_cases_smmoth"] = (
        df.groupby("location")["new_cases"]
        .transform(lambda x: x.rolling(7).mean())
    )

    return df