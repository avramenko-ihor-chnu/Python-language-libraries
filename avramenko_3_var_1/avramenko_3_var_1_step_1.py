class audytoriya():
    def __init__(self, nomer, purpose = None, sits = 0):
        self.nomer   = nomer
        self.purpose = purpose
        self.sits    = sits

if __name__ == "__main__":
    audytoriya_0  = audytoriya(0)
    audytoriya_39 = audytoriya(39, "Лекційна",100)
    print(audytoriya_0.nomer, audytoriya_0.purpose, audytoriya_0.sits)
    print(audytoriya_39.nomer, audytoriya_39.purpose, audytoriya_39.sits)
