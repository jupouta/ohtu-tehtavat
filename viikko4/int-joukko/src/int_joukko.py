OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=OLETUSKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.tarkista_kapasiteetti_ja_kasvatuskoko(kapasiteetti, kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def tarkista_kapasiteetti_ja_kasvatuskoko(self, kapasiteetti, kasvatuskoko):
        if not (isinstance(kapasiteetti, int) and isinstance(kasvatuskoko, int)) or (kapasiteetti < 0 and kasvatuskoko < 0):
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

    def kuuluu_joukkoon(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                return True
        return False

    def lisaa_luku(self, n):
        if not self.kuuluu_joukkoon(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, n):
        kohta = -1

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            apu = self.lukujono[kohta+1:]
            self.lukujono[kohta:] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1


    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def listaa_luvut(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu


    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.listaa_luvut()
        b_taulu = b.listaa_luvut()

        for i in range(0, len(a_taulu)):
            x.lisaa_luku(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa_luku(b_taulu[i])

        return x

    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.listaa_luvut()
        b_taulu = b.listaa_luvut()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa_luku(b_taulu[j])

        return y

    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.listaa_luvut()
        b_taulu = b.listaa_luvut()

        for i in range(0, len(a_taulu)):
            z.lisaa_luku(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
