#    AUDYTORIYA
class Audytoriya():
    def __init__(self,nomer,purpose = None,sits = 0):
        self.setNomer(nomer); self.setPurpose(purpose); self.setSits(sits)

    def LessSits(self, deleted_sits):
        self.sits -= deleted_sits
    def MoreSits(self, added_sits):
        self.sits += added_sits

    #    GET
    def getNomer(self)  : return(self.nomer)
    def getPurpose(self): return(self.purpose if self.purpose != None else "не визначене")
    def getSits(self)   : return(self.sits    if self.sits    != 0    else "не визначена")

    #    SET
    def setNomer(self,nomer)    : self.nomer   = nomer
    def setPurpose(self,purpose): self.purpose = purpose
    def setSits(self,sits)      : self.sits    = sits

    #    STR
    def __str__(self):
        return("""
        Аудиторія номер %d
        \tПризначення %s
        \tКількість стільців %s
        """%(self.nomer,self.getPurpose(),self.getSits()))



#    LEKCIYNA
class Lekciyna    (Audytoriya):
    #    __INIT__
    def __init__(self, nomer,sits):
        Audytoriya.__init__(self, nomer, "Лекційна", sits)
    #    ----
    def setSits(self,sits, numer_of_tables = 1): self.sits = sits * numer_of_tables



#    COMPUTERNA
class Computerna (Audytoriya):
    #    __INIT__
    def __init__(self, nomer,sits):
        Audytoriya.__init__(self, nomer, "Комп'ютерна", sits)
    #    ----
    def setSits(self,sits,with_computer = 0):
        super().setSits(sits)
        self.with_computer = with_computer
        if with_computer > sits:
            print("!к-сть місць з комп'ютером > загальної к-сті місць. Вірогідна помилка")
    def getSits(self):
        return ("%s, %s з яких обладнано комп'ютером" % (super().getSits(), self.with_computer))



#    VYKLADATSKA
class Vykladatska(Audytoriya):
    #    __INIT__
    def __init__(self, nomer,sits):
        Audytoriya.__init__(self, nomer, "Викладатська", sits)
        self.setKafedra(None)
    #    ----
    def setKafedra(self,kafedra): self.kafedra = kafedra
    def getKafedra(self): return(self.kafedra    if self.kafedra    != 0    else "не визначена")
    def __str__(self):
        return super().__str__() + "\tКафедра %s" % self.getKafedra()


if __name__ == "__main__":
    print("""\nLEKCIYNA""")
    lekciyna_1 = Lekciyna(1, 10)
    print(lekciyna_1)

    print("""\nCOMPUTERNA""")
    computerna_2 = Computerna(2, 20)
    print(computerna_2)

    print("""\nVYKLADATSKA""")
    vykladatska_3 = Vykladatska(3, 30)
    print(vykladatska_3)
