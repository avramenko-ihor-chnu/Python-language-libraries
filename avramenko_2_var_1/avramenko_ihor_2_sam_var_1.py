class Error:
    @staticmethod
    def __str__():
        return("Error")
class Success:
    @staticmethod
    def __str__():
        return("Success")

class NI(Error): pass#...Error
class NG(Error): pass#...Error
class NN(Error): pass#...Error

class L(Success): pass#..Success
class N(Success): pass#..Success

class I(L, N, NN): pass#.Success
class G(I, NI): pass#....Success

class E(NG, G): pass#....Success
class NE(Error): pass#...Error
class B(E, NE): pass#....Success

class H(I): pass#........Success
class R(I): pass#........Success
class W(H, R): pass#.....Success

class Begin(W, B): pass#.Success
#-----


print(B())#..............Success
print(Begin())#..........Success

print()

print("B --------> " ,B.mro())
print("Beging ---> " ,Begin.mro())
