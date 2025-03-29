class Table:
    def __init__(self,l,w,h):
        self.lenght = l #*len

        self.width  = w
        self.height = h

    def outing(self):
        print (self.lenght,self.width,self.height)

class Kitchen(Table):
    def howplaces(self,n):
        if n < 2:
            print ("It is not kitchen table")
            self.places = n # <-- Додав. Без цього рядка видає помилку при n<2
        else: self.places = n

    def outplases(self):
        print (self.places)

t_room1 = Kitchen(2,1,0.5)
t_room1.outing(); t_room1.howplaces(1)
t_room1.outplases()
t_2 = Table(1,3,0.7); t_2.outing()
#t_2.howplaces(5)
