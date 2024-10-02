import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualDataHour(df):
    penggunaan_per_jam = df.groupby('hr')[['casual', 'registered', 'cnt']].mean()

    plt.figure(figsize=(15, 9))

    sns.barplot(x=penggunaan_per_jam.index, y=penggunaan_per_jam['cnt'], color='lime', label='Total')
    sns.barplot(x=penggunaan_per_jam.index, y=penggunaan_per_jam['registered'], color='blue', label='Registered')
    sns.barplot(x=penggunaan_per_jam.index, y=penggunaan_per_jam['casual'], color='red', label='Casual')

    plt.title('Rata-rata Penggunaan Sepeda Per-jam')
    plt.xlabel('Waktu (Jam)')
    plt.ylabel('Rata-rata Sepeda yang Digunakan')
    return plt

def visualDataWeather(df):
    cuaca = df.groupby('weathersit')[['casual', 'registered', 'cnt']].sum()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=cuaca.index, y=cuaca['cnt'], color='lime', label='Total')
    sns.barplot(x=cuaca.index, y=cuaca['registered'], color='blue', label='Registered')
    sns.barplot(x=cuaca.index, y=cuaca['casual'], color='red', label='Casual')

    plt.title('Rata-rata Penggunaan Sepeda Berdasarkan Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Sepeda yang Digunakan')
    plt.xticks([0, 1, 2, 3], ['Cerah', 'Berkabut', 'Hujan/Salju Ringan', 'Hujan/Salju Berat'])
    return plt

day_pd = pd.read_csv(r'Data/day.csv')
hour_pd = pd.read_csv(r'Data\hour.csv')

st.title('Dashboard Proyek Analisis Data Dicoding - Nicholas Tanurgoho')

with st.sidebar:
    st.title('Isi Data CSV')
    st.write ('Data Day.csv')
    st.write(day_pd)
    st.write('Data Hour.csv')
    st.write(hour_pd)

st.write('''Berikut ditampilkan sebuah grafik yang menunjukan jumlah rata rata aktifitas sewa menyewa per-jam''')
st.pyplot(visualDataHour(hour_pd))
st.caption('Grafik 1 - Grafik rata rata penggunaan per jam')
st.write('Rata rata penggunaan sepeda paling banyak pada pukul 17:00 dan diikuti oleh pukul 18:00 lalu mengalami penurunan penyewa pada pukul 19:00. Sedangkan penyewa paling sedikit pada pukul 04:00. Dapat terlihat juga bahwa komposisi penyewa yang menyewa mayoritas dari kelompok \'registered\'.')
st.write('''Berikut ditampilkan sebuah grafik yang menunjukan jumlah rata rata aktifitas sewa menyewa per-cuaca''')
st.pyplot(visualDataWeather(day_pd))
st.caption('Grafik 2 - Grafik rata rata penggunaan per cuaca')
st.write('Terdapat juga data bahwa kondisi cuaca cerah mendapat jumlah penyewa paling banyak lalu juga ditemukan bahwa tidak terdapat kegiatan sewa menyewa pada saat kondisi cuaca hujan/salju berat.')
