import avramenko_3_var_1_step_3 as aud
#    LEKCIYNA
class Lekciyna    (aud.audytoriya):
    def setSits(self,sits, numer_of_tables = 1): self.sits = sits * numer_of_tables
#    COMPUTERNA
class Computerna (aud.audytoriya):
    def setSits(self,sits,with_computer = 0):
        super().setSits(sits)
        self.with_computer = with_computer
        if with_computer > sits:
            print("!к-сть місць з комп'ютером > загальної к-сті місць. Вірогідна помилка")
    def getSits(self):
        return ("%s, %s з яких обладнано комп'ютером" % (super().getSits(), self.with_computer))

#    VYKLADATSKA
class Vykladatska(aud.audytoriya):
    def setKafedra(self,kafedra): self.kafedra = kafedra
    def getKafedra(self): return(self.kafedra    if self.kafedra    != 0    else "не визначена")
    def __str__(self):
        return super().__str__() + "\tКафедра %s" % self.getKafedra()


if __name__ == "__main__":
    print("""\nLEKCIYNA""")
    lekciyna_1 = Lekciyna(1)
    lekciyna_1.setSits(20,10)
    print(lekciyna_1.getSits())

    print("""\nCOMPUTERNA""")
    computerna_2 = Computerna(2)
    computerna_2.setSits(10, 18)
    print(computerna_2.getSits())

    print("""\nVYKLADATSKA""")
    vykladatska_3 = Vykladatska(3)
    vykladatska_3.setKafedra("Математичного Аналізу")
    print(vykladatska_3.getKafedra())
    print(vykladatska_3)
