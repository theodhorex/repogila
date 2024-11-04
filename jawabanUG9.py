class Resto:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def add(self, item, priority):
        self.data.append((priority, item))
        self.data.sort()

    def change_priority(self, item, new_priority):
        index = list(map(lambda x : x[1], self.data)).index(item)
        del self.data[index]
        self.add(item, new_priority)
        

    def remove_highest_priority(self):
        try:
            max = 0
            for i in range(len(self.data)):
                if self.data[i] > self.data[max]:
                    max = i
            item = self.data[max]
            del self.data[max]
            return item
        except IndexError:
            print()
            exit()

    def remove_with_priority(self, priority):
        index = list(map(lambda x : x[0], self.data)).index(priority)
        del self.data[index]

    def display(self):
        for priority, item in self.data:
            print(f"Priority: {priority}, Item: {item}")

antrian = Resto()
antrian.add("Pesan Pizza", 2)
antrian.add("Pesan Ayam Goreng", 1)
antrian.add("Pesan Burger", 3)
print("Isi awal Pesanan:")
antrian.display()

print("\nPesanan Ayam Goreng diminta cepat!!!")
antrian.change_priority("Pesan Ayam Goreng", 4)
antrian.display()

print("\n##### PESANAN PERTAMA SELESAI #####\n")
antrian.remove_highest_priority()

print("Sisa pesanan: ")
antrian.display()

print("\nPesanan dengan prioritas ini telah selesai")
antrian.remove_with_priority(2)
antrian.display()
