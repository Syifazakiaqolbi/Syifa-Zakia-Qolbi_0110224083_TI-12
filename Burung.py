from Animal import Animal

class Burung(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    #Method Info
    def info_burung(self):
        super().info_animal
        print("Nama Hewan\t\t: ", self.nama,"\nMakanan\t\t\t: ", self.makanan, "\nHidup\t\t\t: ", self.hidup, "\nBerkembang Biak\t\t: ", self.berkembang_biak, "\nWarna\t\t\t: ", self.warna, "\nJenis Paruh\t\t: ", self.paruh)
# #Objek
# print()
# Burung = Burung("Elang", "Daging", "Ditebing", "Menghasilkan Telur", "Coklat", "Bengkok dan Lancip" )
# print()
# Burung.info_burung()



