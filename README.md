<h1 align="center">
Laporan Proyek Mahchine Learning - Achmad Naila Muna Ramadhani
</h1>



# Domain Proyek

## *project Background*: 

Polusi udara adalah permasalahan kompleks di setiap daerah, tak terkecuali di DKI Jakarta.Relawan dan konsultan kesehatan dari Yayasan Alam Sehat Lestari (ASRI), mencatat bahwa kualitas udara di jakarta sangatlah buruk, bahkan 5 kali lebih buruk daripada standar minimum baru yang ditetapkan WHO. Menurut Kementrian Lingkungan Hidup dan Kehutanan (KLHK) sumber utama terjadinya pencemaran udara di kota-kota besar termasuk DKI Jakarta yaitu penggunaan kendaraan motor yang terlalu banyak.

# *Bussiness  Understanding*

## * Problem Statement *
* Bagaimana melakukan klasifikasi kualitas udara di Jakarta berdasarkan nilai kandungan udara dengan menggunakan *Machine Learning*?

## * Goals *
* Membangun model *machine learning* yang dapat melakukan klasifikasi kualitas udara di DKI Jakarta berdasarkan nilai parameter kandungan udara dengan menggunakan *LogisticRegression*

# *Data Understanding*

Merujuk dari permasalahan yang ada saya menggunakan data yang dirilis oleh Jakarta open data, mengenai Indeks Standar Pencemaran Udara (ISPU) di DKI Jakarta dalam satu tahun terakhir dalam rentang waktu bulan januari sampai dengan bulan Oktober Tahun 2021 yang didapat dari pengukuran oleh 5 stasiun pemantau kualitas udara (SPKU) yang ada di Provinsi DKI Jakarta yang berjumlah sebanyak 758 data Indeks Standar Pencemaran Udara(ISPU). Untuk menentukan tingkat kualitas udara ini, parameternya mengacu pada parameter penilaian yang sudah ditentukan oleh Dinas lingkungan hidup Provinsi terkait. Sehingga hasil penelitian nantinya dapat menjadi bahan acuan penilaian bagaimana tingkat kualitas udara yang ada pada Provinsi DKI Jakarta. Dataset diperoleh melalui portal open data provinsi DKI Jakarta pada link: https://data.jakarta.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-2021

## Variabel Data:

* tanggal : Tanggal pengukuran kualitas udara
* stasiun : Lokasi pengukuran di stasiun
* pm10 : Partikulat salah satu parameter yang diukur
* pm25 : Partikulat salah satu parameter yang diukur
* so2 : Sulfida (dalam bentuk SO2) salah satu parameter yang diukur
* co : Carbon Monoksida salah satu parameter yand diukur
* o3 : Ozon salah satu parameter yang diukur
* no2 : NItrogen dioksida salah satu parameter yang diukur
* max : Nilai ukur paling tinggi dari seluruh parameter yang diukur dalam waktu yang sama
* critical : Parameter yang hasil pengukurannya paling tinggi
* categori : Kategori hasil perhitungan indeks standar pencemaran udara

# Data Preparation

## *importing Dataset*

Tahap pertama dalam melakukan data preparation adalah melakukan importing/membaca dataset yang akan digunakan menggunakan pandas karena data yang digunakan menggunakan format csv dalam filenya kemudian dilakukan pengecekan terhadap data secara keseluruhan untuk mengetahui jumlah baris dan kolomnya.
![image](https://user-images.githubusercontent.com/79986070/217539915-d42140e1-e7b5-4e64-b024-9007ba1da1c2.png)

## Menghapus colom yang tidak diperlukan

Tahap berikutnya adalah melakukan penghapusan kolom data yang tidak diperlukan seperti kolom tanggal dan kolom max dan critical yang berisi nilai terbesar dari salah satu nilai variabel

## Memeriksa informasi tipe data pada tiap variabel

tahap berikutnya adalah melakukan pengecekan rangkuman tipe data pada tiap tiap variabel paada dataset
![Screenshot (32)](https://user-images.githubusercontent.com/79986070/217543188-3e58370f-b180-47a5-b473-2f204347bf80.png)

## Memeriksa nilai kosong pada dataset
 tahap selanjutnya adalah melakukan pengecekan nilai Nan/nilai kosong pada tiap tiap kolom pada dataset kemudian menggantikan nilai pada kolom yang memiliki nilai kosong dengan nilai rata rata dari tiap kolom variabel pada dataset

![Screenshot (34)](https://user-images.githubusercontent.com/79986070/217544309-07a53885-2379-4b49-b361-f7c2b8ca6714.png)

#EDA
## Dataset Ploting

melakukan pengecekan jumlah pada tiap tiap variabel dengan menggunakan histogram
![Screenshot (35)](https://user-images.githubusercontent.com/79986070/217544953-73edf7c7-b029-44a5-9176-365b4bb8e789.png)

## *Dataset Correlation Check*

melakukan pengecekan terhadap keterkaitan antara satu variabel dengan variabel lainnya dengan menggunakan correlation matrix  yang dimana semakin tinggi atau semakin terang warna pada kolom matriks maka nilai keterkaitan antar variabel juga semakin tinggi
![Screenshot (36)](https://user-images.githubusercontent.com/79986070/217545591-d2f99ecc-64a7-410d-af62-58f0eebc7a5e.png)

## Cek persentase jumlah kategori kualitas udara

melakukan pengecekan jumlah persentase antara tiap tiap kategori yang dimana jika persentasenya semakin tinggi maka semakin banyak pula jumlah kategori yang terdapat pada dataset 
![Screenshot (37)](https://user-images.githubusercontent.com/79986070/217546558-a5d43fdf-1424-44c8-962a-7b90e40f84e2.png)

## Cek hubungan antar variabel terhadap kategori pada dataset

hal ini dilakukan untuk melakukan pemeriksaan hubungan keterkaitan antara tiap variabel indeks dengan kategori dengan menggunakan pairplot
![Screenshot (38)](https://user-images.githubusercontent.com/79986070/217547475-281bf59f-b1dd-4de1-8ffc-0b7917e87c34.png)

# Modelling

## Dataset Splitting

tahap pertama adalah melakukan Data splitting dengan membagi dataset menjadi X_train,y_train,X_test dan y_test dengan menggunakan train_test_split dengan test_size sebesar  20% dan training data sebesar 80% yang nantinya akan digunakan untuk dilatih dalam model *machine learning*

## Import and Define Model

tahap selanjutnya adalah melakukan importing model dari library scikit learn yaitu algoritma fungsi *LogisticRegresion* kemudian mendefinisikan fungsi model sebagai variabel logreg dengan parameter solver menggunakan 'lbfgs' yang dimana solver ini adalah nilai default untuk melakukan permasalahan klasifikasi multi kelas,parameter selanjutnya adalah nilai iterasi maksimal yang berada pada 400 iterasi
![Screenshot (40)](https://user-images.githubusercontent.com/79986070/217550689-61ca0968-ebf7-4a32-bfe8-397b84cc18b0.png)

## Model Fitting

tahapan selanjutnya adalah melakuka model fitting dengan menggunakan nilai X_train dan y_train yang telah dilakukan splitting pada beberapa tahap sebelumnya sebesar 80% untuk data training

# Evaluation

Proses evaluasi digunakan menggunakan nilai dari confussion matrix yang dimana model logisticregression mampu bekerja lebih baik karena menghasilkan nilai akurasi,recall dan f1 score dengan rata rata nilai sebesar 94%.
Nilai nilai matriks diatas dapat diperoleh melalui beberapa parameter berikut
* True Positive(TP): merupakan jumlah record data positif yang benar diklasifikasikan sebagai nilai positif
* False Negative(FN): merupakan jumlah record data positif yang diklasifikasikan sebagai nilai yang negative
* False Positive(FP): merupakan jumlah record data yang bernilai negative namun diklasifikasikan sebagai data yang memiliki nilai positif
* True Negative(TN): merupakan jumlah record data yang bernilai negative dan diklasifikasikan sebagai nilai yang negative.

Hasil dari Confussion Matrix akan digunakan sebagai acuan untuk perhitungan evaluasi dengan menggunakan F1 Score,Recall dan 
Precission serta tingkat akurasi.

* Precission: Precission dapat memberitahu kita mengenai seberapa banyak kasus prediksi benar yang ternyata positif. Nilai dari metriks ini dapat menentukan jika model dapat digunakan atau tidak [1]. 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 / 𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒
* Recall Metrics: Recall menunjukan jumlah kasus yang benar benar positif yang dapat diprediksi dengan benar menggunakan model. Nilai recall dapat diperoleh melalui persamaan berikut [1]: 𝑅𝑒𝑐𝑎𝑙𝑙 =𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 / 𝑇𝑟𝑢𝑒 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒
* F1 Score: F1 Score memberikan kita kombinasi data antara precision dan Recall,yang berarti jika kita mencoba meningkatkan nilai dari precision dan recall akan menurun begitu juga sebaliknya [1]. Nilai dari F1 Score dapat diperoleh melalui persamaan berikut: 𝐹1 𝑆𝑐𝑜𝑟𝑒 = 2 ∗(𝑝𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ∗ 𝑟𝑒𝑐𝑎𝑙𝑙)/(𝑝𝑟𝑒𝑐𝑖𝑠𝑠𝑖𝑜𝑛 + 𝑟𝑒𝑐𝑎𝑙𝑙)
* Accuracy: Accuracy merupakan sebuah fraksi dari sebuah prediksi yang benar dan total dari prediksi yang dibuat oleh pengklasifikasian [1].𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 =𝑇𝑟𝑢𝑒 𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝑇𝑟𝑢𝑒 𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒/𝑇𝑃 + 𝑇𝑁 + 𝐹𝑃 + 𝐹N
Berdasarkan perhitungan menggunakan berbagai formula diatas dapat disimpulkan bahwa model yang dibangun menggunakan LogisticRegression mampu melakukan klasifikasi kualitas udara berdasarkan parameter kandungan udara karena mampu menghasilkan rata rata nilai matriks diatas 90%

# References
[1] A. Tasnim, M. Saiduzzaman, M. A. Rahman, J. Akhter, and A. S. M. M. Rahaman, “Performance Evaluation of Multiple Classifiers for Predicting Fake News,” J. Comput. Commun., vol. 10, no. 09, pp. 1–21, 2022, doi: 10.4236/jcc.2022.109001.



