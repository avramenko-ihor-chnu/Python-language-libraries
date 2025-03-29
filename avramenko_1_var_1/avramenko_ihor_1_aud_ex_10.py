class Complex:
    """ Комплексне число """
    def __init__(self, real=0.0, imaginary=0.0):
        """ Конструктор
        :param real: дійсна частина
        :param imaginary: уявна частина """
        self.real = real; self.imaginary = imaginary
    def __repr__(self):
        """ Метод __repr__ повертає подання об‘єкта у вигляді
        рядка, який має вигляд виразу, що створює аналогічний об‘єкт,
        інакше містить його опис;
        Викликають функцією repr. """
        return 'Complex(%g, %g)' % (self.real, self.imaginary)
    def __str__(self):
        """ Метод __str__ повертає подання об‘єкта у вигляді
        рядка; його викликають функції str, print і format. """
        return '%g %c %gi' % (self.real,
            '+' if self.imaginary >= 0 else '-',
            abs(self.imaginary))
    # Арифметичні операції
    def __add__(self, other):
        """ Метод __add__ визначає операцію додавання. """
        return Complex(self.real + other.real,
            self.imaginary + other.imaginary)
    def __neg__(self):
        """ Операція заперечення """
        return Complex(-self.real, -self.imaginary)
    def __sub__(self, other):
        """ Операція віднімання.
        Додавання і заперечення вже визначені, тому віднімання
        можна визначити через них """
        return self + (-other)
    def __abs__(self):
        """ Модуль числа """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5
    # Операції порівняння
    def __eq__(self, other):
        return self.real==other.real and self.imaginary==other.imaginary
    def __ne__(self, other):
        return not (self == other)

def main():
    x = Complex(2, 3.5)
    print(repr(x)); print('x =', x)
    y = Complex(5, 7)
    print('y =', y); print('x + y =', x + y)
    print('x - y =', x - y); print('|x| =', abs(x))
    print('(x == y) =', x == y)
if __name__ == '__main__': main()
