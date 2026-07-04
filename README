# Implementasi Program Compiler Sederhana
## Do-While dengan Percabangan If-Else dan Three-Address Code (TAC)

**Mata Kuliah:** Kompilasi  
**Bahasa Pemrograman:** Python

---

# 1. Pendahuluan

Program ini merupakan simulasi sederhana proses kerja compiler. Program menerima source code berupa struktur **do-while** yang di dalamnya terdapat percabangan **if-else**, kemudian melakukan beberapa tahapan kompilasi yaitu:

1. Lexical Analysis
2. Syntax & Semantic Analysis
3. Generasi Three-Address Code (TAC)

Program ini dibuat sebagai media pembelajaran untuk memahami bagaimana compiler mengubah source code menjadi representasi kode antara.

---

# 2. Tujuan Program

Tujuan dari program ini adalah:

- Memahami proses Lexical Analysis.
- Memahami proses Syntax Analysis.
- Memahami proses Semantic Analysis.
- Menghasilkan Three-Address Code (TAC).
- Mensimulasikan proses kerja compiler sederhana.

---

# 3. Pattern BNF

Program menggunakan aturan grammar berikut.

```bnf
<program> ::= <do_while>

<do_while> ::= "do" "{"
                 <if_else>
               "}"
               "while"
               "(" <condition> ")"

<if_else> ::= "if"
              "(" <condition> ")"
              "{"
                <statement>
              "}"
              "else"
              "{"
                <statement>
              "}"

<condition> ::= <identifier> <operator> <value>

<statement> ::= <identifier> "=" <value>

<identifier> ::= x | y | z

<operator> ::= > | < | >= | <= | == | !=

<value> ::= angka
```

---

# 4. Source Code

Source code yang digunakan sebagai input adalah:

```c
do {
    if (x > 5) {
        y = 1;
    } else {
        y = 0;
    }
} while (x < 10);
```

---

# 5. Tahapan Implementasi

## 5.1 Constructor

```python
def __init__(self, source_code):
```

Constructor digunakan untuk menyimpan source code yang akan diproses serta menginisialisasi nomor label.

Variabel yang digunakan:

- source_code
- label_counter

---

## 5.2 Fungsi new_label()

```python
def new_label(self):
```

Fungsi ini digunakan untuk membuat label secara otomatis.

Contoh hasil:

```
L1
L2
L3
```

Label digunakan sebagai tujuan instruksi **goto** pada TAC.

---

## 5.3 Lexical Analysis

```python
def lexical_analysis(self):
```

Tahapan ini memecah source code menjadi token-token.

Contoh token yang dihasilkan:

```
do
{
if
(
x
>
5
)
{
y
=
1
;
}
else
{
y
=
0
;
}
}
while
(
x
<
10
)
;
```

Hasil token:

```
['do', '{', 'if', '(', 'x', '>', '5', ')', '{', 'y', '=', '1', ';', '}', 'else', '{', 'y', '=', '0', ';', '}', '}', 'while', '(', 'x', '<', '10', ')', ';']
```

Tahapan ini hanya memecah karakter menjadi token tanpa memeriksa struktur program.

---

## 5.4 Syntax Analysis

Tahap ini melakukan pengecekan apakah struktur program telah sesuai grammar.

Compiler memeriksa:

- terdapat keyword do
- terdapat keyword while
- terdapat keyword if
- terdapat keyword else
- kondisi berada di dalam tanda ()
- statement berada di dalam tanda {}

Apabila struktur tidak sesuai maka program menghasilkan Syntax Error.

---

## 5.5 Semantic Analysis

Tahapan semantic memastikan isi program dapat diproses.

Compiler mengambil:

- kondisi if
- isi blok if
- isi blok else
- kondisi while

Hasil yang diperoleh:

```
Kondisi IF

x > 5

Isi IF

y = 1

Isi ELSE

y = 0

Kondisi WHILE

x < 10
```

---

## 5.6 Three-Address Code (TAC)

Tahap terakhir adalah menghasilkan kode antara.

TAC yang dihasilkan:

```
L1:
ifFalse x > 5 goto L2
y = 1
goto L3
L2:
y = 0
L3:
if x < 10 goto L1
```

Penjelasan:

- L1 merupakan awal perulangan do-while.
- ifFalse digunakan untuk mengecek kondisi if.
- goto digunakan untuk berpindah ke label tertentu.
- L2 merupakan blok else.
- L3 merupakan akhir percabangan.
- Jika kondisi while masih benar maka program kembali ke L1.

---

# 6. Alur Program

```
Source Code
      │
      ▼
Lexical Analysis
      │
      ▼
Syntax Analysis
      │
      ▼
Semantic Analysis
      │
      ▼
Generate Three Address Code
      │
      ▼
Output TAC
```

---

# 7. Contoh Output

## Token

```
['do', '{', 'if', '(', 'x', '>', '5', ')', '{', 'y', '=', '1', ';', '}', 'else', '{', 'y', '=', '0', ';', '}', '}', 'while', '(', 'x', '<', '10', ')', ';']
```

## TAC

```
L1:
ifFalse x > 5 goto L2
y = 1
goto L3
L2:
y = 0
L3:
if x < 10 goto L1
```

---

# 8. Kesimpulan

Program berhasil mensimulasikan tahapan dasar compiler menggunakan bahasa Python. Tahapan yang dilakukan meliputi Lexical Analysis, Syntax Analysis, Semantic Analysis, dan pembentukan Three-Address Code (TAC). Dengan implementasi ini, source code do-while yang memiliki percabangan if-else dapat diubah menjadi representasi kode antara yang lebih sederhana sehingga mudah dipahami sebagai bagian dari proses kompilasi.