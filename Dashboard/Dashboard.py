import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

day = pd.read_csv('./Data/day.csv')
hour = pd.read_csv('./Data/hour.csv')
cleaned_combined_data = pd.read_csv('./Data/cleaned_combined_data.csv')
merged_data = pd.read_csv('./Data/merged_data.csv')

st.title("ANALISIS AIR QUALITY")
st.subheader("Nama : Hamdika Putra")
st.subheader("Email : hmdkaptr@gmail.com")
st.subheader("ID Dicoding : razeyuki")

# Frekuensi Suhu Harian
st.subheader("Frekuensi Suhu Harian:")
st.markdown("Pada bagian ini, kita akan menganalisis distribusi suhu harian dalam rentang tertentu. Dengan membagi suhu menjadi beberapa bin, kita dapat melihat seberapa sering suhu berada dalam setiap rentang. Hal ini membantu kita untuk memahami pola suhu harian dan frekuensinya.")

temp_bins = pd.cut(cleaned_combined_data['temp_x'], bins=10)  # Membagi data menjadi 10 bin
temp_counts = temp_bins.value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=temp_counts.index.astype(str), y=temp_counts.values)
plt.title('Frekuensi Suhu Harian')
plt.xlabel('Rentang Suhu')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)  

st.pyplot(plt)
st.write('Hasil frekuensi suhu:', temp_counts) 

# Rata-rata Jumlah Pengendara Berdasarkan Musim
st.subheader("Rata-rata Jumlah Pengendara Berdasarkan Musim:")
st.markdown("Analisis ini bertujuan untuk melihat bagaimana jumlah pengendara bervariasi di setiap musim. Dengan menghitung rata-rata jumlah pengendara, kita dapat memahami tren penggunaan sepeda berdasarkan kondisi musiman.")

plt.figure(figsize=(10, 6))
sns.lineplot(x='season', y='cnt_x', data=cleaned_combined_data, estimator=np.mean)
plt.title('Rata-rata Jumlah Pengendara Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Pengendara')

st.pyplot(plt)
plt.close()

# Frekuensi Kelembapan Harian
st.subheader("Frekuensi Kelembapan Harian:")
st.markdown("Di sini, kita akan menganalisis distribusi kelembapan harian dengan cara yang mirip dengan analisis suhu. Dengan melihat frekuensi kelembapan dalam rentang tertentu, kita dapat mengetahui seberapa sering kelembapan berada dalam level tertentu.")

hum_bins = pd.cut(cleaned_combined_data['hum_x'], bins=10)  
hum_counts = hum_bins.value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=hum_counts.index.astype(str), y=hum_counts.values)
plt.title('Frekuensi Kelembapan Harian')
plt.xlabel('Rentang Kelembapan')
plt.ylabel('Frekuensi')
plt.xticks(rotation=45)  

st.pyplot(plt)
plt.close()

# Identifikasi Outliers
st.subheader("Identifikasi Outliers Suhu, Kelembapan, dan Jumlah Pengendara:")
st.markdown("Dalam analisis ini, kita akan memeriksa distribusi suhu, kelembapan, dan jumlah pengendara untuk mengidentifikasi adanya outlier. Outlier dapat memberikan wawasan penting tentang data yang tidak biasa dan harus ditangani dengan hati-hati.")

plt.subplot(1, 3, 1)
sns.histplot(cleaned_combined_data['temp_x'], bins=30, kde=True)
plt.title('Distribusi Suhu')
plt.xlabel('Suhu')

# Subplot 2: Distribusi Kelembapan
plt.subplot(1, 3, 2)
sns.histplot(cleaned_combined_data['hum_x'], bins=30, kde=True)
plt.title('Distribusi Kelembapan')
plt.xlabel('Kelembapan')

# Subplot 3: Distribusi Jumlah Pengendara
plt.subplot(1, 3, 3)
sns.histplot(cleaned_combined_data['cnt_x'], bins=30, kde=True)
plt.title('Distribusi Jumlah Pengendara')
plt.xlabel('Jumlah Pengendara')

plt.tight_layout()
st.pyplot(plt)
plt.close()

# Korelasi Antar Variabel
st.subheader("Korelasi Antar Variabel:")
st.markdown("Di sini, kita akan menganalisis hubungan antara suhu, kelembapan, dan jumlah pengendara menggunakan matriks korelasi. Korelasi memberikan wawasan tentang bagaimana perubahan dalam satu variabel dapat mempengaruhi variabel lainnya.")

correlation_matrix = cleaned_combined_data[['temp_x', 'hum_x', 'cnt_x']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Korelasi Antar Variabel')

st.pyplot(plt)
plt.close()

# Pengaruh Suhu Terhadap Jumlah Pengendara
st.subheader("Pengaruh Suhu Terhadap Jumlah Pengendara:")
st.markdown("Analisis ini menunjukkan bagaimana suhu harian mempengaruhi jumlah pengendara. Dengan menggunakan scatter plot, kita dapat melihat pola dan hubungan antara suhu dan jumlah pengendara.")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=cleaned_combined_data['temp_x'], y=cleaned_combined_data['cnt_x'], alpha=0.5)
plt.title('Pengaruh Suhu Terhadap Jumlah Pengendara')
plt.xlabel('Suhu Harian')
plt.ylabel('Jumlah Pengendara')

st.pyplot(plt)
plt.close()

# Variasi Jumlah Pengendara Berdasarkan Rentang Suhu
st.subheader("Variasi Jumlah Pengendara Berdasarkan Rentang Suhu:")
st.markdown("Di bagian ini, kita akan menganalisis variasi jumlah pengendara berdasarkan rentang suhu. Dengan menggunakan box plot, kita dapat melihat distribusi jumlah pengendara di berbagai rentang suhu.")

plt.figure(figsize=(10, 6))
sns.boxplot(x=pd.cut(cleaned_combined_data['temp_x'], bins=5), y='cnt_x', data=cleaned_combined_data)
plt.title('Variasi Jumlah Pengendara Berdasarkan Rentang Suhu')
plt.xlabel('Rentang Suhu')
plt.ylabel('Jumlah Pengendara')

st.pyplot(plt)
plt.close()
