import pandas as pd

# Baca dataset
data = pd.read_csv("../dataset/sustainability_data.csv")

# Ringkasan data
print("Jumlah baris:", len(data))
print("Jumlah kolom:", len(data.columns))
print("\nNama kolom:")
print(data.columns.tolist())

# Tampilkan 5 data pertama
print("\nData sample:")
print(data.head())

# Statistik dasar
print("\nStatistik dasar:")
print(data.describe())

# Simpan ringkasan ke file
with open("../output/ringkasan.txt", "w") as f:
    f.write("Jumlah baris: " + str(len(data)) + "\n")
    f.write("Jumlah kolom: " + str(len(data.columns)) + "\n\n")
    f.write("Nama kolom:\n" + str(data.columns.tolist()) + "\n\n")
    f.write("Statistik dasar:\n" + str(data.describe()))

# Fungsi klasifikasi sederhana
def klasifikasi(nilai):
    if nilai >= 80:
        return "Baik"
    elif nilai >= 60:
        return "Sedang"
    else:
        return "Kurang"

# Tambahin kolom kategori (ganti 'score' sesuai nama kolom di dataset lu)
data["Kategori"] = data["score"].apply(klasifikasi)

# Simpan hasil klasifikasi ke file CSV
data.to_csv("../output/hasil_klasifikasi.csv", index=False)

print("\nData dengan klasifikasi:")
print(data[["score", "Kategori"]].head())
