# Lumoshive Challenge: The Mirror Equation 🐋

<div align="center">
<img src="https://lumoshive.com/assets/newUI/logo.png" alt="lumoshive image" />
</div>

coding chalengge

## Soal

diberikan sebuah persamaan dalam bentuk string: "a + b = c"
Tapi ada yang salah! Salah satu angka TERBALIK (reversed). Tentukan angka mana yang terbalik, dan beberapa seharusnya angka yang benar

## Aturan

- Terbalik = reverse urutan digit `(123 -> 321)`
- Hanya satu angka yang salah
- Prioritas pengecekan: **a, b, c**

## Input

## Output

---

### Contoh

```bash
input: "12 + 34 = 64"
- Cek: 12 + 34 = 46 (bukan 64)
- 64 terbalik = 46 # Benar
- Output: "c,46"
```

```bash
input: "15 + 51 = 66"
- Cek: 15 + 51 = 66 #Benar
- 64 terbalik = 46
- Output: "correct"
```

```bash
input: "15 + 51 = 66"
- Cek: 15 + 51 = 66 #Benar
- 64 terbalik = 46
- Output: "correct"
```

```bash
input: "15 + 51 = 66"
- Cek: 15 + 51 = 66 #Benar
- 64 terbalik = 46
- Output: "correct"
```

## Batasan

- Tidak boleh pakai `regex`
- Tidak boleh pakai `eval()`
- Tidak boleh pakai built-in split/reverse/join untuk parsing
- Manual parsing selain loop

---

<img src="https://i.pinimg.com/736x/5d/d5/9f/5dd59fa3a2be962bc0ae33ba4334271a.jpg" alt="Background image"/>
