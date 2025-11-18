import sys

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def parse_equation(equation_string):
    a_str = ""
    b_str = ""
    c_str = ""
    
    # State machine for parsing:
    # 0: baca a_str (before '+')
    # 1: baca b_str (after '+' and before '=')
    # 2: baca c_str (after '=')
    state = 0
    
    for char in equation_string:
        if char.isdigit():
            if state == 0:
                a_str += char
            elif state == 1:
                b_str += char
            elif state == 2:
                c_str += char
        elif char == '+':
            # Transisi dari a_str ke b_str
            state = 1
        elif char == '=':
            # Transisi dari b_str ke c_str
            state = 2

    return a_str, b_str, c_str

def solve_mirror_equation(equation_string):
    a_str, b_str, c_str = parse_equation(equation_string)
    
    # Konversi ke integer
    try:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    except ValueError:
        return "Error: Format input tidak valid. Pastikan formatnya 'angka + angka = angka'."

    # 1. Cek apakah persamaan sudah benar
    if a + b == c:
        return "correct"

    # --- Cek angka yang dibalik berdasarkan prioritas (a, b, c) ---
    # 2. Cek apakah 'a' adalah angka yang dibalik
    a_rev_str = reverse_string(a_str)
    a_correct = int(a_rev_str)
    if a_correct + b == c:
        return f"a,{a_correct}"

    # 3. Cek apakah 'b' adalah angka yang dibalik
    b_rev_str = reverse_string(b_str)
    b_correct = int(b_rev_str)
    if a + b_correct == c:
        return f"b,{b_correct}"

    # 4. Cek apakah 'c' adalah angka yang dibalik
    c_rev_str = reverse_string(c_str)
    c_correct = int(c_rev_str)
    if a + b == c_correct:
        return f"c,{c_correct}"

    # 5. Tidak ada solusi yang ditemukan berdasarkan aturan
    return "no solution"

if __name__ == '__main__':
    # Baca input dari argumen baris perintah
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
    # Baca input dari standar input (lebih dinamis)
    else:
        print("Masukkan persamaan (contoh: 12 + 34 = 64):")
        try:
            input_str = sys.stdin.readline().strip()
        except EOFError:
            print("Tidak ada input yang diberikan.")
            sys.exit(1)
        
        if not input_str:
            print("Input kosong. Silakan masukkan persamaan.")
            sys.exit(1)

    result = solve_mirror_equation(input_str)
    print(result)
