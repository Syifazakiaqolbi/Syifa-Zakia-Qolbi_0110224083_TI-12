class Gempa:
    #Konstruktor Inisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):

        #Atribut
        self.lokasi = lokasi
        self.skala = skala

    #method menentukan dampak skala gempa
    def dampak(self):
        
        #statement/logika
        if self.skala < 2:
            print('Dampak Gempa Tidak Berasa')
        elif self.skala >=2 and self.skala <=4:
            print('Dampak Gempa Bangunan Retak-Retak')
        elif self.skala >4 and self.skala <=6:
            print('Dampak Gempa Bangunan Roboh')
        elif self.skala >6 :
            print('Dampak Gempa Tsunami')

        #Menampilkan Lokasi dan Skala
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Lokasi Gempa: {self.skala}')


