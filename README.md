# Lumoshive Challenge: The Mirror Equation

<div align="center">
<img src="https://lumoshive.com/assets/newUI/logo.png" alt="lumoshive image" />
</div>

Solusi ini dikembangkan untuk menyelesaikan tantangan "The Mirror Equation" dari Lumoshive, dengan mematuhi semua batasan yang ditetapkan, terutama larangan penggunaan fungsi _built-in_ Python untuk _parsing_ dan pembalikan string.

## Soal

diberikan sebuah persamaan dalam bentuk string: "a + b = c"
Tapi ada yang salah! Salah satu angka TERBALIK (reversed). Tentukan angka mana yang terbalik, dan beberapa seharusnya angka yang benar

## Aturan

- Terbalik = reverse urutan digit `(123 -> 321)`
- Hanya satu angka yang salah
- Prioritas pengecekan: **a, b, c**

## Input

- String persamaan: "a+b = c"
- Format selalu:
  - "angka + angka = angka"

## Output

- correct jika sudah benar
- a,nilai_benar jika a yang salah
- b,nilai_benar jika b yang salah
- c,nilai_benar jika c yang salah
- no solution jika tidak ada yang cocok

---

### Contoh

```bash
input: "12 + 34 = 64"
- Cek: 12 + 34 = 46 (bukan 64)
- 64 terbalik = 46
- Output: "c,46"
```

```bash
input: "15 + 51 = 66"
- Cek: 15 + 51 = 66
- 64 terbalik = 46
- Output: "correct"
```

```bash
input: "16 + 23 = 93"
- Cek: 16 + 23 = 39 (bukan 93)
- 93 terbalik = 39
- Output: "c,39"
```

```bash
input: "21 + 34 = 55"
- Cek: 21 + 34 = 55
- Output: "correct"
```

## Batasan

- Tidak boleh pakai `regex`
- Tidak boleh pakai `eval()`
- Tidak boleh pakai built-in split/reverse/join untuk parsing
- Manual parsing selain loop

---

## Strategi Penyelesaian

Penyelesaian masalah ini dibagi menjadi tiga langkah utama, yang semuanya diimplementasikan secara manual untuk mematuhi batasan:

### 1. Parsing Persamaan (Fungsi `parse_equation`)

Karena dilarang menggunakan fungsi `split()`, proses pemisahan string persamaan `"a + b = c"` menjadi tiga komponen angka (`a_str`, `b_str`, `c_str`) dilakukan menggunakan **State Machine** sederhana.

- **State 0 (Membaca A):** Karakter digit yang ditemukan akan ditambahkan ke `a_str`. Transisi ke State 1 terjadi saat karakter `+` ditemukan.
- **State 1 (Membaca B):** Karakter digit yang ditemukan akan ditambahkan ke `b_str`. Transisi ke State 2 terjadi saat karakter `=` ditemukan.
- **State 2 (Membaca C):** Karakter digit yang ditemukan akan ditambahkan ke `c_str`.

Karakter lain (seperti spasi) diabaikan. Setelah _parsing_, ketiga string angka dikonversi menjadi integer.

### 2. Pembalikan String (Fungsi `reverse_string`)

Batasan melarang penggunaan `s[::-1]` atau `reversed()`. Fungsi `reverse_string` mengimplementasikan pembalikan string secara manual:

- String baru (`reversed_s`) diinisialisasi sebagai string kosong.
- Setiap karakter dari string input di-_loop_ dan ditambahkan di **depan** string baru.
- Contoh: Untuk input `"123"`, prosesnya adalah:
  - `'1'` + `""` → `"1"`
  - `'2'` + `"1"` → `"21"`
  - `'3'` + `"21"` → `"321"`

### 3. Logika Pengecekan (Fungsi `solve_mirror_equation`)

Logika utama mengikuti aturan dan prioritas pengecekan:

1.  **Cek Awal:** Periksa apakah persamaan sudah benar (`a + b == c`). Jika ya, kembalikan `"correct"`.
2.  **Cek Angka A:** Balikkan angka `a`. Periksa apakah persamaan menjadi benar dengan `a_terbalik + b == c`. Jika ya, kembalikan `a,nilai_benar`.
3.  **Cek Angka B:** Balikkan angka `b`. Periksa apakah persamaan menjadi benar dengan `a + b_terbalik == c`. Jika ya, kembalikan `b,nilai_benar`.
4.  **Cek Angka C:** Balikkan angka `c`. Periksa apakah persamaan menjadi benar dengan `a + b == c_terbalik`. Jika ya, kembalikan `c,nilai_benar`.
5.  **Tidak Ada Solusi:** Jika semua pengecekan gagal, kembalikan `"no solution"`.

**Penting:** Pengecekan untuk `a`, `b`, dan `c` dilakukan secara berurutan sesuai prioritas. Begitu satu kondisi terpenuhi, proses berhenti dan hasilnya dikembalikan.

## Cara Menjalankan Kode

Kode ini telah dibuat dinamis untuk menerima input dari baris perintah atau dari _standard input_ (ketika dijalankan tanpa argumen).

### Opsi 1: Input melalui Command Line

```bash
python3 mirror_equation.py "12 + 34 = 64"
# Output: c,46
```

### Opsi 2: Input Interaktif

Jalankan skrip tanpa argumen, dan Anda akan diminta untuk memasukkan persamaan:

```bash
python3 mirror_equation.py
Masukkan persamaan (contoh: 12 + 34 = 64):
16 + 23 = 93
# Output: c,39
```

<img src="https://i.pinimg.com/736x/5d/d5/9f/5dd59fa3a2be962bc0ae33ba4334271a.jpg" alt="Background image"/>
