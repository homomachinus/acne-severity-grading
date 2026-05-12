# Analisis Komprehensif Klasifikasi Keparahan Akne Vulgaris
### Dari Metodologi Klinis Tradisional hingga Integrasi Kecerdasan Buatan dan Manajemen Nutrisi Berbasis Bukti

---

Manajemen klinis akne vulgaris, sebuah gangguan inflamasi kronis pada unit pilosebasea, tetap menjadi salah satu tantangan paling umum dalam dermatologi kontemporer di seluruh dunia. Meskipun kondisi ini secara dominan dikaitkan dengan populasi remaja, prevalensinya pada orang dewasa—terutama fenomena *adult-onset acne*—terus menunjukkan tren peningkatan, yang memerlukan pendekatan diagnosis dan pengobatan yang sangat bernuansa dan personal.

Kompleksitas jerawat berasal dari sifatnya yang pleomorfik, yang ditandai oleh beragam lesi. Penilaian tingkat keparahan penyakit yang akurat sangat krusial, bukan hanya untuk pemilihan terapi awal tetapi juga untuk pemantauan longitudinal efikasi pengobatan dan pencegahan sekuele permanen seperti jaringan parut (*scars*) dan hiperpigmentasi pasca-inflamasi (PIH).

---

## 1. Patogenesis dan Klasifikasi Morfologis Lesi

Memahami tingkat keparahan jerawat memerlukan pemahaman yang kuat tentang patogenesis yang mendasarinya. Pengembangan lesi jerawat didorong oleh interaksi multifaktorial dari:

- Hiperkeratinisasi folikel
- Peningkatan produksi sebum (*seborrhea*)
- Kolonisasi oleh *Cutibacterium acnes* (sebelumnya *Propionibacterium acnes*)
- Respons inflamasi yang kompleks

Penelitian terbaru menunjukkan bahwa inflamasi sebenarnya mungkin mendahului pembentukan mikrokomedo, dengan sel T-helper CD4+ dan makrofag muncul di sekitar folikel pada tahap paling awal perkembangan lesi, bahkan sebelum hiperkeratinisasi menjadi nyata secara klinis.

---

## 2. Klasifikasi Lima Kelas Lesi (Five-Class Lesion Taxonomy)

Dalam sistem klasifikasi yang digunakan pada penelitian ini, lesi akne vulgaris dikategorikan ke dalam **lima kelas** yang mencerminkan spektrum klinis dari non-inflamasi hingga inflamasi berat. Pembagian ini menyelaraskan terminologi visual yang lazim digunakan secara klinis dengan kebutuhan anotasi dataset untuk sistem berbasis kecerdasan buatan.

### 2.1 Blackhead (Komedo Terbuka)

Blackhead terbentuk ketika folikel rambut tersumbat oleh sebum dan debris keratinous, namun orifisium folikel tetap **terbuka** sehingga isinya terpapar udara. Proses oksidasi melanin dan lipid menciptakan tampilan gelap yang khas—bukan karena kotoran, melainkan karena reaksi kimiawi.

| Atribut | Deskripsi |
|---|---|
| Kategori | Non-inflamasi |
| Warna | Hitam hingga abu-abu gelap |
| Karakteristik | Pori melebar; permukaan rata atau sedikit menonjol |
| Risiko Jaringan Parut | Rendah |
| Konteks Patogenetik | Oksidasi keratin/sebum di permukaan kulit |

### 2.2 Whitehead (Komedo Tertutup)

Whitehead terjadi ketika folikel tersumbat namun **orifisium tetap tertutup** oleh lapisan epidermis tipis. Isi folikel tidak terpapar udara sehingga tidak mengalami oksidasi, menghasilkan tampilan putih atau sewarna kulit.

| Atribut | Deskripsi |
|---|---|
| Kategori | Non-inflamasi |
| Warna | Putih hingga sewarna kulit |
| Karakteristik | Benjolan kecil, bulat, permukaan halus |
| Risiko Jaringan Parut | Rendah |
| Konteks Patogenetik | Penyumbatan folikel di bawah epidermis |

### 2.3 Papule (Papul)

Papul merupakan progresi pertama dari lesi inflamasi. Dinding folikel yang melemah pecah dan menumpahkan sebum, keratin, serta bakteri ke dalam dermis di sekitarnya, memicu respons imun yang menghasilkan kemerahan dan pembengkakan tanpa purulensi yang terlihat.

| Atribut | Deskripsi |
|---|---|
| Kategori | Inflamasi |
| Warna | Merah hingga merah muda |
| Karakteristik | Benjolan padat, lunak, diameter < 1 cm, tanpa nanah terlihat |
| Risiko Jaringan Parut | Sedang |
| Konteks Patogenetik | Respons imun awal; dinding folikel pecah |

### 2.4 Pustule (Pustul)

Pustul secara morfologis serupa dengan papul namun memiliki **inti purulen sentral** yang terlihat. Akumulasi leukosit (neutrofil) sebagai respons terhadap *C. acnes* menghasilkan nanah berwarna putih atau kuning di pusat lesi.

| Atribut | Deskripsi |
|---|---|
| Kategori | Inflamasi |
| Warna | Dasar merah dengan puncak putih/kuning |
| Karakteristik | Berisi nanah, lunak saat disentuh, diameter bervariasi |
| Risiko Jaringan Parut | Sedang hingga tinggi |
| Konteks Patogenetik | Akumulasi leukosit; pembentukan nanah aktif |

### 2.5 Nodule (Nodul)

Nodul mewakili ujung spektrum inflamasi yang paling berat dalam klasifikasi lima kelas ini. Lesi ini bersifat padat, dalam, sangat nyeri, dan berdiameter lebih dari 1 cm. Nodul terbentuk akibat inflamasi dermal yang luas dan destruktif, dan membawa risiko signifikan terhadap pembentukan jaringan parut permanen.

> **Catatan Klinis**: Keberadaan nodul secara otomatis menggeser kategorisasi klinis ke arah spektrum "parah" hingga "sangat parah" dan umumnya mengindikasikan perlunya terapi sistemik.

| Atribut | Deskripsi |
|---|---|
| Kategori | Inflamasi berat |
| Warna | Merah gelap hingga ungu kemerahan |
| Karakteristik | Padat, dalam, sangat nyeri, diameter > 1 cm |
| Risiko Jaringan Parut | Tinggi hingga sangat tinggi |
| Konteks Patogenetik | Inflamasi dermal yang luas dan destruktif |

---

### Ringkasan Perbandingan Lima Kelas Lesi

| Kelas | Kategori | Visual Utama | Kedalaman | Risiko Parut |
|---|---|---|---|---|
| **Blackhead** | Non-inflamasi | Bintik hitam, pori terbuka | Superfisial | Rendah |
| **Whitehead** | Non-inflamasi | Bintik putih, tertutup kulit | Superfisial | Rendah |
| **Papule** | Inflamasi | Merah, padat, tanpa nanah | Mid-dermal | Sedang |
| **Pustule** | Inflamasi | Merah + pusat putih/kuning | Mid-dermal | Sedang–Tinggi |
| **Nodule** | Inflamasi berat | Besar, dalam, sangat nyeri | Dermal dalam | Tinggi |

---

## 3. Evolusi Sistem Klasifikasi Keparahan Klinis

Komunitas dermatologi secara historis kekurangan sistem klasifikasi tunggal yang diadopsi secara universal. Sistem awal berfokus pada kesan klinis subjektif, sementara metode selanjutnya berusaha memperkenalkan objektivitas melalui penghitungan lesi dan standar fotografi.

### 3.1 Sistem Pillsbury, Shelley, dan Kligman (1956)

Sistem Pillsbury adalah upaya besar pertama untuk menstandarisasi penilaian jerawat menggunakan skala empat tingkat berdasarkan jenis lesi dan distribusinya.

- **Derajat 1**: Komedo dan kista kecil sesekali, terbatas pada wajah
- **Derajat 2**: Lebih banyak komedo dan lesi inflamasi ringan
- **Derajat 3**: Banyak lesi inflamasi, mulai melibatkan leher dan punggung atas
- **Derajat 4**: Lesi dalam yang menyatu (*confluent*) pada wajah dan tubuh bagian atas

Sistem ini sering dikritik karena terlalu reduktif dan gagal memperhitungkan perubahan halus dalam respons terapeutik. Namun, terminologi "Grade 1–4" tetap menjadi dasar bagi banyak klasifikasi modern.

### 3.2 Teknik Leeds dan Penilaian Revisi (1984, 1998)

Teknik Leeds memperkenalkan pendekatan yang lebih granular menggunakan **skala 0 hingga 10**, dengan pembagian:

- **Acne minor**: Derajat 0,25 hingga 1,5 (sering fisiologis, awal pubertas)
- **Acne major**: Derajat 1,5 ke atas (memerlukan intervensi klinis)

Revisi tahun 1998 menambahkan standar fotografi untuk wajah, punggung, dan dada, meningkatkan *inter-rater reliability* secara signifikan—sangat berguna dalam uji klinis di mana perubahan kecil jumlah lesi perlu didokumentasikan dengan akurasi tinggi.

### 3.3 Global Acne Grading System (GAGS)

Dikembangkan pada tahun 1997 oleh Doshi, Zaheer, dan Stiller, GAGS saat ini merupakan salah satu alat yang paling banyak digunakan dalam penelitian dan praktik klinis karena sifatnya yang **kuantitatif dan komprehensif**.

**Formula**: `Skor Lokal = Faktor Area × Grade Lesi Terparah`

Skor global adalah jumlah dari seluruh skor lokal.

| Lokasi | Faktor Area | Grade Lesi (0–4) |
|---|---|---|
| Dahi | 2 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |
| Pipi Kanan | 2 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |
| Pipi Kiri | 2 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |
| Hidung | 1 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |
| Dagu | 1 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |
| Dada & Punggung Atas | 3 | 0: Tidak ada, 1: Blackhead/Whitehead, 2: Papule, 3: Pustule, 4: Nodule |

**Klasifikasi berdasarkan total skor GAGS:**

| Skor | Tingkat Keparahan |
|---|---|
| 1–18 | Ringan (*Mild*) |
| 19–30 | Sedang (*Moderate*) |
| 31–38 | Parah (*Severe*) |
| > 39 | Sangat Parah (*Very Severe*) |

Sistem ini sangat dihargai karena kecepatannya dan kemampuannya untuk memperhitungkan *truncal acne* (jerawat pada tubuh), yang seringkali diabaikan sistem lain.

> **Penyesuaian Klasifikasi Lima Kelas**: Dalam konteks sistem lima kelas yang digunakan di sini, **blackhead dan whitehead** menempati Grade 1 pada skala GAGS karena keduanya bersifat non-inflamasi. **Papule** = Grade 2, **Pustule** = Grade 3, dan **Nodule** = Grade 4.

### 3.4 Investigator's Global Assessment (IGA)

IGA adalah skala statis yang menggambarkan gambaran klinis secara keseluruhan pada satu titik waktu menggunakan **skala 5 poin (0–4)**:

| Skor IGA | Deskripsi |
|---|---|
| 0 | Bersih (*Clear*) — Tidak ada lesi |
| 1 | Hampir Bersih — Lesi sangat minimal, hampir tidak terlihat |
| 2 | Ringan — Beberapa papule/pustule, sedikit nodule |
| 3 | Sedang — Banyak papule/pustule, beberapa nodule |
| 4 | Parah — Banyak nodule, lesi inflamasi luas |

Meskipun digunakan secara luas dalam uji klinis yang dimandatkan FDA, IGA tetap bersifat subjektif dan dapat menyebabkan variabilitas antar dokter.

---

## 4. Klasifikasi Berbasis Citra dan Peran Kecerdasan Buatan (AI)

Subjektivitas yang melekat pada penilaian klinis manual telah mendorong lonjakan pengembangan alat visi komputer dan kecerdasan buatan (AI) untuk penilaian jerawat.

### 4.1 Deep Learning dan Convolutional Neural Networks (CNN)

Sistem AI modern untuk jerawat biasanya menggunakan *Convolutional Neural Networks* (CNN), yang sangat mahir dalam mengenali pola kompleks dalam data gambar. Penelitian terbaru telah menggunakan paradigma pelatihan berbasis CenterNet untuk mendeteksi dan mengkategorikan lesi dengan **akurasi sekitar 83%**, secara signifikan melampaui model ResNet-18 yang lebih lama.

Tantangan signifikan dalam AI dermatologi adalah **bias historis dalam dataset pelatihan**. Banyak model awal dilatih terutama pada kulit Kaukasia, yang mungkin tidak diterjemahkan secara akurat ke kelompok etnis lain karena perbedaan presentasi lesi dan risiko PIH yang lebih tinggi pada tipe kulit Fitzpatrick IV–VI.

### 4.2 Alur Kerja Pemrosesan Gambar Otomatis

Dalam konteks sistem lima kelas (blackhead, whitehead, papule, pustule, nodule), alur kerja AI yang ideal mencakup tahapan berikut:

**Tahap 1 — Penilaian Kualitas Gambar**
Model AI menilai apakah gambar input memiliki pencahayaan yang memadai dan bebas dari halangan seperti rambut atau kacamata.

**Tahap 2 — Segmentasi Semantik**
Masker segmentasi diterapkan untuk mengisolasi hanya wilayah kulit yang berpotensi terkena jerawat, mencegah analisis area tidak relevan (latar belakang, bibir, mata).

**Tahap 3 — Deteksi dan Klasifikasi Lima Kelas**
Model mendeteksi dan mengklasifikasikan setiap lesi individu ke dalam satu dari lima kelas: **blackhead, whitehead, papule, pustule, atau nodule**. Pendekatan ini lebih transparan dibanding penilaian "kotak hitam" karena menyelaraskan logika AI dengan kriteria morfologis yang digunakan dokter kulit.

**Tahap 4 — Prediksi Keparahan**
Output akhir berupa skor IGA atau GAGS yang diturunkan dari jumlah lesi, distribusi spasialnya, dan dominansi kelas lesi tertentu—terutama keberadaan nodule sebagai penanda keparahan.

### 4.3 Relevansi Klasifikasi Lima Kelas dalam Konteks AI

Penggunaan lima kelas yang terdefinisi jelas (blackhead, whitehead, papule, pustule, nodule) memberikan sejumlah keunggulan untuk sistem berbasis AI:

- **Granularitas lebih tinggi** dibanding sistem dua kelas (inflamasi vs non-inflamasi)
- **Selaras dengan terminologi klinis** yang lazim digunakan dokter spesialis kulit
- **Memungkinkan penghitungan per kelas** untuk pemantauan longitudinal yang lebih akurat
- **Mendukung prioritisasi terapi** berdasarkan distribusi kelas lesi yang terdeteksi

---

## 5. Strategi Manajemen Farmakologis Berdasarkan Tingkat Keparahan

Strategi pengobatan untuk akne vulgaris didikte oleh tingkat keparahan kondisi, jenis lesi yang dominan, dan riwayat serta faktor risiko individu pasien. Pedoman *American Academy of Dermatology* (AAD) tahun 2024 menekankan pendekatan multimodal yang menggabungkan mekanisme aksi berbeda secara simultan.

### 5.1 Jerawat Ringan — Dominasi Blackhead dan Whitehead

Fokus utama adalah normalisasi keratinisasi folikel dan reduksi komedogenesis.

- **Retinoid topikal** (adapalene, tretinoin, tazarotene, trifarotene): standar emas untuk mencegah pembentukan blackhead dan whitehead baru melalui normalisasi epitel folikel
- **Benzoyl Peroxide (BPO) topikal**: sifat antibakteri kuat; mencegah resistensi bakteri saat dikombinasikan dengan antibiotik
- **Asam salisilat** atau **asam azelaat**: alternatif untuk kulit sensitif; asam azelaat juga mencerahkan PIH

### 5.2 Jerawat Sedang — Papule dan Pustule Dominan

Kepadatan lesi inflamasi lebih tinggi; tanda awal jaringan parut mulai mungkin terlihat.

- **Kombinasi dosis tetap**: BPO/Adapalene atau BPO/Clindamycin — mengatasi *C. acnes* dan kaskade inflamasi secara bersamaan; lebih unggul dari monoterapi
- **Antibiotik sistemik** (doksisiklin, minosiklin, saresiklin): maksimum 12 minggu; tidak boleh sebagai monoterapi
- **Terapi hormonal** (wanita): kontrasepsi oral kombinasi (COC) atau spironolakton untuk pemicu hormonal

### 5.3 Jerawat Parah — Nodule Dominan

Keberadaan banyak nodule dengan nyeri signifikan dan risiko tinggi jaringan parut permanen.

- **Isotretinoin oral**: satu-satunya pengobatan yang mengatasi keempat faktor patogenetik sekaligus (produksi sebum, komedogenesis, jumlah bakteri, inflamasi). Dosis kumulatif standar 120–150 mg/kg
- **Kortikosteroid intralesi** (triamsinolon asetonid): untuk nodule tunggal yang besar dan sangat nyeri
- **Agen biologis** (inhibitor TNF-α, IL-17/IL-23): untuk kasus refrakter ekstrem seperti sindrom SAPHO

### 5.4 Ringkasan Terapi Berdasarkan Bukti

| Tingkat Keparahan | Lesi Dominan | Terapi Utama | Mekanisme Utama |
|---|---|---|---|
| Ringan | Blackhead, Whitehead | Retinoid Topikal, BPO, Asam Salisilat | Keratolisis, Antibakteri permukaan |
| Sedang | Papule, Pustule | Kombinasi Topikal + Antibiotik Oral (maks 12 mgg) | Inflamasi sistemik, jumlah *C. acnes* |
| Parah | Nodule | Isotretinoin Oral, Spironolakton (wanita) | Produksi sebum, inflamasi kistik dalam |
| Pemeliharaan | — | Retinoid Topikal ± BPO | Pencegahan mikrokomedo baru |

---

## 6. Peran Nutrisi dan Suplementasi Oral

Peran diet dalam jerawat telah mengalami pergeseran paradigma yang signifikan dalam dua dekade terakhir—dari dianggap mitos menjadi komponen terapeutik berbasis bukti yang semakin diakui.

### 6.1 Indeks Glikemik dan IGF-1

Diet dengan indeks glikemik (GI) tinggi memicu hiperinsulinemia, yang merangsang produksi *Insulin-Like Growth Factor 1* (IGF-1). IGF-1 mempromosikan hiperplasia kelenjar sebasea dan meningkatkan produksi sebum—khususnya memperburuk lesi inflamasi seperti **papule, pustule, dan nodule**. Diet rendah GI terbukti secara signifikan mengurangi jumlah lesi.

### 6.2 Produk Susu dan Protein Whey

Susu skim mengandung hormon dan molekul bioaktif yang merangsang poros IGF-1. Protein whey memiliki efek insulinotropik tinggi dan didokumentasikan dapat memicu munculnya lesi inflamasi yang tiba-tiba—terutama **pustule dan nodule**—pada pengguna suplemen binaragawan.

### 6.3 Suplementasi Mikronutrisi

#### Seng (Zinc)

Seng adalah mineral yang paling banyak dipelajari dalam konteks jerawat. Mekanismenya mencakup penghambatan ekspresi Toll-Like Receptor 2 (TLR2) pada keratinosit dan pengurangan sitokin pro-inflamasi—efektif terutama pada **papule dan pustule**.

| Parameter | Detail |
|---|---|
| Bentuk direkomendasikan | Seng glukonat (toleransi GI lebih baik dari seng sulfat) |
| Kandungan elemental | ~14% — tablet 100 mg = 14 mg seng elemental |
| Dosis efektif | 30–100 mg seng elemental/hari |
| Efek samping | Mual, nyeri lambung (diminimalisir dengan konsumsi bersama makanan) |

#### Vitamin D

Defisiensi Vitamin D lebih umum pada pasien akne dibanding kontrol sehat. Vitamin D mengatur respons imun terhadap *C. acnes* melalui reseptor yang ditemukan dalam sebosit. Suplementasi **1.000 IU/hari** terbukti memperbaiki lesi inflamasi pada pasien dengan defisiensi terdokumentasi.

#### Vitamin A Oral

Efek anti-keratinisasi yang kuat membantu menekan pembentukan **blackhead dan whitehead**. Namun, dosis tinggi (hingga 100.000 IU/hari) membawa risiko serius: teratogenisitas dan toksisitas hati. Sebagian besar peran ini kini diambil alih oleh isotretinoin dengan protokol keamanan yang lebih mapan.

#### Omega-3 (EPA/DHA)

Menghambat produksi leukotrien B4 (LTB4), mediator inflamasi utama dalam pembentukan **papule, pustule, dan nodule**. Dosis efektif umumnya 2–3 g EPA+DHA per hari.

#### Probiotik

Strain seperti *Lactobacillus rhamnosus* SP1 terbukti mengurangi ekspresi IGF-1 dan memperbaiki tampilan jerawat melalui mekanisme poros "usus-kulit" (*gut-skin axis*). Juga membantu memitigasi efek samping GI akibat antibiotik jangka panjang.

### 6.4 Tabel Perbandingan Suplemen

| Nutrisi | Bentuk Rekomendasi | Bukti Klinis | Risiko & Efek Samping |
|---|---|---|---|
| Seng | Seng glukonat | Mengurangi lesi inflamasi; menghambat TLR2 | Mual, nyeri lambung |
| Vitamin A | Retinol / Retinil Ester | Efek anti-keratinisasi kuat | Risiko cacat lahir; toksik hati |
| Vitamin D | Kolekalsiferol (D3) | Memperbaiki respons imun folikel | Hiperkalsemia (dosis ekstrem) |
| Omega-3 | Minyak Ikan (EPA/DHA) | Menghambat produksi leukotrien B4 | Rasa amis; pengencer darah ringan |
| Laktoferin | Protein Susu | Menurunkan sebum dan jumlah bakteri | Relatif aman; biaya lebih tinggi |
| Probiotik | *L. rhamnosus*, *B. bifidum* | Mengatur poros usus-kulit; reduksi IGF-1 | Kembung ringan di awal konsumsi |

---

## 7. Panduan Perawatan Kulit dan Gaya Hidup

### 7.1 Pembersihan dan Hidrasi

- **Pembersih**: Gunakan produk dengan pH 5,5–7,0 (syndets atau pembersih cair). Sabun batangan alkalin mengganggu mantel asam kulit dan memperburuk inflamasi. Frekuensi: dua kali sehari.
- **Pelembap**: Bahkan kulit berminyak memerlukan hidrasi, terutama saat menggunakan BPO atau retinoid. Pelembap berbasis ceramide direkomendasikan untuk memperbaiki *skin barrier* dan mengurangi *transepidermal water loss* (TEWL).
- **Label non-komedogenik**: Semua produk topikal—termasuk tabir surya dan kosmetik—harus berlabel "non-komedogenik" atau "oil-free".

### 7.2 Faktor Mekanis dan Lingkungan

- **Hindari memencet lesi**: Ekstrusi manual mendorong materi inflamasi lebih dalam ke dermis, meningkatkan risiko jaringan parut dan PIH secara signifikan—terutama berbahaya untuk **nodule**. Blackhead dapat diekstraksi secara profesional setiap 3–4 minggu.
- **Proteksi UV**: Retinoid dan doksisiklin meningkatkan fotosensitivitas. Penggunaan tabir surya non-komedogenik setiap hari adalah wajib.
- **Manajemen stres dan tidur**: Kortisol yang meningkat akibat stres emosional merangsang produksi sebum, yang berkontribusi pada pembentukan blackhead, whitehead, dan lesi inflamasi berikutnya.

---

## 8. Sintesis dan Kesimpulan

Klasifikasi dan manajemen akne vulgaris telah berevolusi menjadi bidang yang sangat khusus, mengintegrasikan penilaian morfologis klasik dengan teknologi kecerdasan buatan mutakhir dan ilmu nutrisi berbasis bukti.

Penggunaan **sistem lima kelas lesi—blackhead, whitehead, papule, pustule, dan nodule**—memberikan kerangka kerja yang lebih presisi dibanding dikotomi sederhana inflamasi/non-inflamasi. Sistem ini:

- Menyelaraskan terminologi klinis dengan kebutuhan anotasi dataset AI
- Memungkinkan pemetaan langsung ke sistem skoring seperti GAGS dan IGA
- Mendukung penentuan terapi yang lebih tepat sasaran berdasarkan dominansi kelas lesi
- Memfasilitasi pemantauan longitudinal yang lebih akurat terhadap respons terapeutik

Secara klinis, penekanan saat ini bergeser ke arah pengawasan antibiotik (*antibiotic stewardship*) dengan preferensi pada terapi kombinasi dosis tetap dan penggunaan isotretinoin yang strategis—khususnya pada kasus dengan dominansi nodule. Pengakuan terhadap poros IGF-1 sebagai pendorong patogenesis menegaskan pentingnya intervensi diet, termasuk pengurangan beban glikemik dan suplementasi seng glukonat serta probiotik sebagai adjuvan bernilai.

Untuk mencapai hasil optimal, rencana perawatan komprehensif harus menangani aspek medis, nutrisi, dan perilaku secara simultan—tidak hanya memberikan pembersihan lesi fisik, tetapi juga meminimalkan risiko sekuele permanen seperti jaringan parut dan PIH, serta memperbaiki kualitas hidup dan beban psikososial yang sering menyertai kondisi kronis ini.

---

*Referensi utama: AAD Guidelines 2024, GAGS (Doshi et al., 1997), Leeds Revised Technique (1998), IGA FDA Framework, serta literatur terpilih mengenai gut-skin axis dan AI-based acne grading.*
