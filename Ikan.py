from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.bernapas = bernapas
        self.habitat = habitat

    def info_ikan(self):
        super().info_animal()
        print("Nama Hewan\t\t: ", self.nama,"\nMakanan\t\t\t: ", self.makanan, "\nHidup\t\t\t: ", self.hidup, "\nBerkembang Biak\t\t: ", self.berkembang_biak, "\nBernapas Menggunakan\t: ", self.bernapas , "\nHabitat di \t\t: ", self.habitat)

#Objek
print()
ikan = Ikan("Hiu", "Daging", "Di Laut", "Melahirkan", "Insang", "Air Asin" )
print()
ikan.info_ikan()
