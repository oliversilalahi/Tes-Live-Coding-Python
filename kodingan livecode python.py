import csv

# Membaca file CSV yang telah diunggah
file_path = "C:\\Users\\USER\\Downloads\\data animal.csv"

# Menyimpan data dari file CSV ke dalam list
animal_list = []
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Melewati header jika ada
    for row in reader:
        if len(row) > 0:  # Memeriksa apakah baris tidak kosong
            animal_list.append(row[0])  # Mengambil nama hewan dari kolom pertama

# Fungsi untuk memeriksa apakah huruf pertama dari kata kedua adalah vokal
def hurufpertama_katakedua_vokal(word):
    vowels = "aeiouAEIOU"
    return word[0] in vowels

# Memproses dan mencetak nama hewan yang memiliki lebih dari 2 kata dan kata kedua dimulai dengan huruf vokal
for animal in animal_list:
    words = animal.split()
    if len(words) > 1 and hurufpertama_katakedua_vokal(words[1]):  # Memeriksa jika lebih dari 2 kata dan kata kedua dimulai dengan vokal
        print(animal)
