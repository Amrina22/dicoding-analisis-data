import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
file_path = "data.csv"
dfs = pd.read_csv(file_path)

# Select specific air quality indicator columns
columns_of_interest = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']

# Create a subset DataFrame with the selected columns
df_subset = dfs[columns_of_interest]

# Check for NaN values in the subset DataFrame
df_subset = df_subset.fillna(0)

# Calculate correlation matrix
correlation_matrix = df_subset.corr()

# Select specific columns for bar plot
columns_to_plot = ['NO2', 'SO2', 'PM10', 'O3', 'CO']

# Menggunakan data hanya untuk tahun 2017
df_2017 = dfs[dfs['year'] == 2017]

# Layout Streamlit
st.title('Analisis Kualitas Udara')

# Visualisasi matriks korelasi menggunakan heatmap (Atas)
st.header('Matriks Korelasi: Indikator Kualitas Udara')
fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5, ax=ax_corr)
ax_corr.set_title('Matriks Korelasi: Indikator Kualitas Udara')
st.pyplot(fig_corr)
st.caption('PM10 terkait dengan PM2.5, ini diharapkan karena keduanya merupakan partikel. CO, NOx dan NO2 saling berkaitan. Ketika kadar CO dan NO2 tinggi, maka kadar O3 kecil')

# Visualisasi Bar Plot Stasiun (Bawah)
st.header('Bar Plot untuk Stasiun')
fig_bar, ax_bar = plt.subplots(figsize=(15, 6))
for column in columns_to_plot:
    sns.barplot(x='station', y=column, data=df_2017, ci=None, label=column, ax=ax_bar)

ax_bar.set_title('Rata-rata Tingkat Pencemaran berdasarkan Stasiun Tahun 2017')
ax_bar.set_ylabel('Rata-rata Tingkat Pencemaran')
ax_bar.set_xlabel('Stasiun')

# Rotasi dan penataan label sumbu x
ax_bar.set_xticklabels(ax_bar.get_xticklabels(), rotation=45, ha='right')

ax_bar.legend()
st.pyplot(fig_bar)
st.caption('Keterangan: Bar plot menunjukkan rata-rata tingkat pencemaran berdasarkan stasiun pada tahun 2017. Stasiun dengan kadar polusi tertinggi yang terjadi pada tahun 2017 adalah stasiun Wanliu')
