import plotly.express as px

def plot_top_countries(df):
    latest = df.sort_values("date").groupby("location").tail(1)

    top = latest.sort_values("total_cases", ascending=False).head(10)

    fig = px.bar(
        top,
        x="location",
        y="total_cases",
        title="Top 10 Countries by Total Cases"
    )
    return fig