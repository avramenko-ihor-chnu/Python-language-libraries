class audytoriya():
    def __init__(self,nomer,purpose = None,sits = 0):
        self.setNomer(nomer), self.setPurpose(purpose), self.setSits(sits)

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

if __name__ == "__main__":
    audytoriya_0  = audytoriya(0)
    audytoriya_39 = audytoriya(39, "Лекційна",100)
    print(audytoriya_0.getNomer(),  audytoriya_0.getPurpose(),  audytoriya_0.getSits())
    print(audytoriya_39.getNomer(), audytoriya_39.getPurpose(), audytoriya_39.getSits())
