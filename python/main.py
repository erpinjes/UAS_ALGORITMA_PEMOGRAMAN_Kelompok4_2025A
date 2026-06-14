import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/sustainability_data.csv")

with open("../output/laporan_sustainability_py.txt", "w") as f:
    f.write("Jumlah baris: " + str(len(data)) + "\n")
    f.write("Jumlah kolom: " + str(len(data.columns)) + "\n\n")
    f.write("Nama kolom:\n" + str(data.columns.tolist()) + "\n\n")
    f.write("Statistik dasar:\n" + str(data.describe()))

def klasifikasi(nilai):
    if nilai >= 80:
        return "Baik"
    elif nilai >= 60:
        return "Sedang"
    else:
        return "Kurang"

data["Kategori"] = data["nilai"].apply(klasifikasi)
data.to_csv("../output/hasil_klasifikasi_py.csv", index=False)


plt.style.use("seaborn-v0_8")
kategori_counts = data["Kategori"].value_counts()
ax = kategori_counts.plot(kind="bar", color=["green", "orange", "red"], edgecolor="black")
plt.title("Distribusi Kategori", fontsize=14, fontweight="bold")
plt.xlabel("Kategori")
plt.ylabel("Jumlah Data")
for p in ax.patches:
    ax.annotate(str(int(p.get_height())),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom')
plt.savefig("../docs/distribusi_kategori.png")
plt.close()

avg_per_param = data.groupby("parameter")["nilai"].mean()
avg_per_param.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Rata-rata Nilai per Parameter", fontsize=14, fontweight="bold")
plt.xlabel("Parameter")
plt.ylabel("Rata-rata Nilai")
plt.savefig("../docs/rata_rata_per_parameter.png")
plt.close()

plt.boxplot(data["nilai"])
plt.title("Boxplot Distribusi Nilai", fontsize=14, fontweight="bold")
plt.ylabel("Nilai")
plt.savefig("../docs/boxplot_nilai.png")
plt.close()

data["tanggal"] = pd.to_datetime(data["tanggal"])
energy_data = data[data["parameter"] == "Energy"]
monthly_avg = energy_data.groupby(data["tanggal"].dt.to_period("M"))["nilai"].mean()
monthly_avg.plot(kind="line", marker="o", color="blue")
plt.title("Tren Rata-rata Energy per Bulan", fontsize=14, fontweight="bold")
plt.xlabel("Bulan")
plt.ylabel("Rata-rata Energy (kWh)")
plt.savefig("../docs/tren_energy_per_bulan.png")
plt.close()
