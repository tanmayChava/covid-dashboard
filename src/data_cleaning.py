import pandas as pd

def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert Date
    df["date"] = pd.to_datetime(df["date"])

    # Select relevant columns

    cols = [
        "location",
        "date",
        "total_cases",
        "new_cases",
        "total_deaths",
        "new_deaths",
        "total_vaccinations",
        "people_vaccinated",
        "population"
    ]
    df = df[cols]

    # drop rows with no country
    df = df.dropna(subset=["location"])
    return df