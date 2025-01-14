# MultiTimer App: Multi-threaded Timer Management 

MultiTimer App adalah aplikasi berbasis GUI untuk mengelola beberapa timer secara bersamaan menggunakan konsep multithreading. 
Aplikasi ini dirancang untuk memberikan pengalaman pengguna yang responsif dengan memanfaatkan thread terpisah untuk 
menjalankan timer, sehingga tidak mengganggu proses utama aplikasi.

# Teknologi yang Digunakan   
• Bahasa Pemrograman: Python  
• Framework GUI: PyQt5
• Konsep: Multithreading
• Sistem Operasi: Windows, MacOS, Linux

# Cara Instalasi  
Persyaratan Sistem:
• Python versi 3.7 atau lebih baru  
• PyQt5   

### 1. Clone Repository
```bash
git clone https://github.com/adndax/multitimer.git
cd multitimer
```

### 2. Set Up Virtual Environment
For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

For Unix/MacOS:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install PyQt5
```

### 4. Run Application
```bash
python src/main.py
```

# Konsep Multithreading
Aplikasi ini menggunakan konsep multithreading untuk menjalankan beberapa timer secara bersamaan. Setiap timer berjalan pada thread terpisah menggunakan class QThread dari PyQt5. Hal ini memastikan:
	•	Timer dapat berjalan paralel tanpa memblokir proses utama.
	•	Aplikasi tetap responsif terhadap input pengguna saat timer aktif.
 
# Alur Penggunaan
1. Tentukan jumlah timer menggunakan input spin box.
2. Klik tombol Set Timer untuk membuat timer.
3. Atur durasi setiap timer dan klik tombol Mulai untuk memulai hitungan mundur.
4. Timer akan berjalan secara paralel dan notifikasi akan muncul saat timer selesai.
