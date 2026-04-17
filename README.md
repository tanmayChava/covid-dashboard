# 🌍 COVID-19 Interactive Dashboard

## 📌 Overview

This project is an interactive data dashboard that visualizes global COVID-19 trends using real-world data. Users can explore cases, deaths, and vaccination progress across countries with dynamic filters and interactive charts.

The dashboard is built using Python and deployed as a web app for easy access.

---

## 🚀 Live Demo

🔗 *(Add your deployed Streamlit link here after deployment)*

---

## 📊 Features

* 🌎 Country-wise analysis (single and multiple selection)
* 📅 Date range filtering
* 📈 Time-series trends (7-day rolling average)
* 📊 Top countries comparison
* 🌍 Interactive world map visualization
* 🔍 Scatter analysis (vaccination vs cases)

---

## 🛠️ Tech Stack

* Python
* Pandas
* Plotly
* Streamlit

---

## 📂 Project Structure

```
covid-climate-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── features.py
│
├── charts/
│   ├── line_chart.py
│   ├── bar_chart.py
│   ├── map_chart.py
│   ├── scatter_plot.py
│
├── utils/
│   └── filters.py
```

---

## 📁 Data Source

Data is sourced from **Our World in Data**, which provides publicly available COVID-19 datasets.

---

## ⚙️ How to Run Locally

1. Clone the repository
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the app:

   ```
   streamlit run app.py
   ```

---

## 🌐 Deployment

This app can be deployed using **Streamlit Community Cloud**:

* Connect your GitHub repository
* Select `app.py` as the main file
* Deploy and get a live URL

---

## 📌 Key Insights

* COVID trends vary significantly across countries
* Rolling averages provide clearer trend patterns than raw daily data
* Vaccination levels show varying correlation with case trends

---

## 📈 Future Improvements

* Add more KPIs (death rate, recovery rate)
* Include continent-level filtering
* Improve UI/UX with custom styling
* Add climate dataset integration for comparison

---

## 📄 License

This project is open-source and available for learning purposes.
