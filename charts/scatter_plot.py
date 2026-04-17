import plotly.express as px

def plot_vaccine_vs_cases(df):
    latest = df.sort_values("date").groupby("location").tail(1)

    fig = px.scatter(
        latest,
        x="people_vaccinated",
        y="total_cases",
        size="population",
        hover_name="location",
        title="Vaccination vs Cases"
    )
    return fig