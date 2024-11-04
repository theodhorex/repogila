[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/OG5cg6PZ)
# UG09_PriorityQueue

### Kerjakan pada file main.py!!!

Buatlah sebuah program Sorted Priority Queue menggunakan list. Fungsi yang harus ditambahkan adalah : 
  
  - Mengubah prioritas data

  - Menghapus data dengan prioritas tertinggi

  - Menghapus data dengan priotitas sesuai parameter


 TEST CASE:

antrian = Resto()

antrian.add("Pesan Pizza", 2)

antrian.add("Pesan Ayam Goreng", 1)

antrian.add("Pesan Burger", 3)

print("Isi awal Pesanan:")

antrian.display()

print("\nPesanan Ayam Goreng diminta cepat!!!")

antrian.change_priority("Pesan Ayam Goreng", 4)

antrian.display()

print("\n##### PESANAN PERTAMA SUDAH SELESAI #####\n")

antrian.remove_highest_priority()

print("Sisa pesanan: ")

antrian.display()

print("\nPesanan dengan prioritas ini telah selesai")

antrian.remove_with_priority(2)
antrian.display()
