hommomachinus

## Roadmap: Deteksi Jerawat

### [ ] **1. Persiapan Dataset & Konfigurasi Dasar**

Langkah awal untuk memastikan data siap dikonsumsi oleh model.

* **Hyperparameters:**
* Ukuran Gambar: 640 x 640
* Batch Size: 16
* Epochs: 50


* **Struktur Dataset (YOLO Format):**
* `images/` (Train & Validation)
* `labels/` (Annotation files dalam format .txt)


* **Definisi Kelas:**
* `0: acne_mild`
* `1: acne_moderate`
* `2: acne_severe`



---

### [ ] **2. Data Augmentation & Pre-processing**

Mengolah data agar model lebih tangguh (robust) terhadap variasi kondisi input.

* **Teknik Augmentasi:**
* Horizontal Flip & Rotation (mengatasi variasi sudut wajah).
* Zoom & Brightness Adjustment (mengatasi variasi jarak dan pencahayaan).
* **Mosaic Augmentation:** Menggabungkan 4 gambar menjadi satu untuk membantu model mendeteksi objek kecil.



---

### [ ] **3. Arsitektur Model & Konfigurasi Training**

Menyiapkan "otak" model dan menentukan cara ia belajar.

* **Load Model:** Menggunakan `YOLOv8n` (Nano) sebagai base model agar ringan dan cepat.
* **Layer Freezing:** Membekukan layer awal (*backbone*) untuk menjaga fitur dasar (seperti garis dan tekstur) yang sudah dipelajari dari dataset masif (ImageNet/COCO).
* **Setting Input:** Mengunci input pada 640x640 dengan 3 kelas output.
* **Optimizer:** Menggunakan **AdamW** dengan *Learning Rate* $0.001$ untuk stabilitas konvergensi.

---

### [ ] **4. Proses Eksekusi Training & Validasi**

Menjalankan mesin pelatihan dan memantau perkembangannya.

* **Training Loop:** Melatih model menggunakan dataset `train`.
* **Validation Loop:** Melakukan pengujian pada dataset `validation` setiap akhir epoch untuk mencegah *overfitting*.

---

### [ ] **5. Evaluasi Performa & Metrik**

Menganalisis seberapa akurat model dalam mengenali jerawat.

* **Metrik Utama:**
* **mAP50:** Mean Average Precision pada IoU threshold 0.5.
* **Precision:** Seberapa akurat prediksi positif model.
* **Recall:** Seberapa banyak objek jerawat yang berhasil ditemukan model.


* **Monitoring:** Memantau grafik *Validation Loss* untuk memastikan penurunan error yang konsisten.

---

### [ ] **6. Finalisasi & Ekspor Model**

Mengubah model hasil training ke format yang siap digunakan di berbagai platform.

* **Penyimpanan:** Menyimpan file bobot terbaik (`best.pt`).
* **Format Ekspor:**
* **TensorFlow Lite:** Untuk deployment di aplikasi Android/iOS.
* **ONNX:** Untuk integrasi universal di berbagai runtime.
* **TorchScript:** Untuk performa tinggi di lingkungan produksi berbasis C++.



---

**Saran kecil:** Karena jerawat seringkali berukuran kecil, pastikan saat proses *Labeling*, kotak pembatas (*bounding box*) dibuat sepresisi mungkin agar mAP50 Anda tidak "terjun bebas". Ada bagian spesifik dari konfigurasi ini yang ingin Anda bedah lebih dalam?
