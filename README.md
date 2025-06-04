# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan
## Business Understanding

Jaya Jaya Institut, berdiri sejak tahun 2000, memiliki reputasi kuat dalam menghasilkan lulusan berkualitas. Namun, saat ini institusi menghadapi tantangan besar berupa tingginya angka **dropout** mahasiswa. Banyaknya mahasiswa yang tidak menyelesaikan studi mereka menimbulkan dampak signifikan pada reputasi dan efisiensi operasional institusi.

### Permasalahan Bisnis

Tingginya angka dropout di Jaya Jaya Institut mengindikasikan beberapa masalah utama yang perlu ditangani:

* **Ketidaksiapan Akademik:** Mahasiswa mungkin kesulitan mengikuti perkuliahan, yang tercermin dari nilai rendah dan banyaknya mata kuliah yang tidak lulus.
* **Masalah Keuangan:** Keterlambatan pembayaran biaya pendidikan bisa menjadi faktor pemicu utama dropout.
* **Kurangnya Motivasi atau Ketidakcocokan Program Studi:** Mahasiswa mungkin kehilangan motivasi atau merasa program studi yang dipilih tidak sesuai.
* **Faktor Demografis:** Usia saat mendaftar dan latar belakang pendidikan sebelumnya dapat memengaruhi kemampuan mahasiswa untuk menyelesaikan studi.
* **Kurangnya Sistem Deteksi Dini:** Belum ada sistem proaktif yang mampu memantau dan mendeteksi mahasiswa yang berisiko dropout.

Permasalahan ini menuntut pendekatan berbasis data untuk memungkinkan intervensi yang lebih cepat, tepat, dan berdampak nyata.

### Tujuan Proyek

Proyek ini bertujuan untuk membantu Jaya Jaya Institut mengatasi masalah dropout mahasiswa dengan:

* **Mengidentifikasi faktor-faktor utama** yang memengaruhi kemungkinan siswa mengalami dropout.
* **Membangun model prediktif berbasis *machine learning*** untuk mendeteksi risiko dropout sedini mungkin.
* **Menyediakan *business dashboard* interaktif** yang dapat digunakan oleh manajemen akademik untuk memantau performa siswa dan merancang strategi intervensi secara proaktif.

---

### Cakupan Proyek

Proyek ini akan mencakup tahapan-tahapan berikut:

#### Cakupan Analisis

Analisis akan difokuskan pada sejumlah aspek penting yang diyakini berkontribusi terhadap fenomena dropout, antara lain:

* **Demografis:** Meliputi analisis terhadap `Marital status`, `Nacionality`, `Gender`, `Age at enrollment`, `Displaced`, dan `Educational special needs` untuk memahami karakteristik umum mahasiswa yang berisiko dropout.
* **Latar Belakang Pendidikan dan Aplikasi:** Mencakup pemeriksaan `Application mode`, `Application order`, `Course` yang dipilih, `Daytime/evening attendance`, `Previous qualification`, `Previous qualification (grade)`, `Mother's qualification`, `Father's qualification`, `Mother's occupation`, `Father's occupation`, dan `Admission grade`. Aspek ini penting untuk mengidentifikasi pola terkait riwayat pendidikan dan proses pendaftaran.
* **Kinerja Akademik:** Akan menganalisis metrik dari semester pertama dan kedua, seperti `Curricular units 1st sem (credited)`, `Curricular units 1st sem (enrolled)`, `Curricular units 1st sem (evaluations)`, `Curricular units 1st sem (approved)`, `Curricular units 1st sem (grade)`, `Curricular units 1st sem (without evaluations)`, `Curricular units 2nd sem (credited)`, `Curricular units 2nd sem (enrolled)`, `Curricular units 2nd sem (evaluations)`, `Curricular units 2nd sem (approved)`, `Curricular units 2nd sem (grade)`, `Curricular units 2nd sem (without evaluations)`. Selain itu, `Scholarship holder` juga akan dianalisis untuk melihat pengaruh beasiswa terhadap performa dan potensi dropout.
* **Faktor Finansial dan Makroekonomi:** Melibatkan analisis `Debtor`, `Tuition fees up to date` untuk menilai kondisi keuangan mahasiswa, serta `Unemployment rate`, `Inflation rate`, dan `GDP` yang dapat memberikan konteks ekonomi makro yang memengaruhi stabilitas finansial siswa.

#### Tahapan Proyek

1.  **Data Understanding:** Mengumpulkan data mahasiswa yang relevan dan memahami struktur, sumber, serta potensi masalah kualitas data. Tahap ini bertujuan untuk mendapatkan pemahaman mendalam tentang konteks data yang digunakan.
2.  **Data Preparation:** Membersihkan data dari nilai hilang (*missing values*), pencilan (*outliers*), dan inkonsistensi. Melakukan transformasi data yang diperlukan, seperti *encoding* variabel kategorikal dan normalisasi, agar data siap untuk dianalisis dan dimodelkan.
3.  **Exploratory Data Analysis (EDA):** Melakukan analisis deskriptif dan visualisasi data untuk mengidentifikasi pola, tren, dan hubungan antar variabel. Tujuan utama dari tahap ini adalah menemukan faktor-faktor potensial yang memengaruhi tingkat dropout.
4.  **Pemodelan Machine Learning:** Membagi *dataset* menjadi data pelatihan dan data pengujian. Memilih algoritma yang sesuai, melatih model dengan data pelatihan, dan melakukan *tuning hyperparameter* jika diperlukan untuk meningkatkan performa model.
5.  **Evaluasi Model:** Mengukur kinerja model menggunakan data pengujian dengan metrik evaluasi seperti akurasi, presisi, *recall*, dan F1-score, guna menentukan model terbaik dalam memprediksi risiko dropout.
6.  **Membuat Prototipe Streamlit:** Mengembangkan antarmuka pengguna sederhana menggunakan Streamlit untuk mengakses model prediksi secara interaktif. Prototipe ini akan memungkinkan pengguna memasukkan data siswa dan mendapatkan prediksi risiko dropout secara *real-time*.
7.  **Pengembangan Business Dashboard:** Merancang dan membangun *dashboard* interaktif yang memungkinkan tim manajemen akademik memantau metrik penting terkait dropout, mengeksplorasi faktor risiko utama, dan melihat hasil prediksi model secara *real-time*.
8.  **Penyusunan Laporan dan Rekomendasi:** Mendokumentasikan seluruh proses proyek, mulai dari analisis hingga implementasi. Menyajikan temuan utama dan memberikan rekomendasi berbasis data yang dapat ditindaklanjuti oleh manajemen untuk menekan angka dropout.

---

### Persiapan

Sumber Data: [Dataset Mahasiswa Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup Environment:

1.  **Jalankan `notebook.ipynb`:**
    * **Instal Dependensi:** Di terminal proyek, jalankan perintah berikut:
        ```bash
        pip install -r requirements.txt
        ```
    * **Jalankan Notebook:** Gunakan `jupyter notebook` atau `jupyter lab` (lokal) atau unggah ke Google Colab dan jalankan semua sel.

2.  **Jalankan `prediction.py`:**
    * **Verifikasi Direktori Model:** Pastikan *path* model dan *encoder* di `prediction.py` sudah benar. Ubah jika perlu, model akan diambil dari folder `model/`:
        ```python
        model = joblib.load("model/rf_model.pkl")
        encoder = joblib.load("model/onehot_encoder.pkl")
        ```
    * **Instal Dependensi (jika belum):**
        ```bash
        pip install pandas joblib scikit-learn
        ```
    * **Jalankan Skrip:** Di terminal proyek, jalankan:
        ```bash
        python prediction.py
        ```
        Hasil prediksi akan ditampilkan sebagai *output*.

3.  **Jalankan Streamlit App (`app.py`):**
    * **Pastikan Model Tersedia:** Pastikan file model (`rf_model.pkl`) dan encoder (`onehot_encoder.pkl`) berada di dalam folder `model/` di direktori proyek Anda.
    * **Instal Streamlit (jika belum):**
        ```bash
        pip install streamlit
        ```
    * **Jalankan Aplikasi:** Di terminal proyek, jalankan:
        ```bash
        streamlit run app.py
        ```
        Aplikasi Streamlit akan terbuka di *browser* Anda.

4.  **Jalankan Dashboard (Metabase dengan Docker):**
    * **Instal Docker Desktop:** Unduh dan instal dari [www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
    * **Pindahkan Database:** Letakkan `metabase.db.mv.db` di direktori yang mudah diakses (misalnya, direktori proyek).
    * **Tarik Image:** Di terminal, jalankan:
        ```bash
        docker pull metabase/metabase:latest
        ```
    * **Jalankan Container (Mount Volume):** Ganti `/path/ke/direktori/anda` dengan *path* absolut ke direktori `metabase.db.mv.db`:
        ```bash
        docker run -d -p 3000:3000 --name metabase -v /path/ke/direktori/anda:/metabase-data metabase/metabase
        ```
    * **Akses Metabase:** Buka `http://localhost:3000` di *browser*.
    * **Login:** Email: `root@mail.com`, Password: `root123`.
    * **Hubungkan Database:** Tambahkan database H2. *Path* database di *container*: `/metabase-data/metabase.db.mv.db`. Tidak ada kredensial tambahan biasanya. Uji koneksi.

## Business Dashboard

![Alt text](<needkh-dashboard 1.png>)
![Alt text](<needkh-dashboard 2.png>)
![Alt text](<needkh-dashboard 3.png>) 
![Alt text](<needkh-dashboard 4.png>)

*Business Dashboard* ini dikembangkan menggunakan Metabase dan berfungsi sebagai alat visualisasi interaktif untuk memantau performa mahasiswa dan menganalisis faktor-faktor yang berkontribusi terhadap *dropout*. *Dashboard* ini menyediakan gambaran komprehensif mengenai status mahasiswa dan metrik kunci yang relevan.

### Ikhtisar Dashboard:

* **Ringkasan Statistik Utama:**
    * **Total Mahasiswa:** Menampilkan jumlah keseluruhan mahasiswa (misal: 4,424).
    * **Total Mahasiswa yang Terdaftar:** Jumlah mahasiswa yang aktif terdaftar (misal: 794).
    * **Total Mahasiswa yang Telah Lulus:** Jumlah mahasiswa yang sudah menyelesaikan studi (misal: 2,209).
    * **Total Mahasiswa yang Telah Keluar:** Jumlah mahasiswa yang *dropout* atau keluar dari institusi (misal: 1,421).
    * **Total Mahasiswa yang Berpotensi Keluar:** Jumlah mahasiswa yang diidentifikasi berisiko tinggi *dropout* oleh model (misal: 117).
    * **Total Mahasiswa yang Berpotensi Tinggi Keluar:** Subset dari mahasiswa berpotensi keluar dengan risiko yang sangat tinggi (misal: 28).

* **10 Fitur Penting Teratas Penyebab Mahasiswa Keluar:**
    * Diagram batang ini menampilkan fitur-fitur (variabel) dengan *importance* tertinggi yang memengaruhi keputusan mahasiswa untuk *dropout*. Berdasarkan analisis model, 10 fitur paling penting yang berkontribusi terhadap risiko *dropout* mahasiswa adalah:
        1.  `Curricular_units_2nd_sem_approved`
        2.  `Curricular_units_2nd_sem_grade`
        3.  `Curricular_units_1st_sem_grade`
        4.  `Curricular_units_1st_sem_approved`
        5.  `Age_at_enrollment`
        6.  `Tuition_fees_up_to_date`
        7.  `Scholarship_holder`
        8.  `Debtor`
        9.  `Gender_Male`
        10. `Application_mode_2nd Phase - General Contingent`
    * Fitur-fitur ini menjadi fokus utama dalam memahami dan mengatasi masalah *dropout*.

* **Distribusi Mahasiswa berdasarkan Status:**
    * Diagram donat ini menunjukkan proporsi mahasiswa berdasarkan status mereka: `Graduate` (lulus), `Dropout`, dan `Enrolled` (terdaftar). Total mahasiswa ditampilkan di tengah diagram.

### Temuan Utama dari Dashboard:

* **Distribusi Curricular_units_2nd_sem_approved berdasarkan Status:** Mahasiswa yang *dropout* banyak terkonsentrasi pada skala unit kurikuler yang disetujui 0-2.5 sebanyak 929 mahasiswa, diikuti oleh skala 2.5-5 sebanyak 239 mahasiswa, dan skala 5-7.5 sebanyak 202 mahasiswa. Ini menunjukkan bahwa performa akademik yang rendah (jumlah unit yang disetujui sedikit) di semester kedua sangat berkorelasi dengan *dropout*.
* **Distribusi Curricular_units_2nd_sem_grade berdasarkan Status:** Pola serupa terlihat pada nilai. Mahasiswa yang *dropout* paling banyak berada pada skala nilai 0-10 sebanyak 727 mahasiswa, diikuti oleh skala 10-12.5 sebanyak 450 mahasiswa, dan skala 12.5-15 sebanyak 216 mahasiswa. Ini menegaskan bahwa rata-rata nilai akademik yang rendah merupakan indikator kuat risiko *dropout*.
* **Distribusi Scholarship_holder berdasarkan Status:** Sebagian besar mahasiswa yang *dropout* adalah mereka yang tidak memiliki beasiswa, yaitu sebanyak 1287 mahasiswa, dibandingkan dengan 134 mahasiswa *dropout* yang memiliki beasiswa. Hal ini menyoroti pentingnya dukungan finansial sebagai salah satu faktor mitigasi *dropout*.
* **Distribusi Age_at_enrollment berdasarkan Status:** Mahasiswa yang *dropout* paling banyak berada dalam rentang usia 15-22.5 tahun sebanyak 693 mahasiswa, diikuti oleh rentang usia 22.5-30 tahun sebanyak 343 mahasiswa. Ini mengindikasikan bahwa mahasiswa yang lebih muda saat pendaftaran mungkin memiliki risiko *dropout* yang lebih tinggi.
* **Distribusi Gender berdasarkan Status:** Jumlah mahasiswa laki-laki yang *dropout* adalah 701, sementara mahasiswa perempuan yang *dropout* sedikit lebih banyak yaitu 720. Angka ini menunjukkan bahwa *dropout* terjadi pada kedua *gender* dengan distribusi yang relatif seimbang, namun perlu diperhatikan perbedaan spesifik jika ada.
* **Distribusi Debtor berdasarkan Status:** Mahasiswa yang *dropout* sebagian besar adalah mereka yang *tidak* berstatus *debtor* (1109 mahasiswa), sementara 312 mahasiswa yang *dropout* berstatus *debtor*. Meskipun mayoritas *dropout* bukan *debtor*, status *debtor* tetap menjadi kontributor signifikan terhadap *dropout* bagi sebagian kelompok mahasiswa.
* **Distribusi Tuition_fees_up_to_date berdasarkan Status:** Mahasiswa yang *dropout* didominasi oleh mereka yang `Tuition_fees_up_to_date` (964 mahasiswa), sementara 457 mahasiswa *dropout* tidak `Tuition_fees_up_to_date`. Hal ini menunjukkan bahwa keterlambatan pembayaran biaya kuliah (tidak `up_to_date`) memang menjadi faktor risiko *dropout*, meskipun jumlahnya tidak sebanyak mereka yang sudah membayar tepat waktu.

### Kesimpulan dari Dashboard:

*Dashboard* ini secara jelas menunjukkan bahwa **kinerja akademik** (jumlah unit dan nilai yang disetujui di semester 1 dan 2) adalah prediktor paling kuat untuk *dropout* mahasiswa di Jaya Jaya Institut. Usia saat pendaftaran juga merupakan faktor penting, dengan mahasiswa yang lebih muda cenderung memiliki risiko *dropout* lebih tinggi. Meskipun faktor finansial seperti status `Scholarship_holder` dan `Debtor`, serta status pembayaran `Tuition_fees_up_to_date`, juga berkontribusi, pengaruhnya tidak sebesar faktor akademik. Distrubusi *dropout* berdasarkan gender relatif seimbang.
Temuan ini menyoroti perlunya intervensi dini yang berfokus pada dukungan akademik dan pemantauan ketat terhadap progres nilai dan penyelesaian unit kurikuler, terutama pada semester-semester awal. Dukungan finansial juga tetap relevan, terutama bagi mahasiswa yang tidak memiliki beasiswa.

## Menjalankan Sistem Machine Learning

Prototype sistem *machine learning* ini bertujuan untuk memprediksi status mahasiswa di Jaya Jaya Institut, apakah mereka akan *dropout* atau tidak, berdasarkan data individual mahasiswa.

### Langkah-langkah Menjalankan Prototype:

1.  **Buka aplikasi prototype** melalui *link* berikut: [Streamlit Prediksi Dropout Mahasiswa Jaya Jaya Institut](https://nidaank-submission-bpds2-app-cjrbjq.streamlit.app])
2.  **Isi seluruh *field input*** sesuai data yang diinginkan, yang terbagi dalam beberapa bagian seperti yang terlihat pada *screenshot* Anda:

    * **Input Data Mahasiswa (Bagian Atas):**
        * `Application Mode`: Pilih mode aplikasi mahasiswa.
        * `Course`: Pilih program studi yang diambil mahasiswa.
        * `Gender`: Pilih jenis kelamin mahasiswa.
        * `Previous Qualification`: Pilih kualifikasi pendidikan terakhir mahasiswa sebelum masuk kuliah.
        * `Age at Enrollment`: Sesuaikan usia mahasiswa saat mendaftar menggunakan *slider*.

    * **Input Data Mahasiswa (Bagian Kanan Atas - Kinerja Akademik Semester 2):**
        * `2nd Sem Units Approved`: Masukkan jumlah unit kurikuler yang disetujui pada semester kedua.
        * `2nd Sem Grade`: Masukkan rata-rata nilai unit kurikuler yang disetujui pada semester kedua.

    * **Input Data Mahasiswa (Bagian Kanan Tengah - Kinerja Akademik Semester 1):**
        * `1st Sem Units Approved`: Masukkan jumlah unit kurikuler yang disetujui pada semester pertama.
        * `1st Sem Grade`: Masukkan rata-rata nilai unit kurikuler yang disetujui pada semester pertama.

    * **Input Data Mahasiswa (Bagian Bawah - Kondisi Finansial):**
        * `Tuition Fees Up to Date?`: Pilih 1 jika biaya kuliah sudah lunas, 0 jika belum.
        * `Scholarship Holder?`: Pilih 1 jika mahasiswa penerima beasiswa, 0 jika tidak.
        * `Debtor?`: Pilih 1 jika mahasiswa memiliki utang biaya, 0 jika tidak.

3.  **Klik tombol “Prediksi”**.

Sistem akan menjalankan model *machine learning* yang telah dilatih sebelumnya. Hasil prediksi akan muncul di bagian bawah antarmuka, misalnya:

* `❌ Mahasiswa diprediksi berpotensi DROP OUT dengan kemungkinan: 60.89%`
* `✅ Mahasiswa TIDAK diprediksi dropout. Kemungkinan bertahan: 83.33%`

### Penjelasan Teknis Singkat:

* Sistem ini dibangun dengan *framework* Streamlit, yang menghubungkan antarmuka pengguna dengan model *machine learning* berbasis Python.
* Model telah melalui proses pelatihan (*training*) menggunakan data historis mahasiswa.
* Saat pengguna mengisi *form*, data tersebut akan di-*encoding* menjadi *input* numerik dan kategorikal yang sesuai dengan format model.
* Model kemudian memprediksi status mahasiswa dan hasilnya ditampilkan langsung.

## Conclusion

Proyek ini berhasil mengembangkan sistem deteksi dini risiko *dropout* mahasiswa untuk Jaya Jaya Institut, yang merupakan langkah krusial dalam mengatasi tingginya angka *dropout*. Dengan memanfaatkan data historis mahasiswa, kami telah membangun model *machine learning* prediktif dan menyajikan wawasan penting melalui *business dashboard* interaktif.

Evaluasi model *machine learning* menggunakan algoritma **Random Forest** menunjukkan kinerja yang sangat baik:
* **Accuracy:** 0.9434 (94.34%)
* **ROC AUC:** 0.9790

**Classification Report:**
```
              precision    recall  f1-score   support

           0       0.92      0.97      0.94       601
           1       0.97      0.92      0.94       601

    accuracy                           0.94      1202
   macro avg       0.94      0.94      0.94      1202
weighted avg       0.94      0.94      0.94      1202
```
Hasil ini menunjukkan bahwa model memiliki kemampuan yang kuat dalam mengidentifikasi mahasiswa yang berpotensi *dropout* (kelas 1) maupun yang tidak (*dropout*) (kelas 0), dengan *precision* dan *recall* yang seimbang dan tinggi.

Analisis *feature importance* mengkonfirmasi bahwa faktor **kinerja akademik** (nilai dan jumlah unit kurikuler yang disetujui di semester 1 dan 2) adalah prediktor paling dominan. Ini selaras dengan temuan dari *business dashboard* yang menunjukkan konsentrasi *dropout* pada mahasiswa dengan nilai dan unit yang disetujui rendah. Faktor lain seperti usia saat pendaftaran, status pembayaran biaya kuliah, kepemilikan beasiswa, dan status *debtor* juga memiliki pengaruh, meskipun tidak sekuat faktor akademik.

### Rekomendasi Action Items

Berdasarkan temuan proyek dan kinerja model, berikut adalah beberapa rekomendasi *action items* yang dapat dilakukan Jaya Jaya Institut untuk menekan angka *dropout*:

* **Intervensi Akademik Dini:**
    * Fokus pada mahasiswa dengan performa akademik rendah, terutama pada semester pertama dan kedua, yang ditunjukkan oleh nilai `Curricular_units_1st/2nd_sem_grade` dan `Curricular_units_1st/2nd_sem_approved` yang rendah.
    * Sediakan program bimbingan belajar, *peer tutoring*, atau klinik akademik khusus bagi mahasiswa yang menunjukkan tanda-tanda kesulitan di awal semester.
    * Pantau secara proaktif kemajuan akademik mahasiswa yang teridentifikasi berisiko tinggi melalui *dashboard* dan prototipe Streamlit.

* **Dukungan Finansial dan Konseling:**
    * Tinjau dan tingkatkan program beasiswa atau bantuan finansial, terutama bagi mahasiswa yang tidak memiliki beasiswa (`Scholarship_holder`) dan yang memiliki masalah keterlambatan pembayaran (`Tuition_fees_up_to_date` tidak lunas) atau status `Debtor`.
    * Sediakan layanan konseling finansial untuk membantu mahasiswa mengelola biaya pendidikan dan mencari solusi jika menghadapi kesulitan.

* **Program Adaptasi dan Orientasi:**
    * Pertimbangkan program orientasi atau adaptasi yang lebih intensif bagi mahasiswa baru, terutama yang berusia lebih muda (`Age_at_enrollment`), untuk membantu mereka menyesuaikan diri dengan lingkungan perkuliahan.
    * Perkuat program bimbingan dan pendampingan untuk mahasiswa yang masuk melalui `Application_mode` tertentu yang menunjukkan risiko *dropout* lebih tinggi (misalnya, `2nd Phase - General Contingent`).

* **Peningkatan Kualitas Kurikulum dan Pengajaran:**
    * Menganalisis lebih lanjut mata kuliah dan program studi (`Course`) yang memiliki tingkat *dropout* tinggi untuk mengidentifikasi potensi perbaikan dalam kurikulum atau metode pengajaran.
    * Pastikan kualitas pengajaran yang konsisten untuk menjaga motivasi dan performa akademik mahasiswa.

* **Pemanfaatan Sistem Prediksi:**
    * Integrasikan prototipe Streamlit ke dalam alur kerja manajemen akademik untuk identifikasi risiko *dropout* secara *real-time*.
    * Gunakan *business dashboard* secara rutin untuk memantau tren *dropout*, mengevaluasi efektivitas intervensi, dan membuat keputusan strategis berbasis data.

Dengan implementasi rekomendasi ini, Jaya Jaya Institut diharapkan dapat secara signifikan mengurangi angka *dropout* dan meningkatkan tingkat keberhasilan studi mahasiswanya.
