#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

struct Data {
    string tanggal, lokasi, parameter, satuan;
    double nilai;
    string kategori;
};

string klasifikasi(double nilai) {
    if (nilai >= 80) return "Baik";
    else if (nilai >= 60) return "Sedang";
    else return "Kurang";
}

int main() {
    ifstream file("../dataset/sustainability_data.csv");
    ofstream ringkasan("../output/laporan_sustainability_cpp.txt");
    ofstream hasil("../output/hasil_klasifikasi_cpp.csv");

    if (!file.is_open()) {
        cout << "Gagal membuka file dataset!" << endl;
        return 1;
    }

    vector<Data> dataset;
    string line;
    getline(file, line); // skip header

    while (getline(file, line)) {
        stringstream ss(line);
        Data d;
        string nilaiStr;

        getline(ss, d.tanggal, ',');
        getline(ss, d.lokasi, ',');
        getline(ss, d.parameter, ',');
        getline(ss, nilaiStr, ',');
        getline(ss, d.satuan, ',');

        d.nilai = stod(nilaiStr);
        d.kategori = klasifikasi(d.nilai);
        dataset.push_back(d);
    }

    int n = dataset.size();
    vector<double> values;
    double sum = 0;
    double minVal = dataset[0].nilai, maxVal = dataset[0].nilai;

    for (auto &d : dataset) {
        sum += d.nilai;
        minVal = min(minVal, d.nilai);
        maxVal = max(maxVal, d.nilai);
        values.push_back(d.nilai);
    }

    double mean = sum / n;
    double var = 0;
    for (auto &v : values) var += (v - mean) * (v - mean);
    double stddev = sqrt(var / n);

    sort(values.begin(), values.end());
    double q25 = values[n/4];
    double q50 = values[n/2];
    double q75 = values[(3*n)/4];

    ringkasan << "Jumlah baris: " << n << endl;
    ringkasan << "Jumlah kolom: 5\n" << endl;
    ringkasan << "Nama kolom:\n['tanggal', 'lokasi', 'parameter', 'nilai', 'satuan']\n" << endl;
    ringkasan << "Statistik dasar:\n";
    ringkasan << "count\t" << n << endl;
    ringkasan << "mean\t" << mean << endl;
    ringkasan << "std\t" << stddev << endl;
    ringkasan << "min\t" << minVal << endl;
    ringkasan << "25%\t" << q25 << endl;
    ringkasan << "50%\t" << q50 << endl;
    ringkasan << "75%\t" << q75 << endl;
    ringkasan << "max\t" << maxVal << endl;

    ringkasan << "\nData dengan klasifikasi:\n";
    ringkasan << "nilai\tKategori\n";
    for (int i = 0; i < 5 && i < n; i++) {
        ringkasan << dataset[i].nilai << "\t" << dataset[i].kategori << endl;
    }

    hasil << "tanggal,lokasi,parameter,nilai,satuan,Kategori\n";
    for (auto &d : dataset) {
        hasil << d.tanggal << "," << d.lokasi << "," << d.parameter << ","
              << d.nilai << "," << d.satuan << "," << d.kategori << "\n";
    }

    cout << "Proses selesai. Ringkasan lengkap sudah dibuat di output." << endl;
    return 0;
}
