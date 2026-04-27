# # 21
class Yozuvchi:
    def __init__(self, ism):
        self.ism = ism

    def yozish(self):
        print("Yozmoqda")

class Shoir(Yozuvchi):
    def yozish(self):
        print("She’r yozmoqda")

a = Shoir("Alisher")
a.yozish()


# # 22
class Internet:
    def __init__(self, tezlik):
        self.tezlik = tezlik

    def ulanish(self):
        print("Ulandi")

class WiFi(Internet):
    def ulanish(self):
        print("WiFi ulandi")

a1 = Internet(100)
a2 = WiFi(50)

a1.ulanish()
a2.ulanish()


# # 23
class Kiyim:
    def __init__(self, nomi):
        self.nomi = nomi

    def kiyish(self):
        print("Kiyildi")

class Kurtka(Kiyim):
    def kiyish(self):
        print("Kurtka kiyildi")

a = Kurtka("Qishki kurtka")
a.kiyish()


# # 24
class Talaba:
    def __init__(self, ism):
        self.ism = ism

    def oqish(self):
        print("O‘qimoqda")

class ITtalaba(Talaba):
    def oqish(self):
        print("Dasturlash o‘qimoqda")

a1 = Talaba("Ali")
a2 = ITtalaba("Vali")

a1.oqish()
a2.oqish()


# # 25
class Shahar:
    def __init__(self, nomi):
        self.nomi = nomi

    def info(self):
        print("Shahar mavjud")

class Poytaxt(Shahar):
    def info(self):
        print("Bu poytaxt")

a = Poytaxt("Toshkent")
a.info()
