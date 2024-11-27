from math import gcd
class Fraction:
    """Class representing a fraction and operations on it

    Author : A. Gavage
    Date : Novembre 2024
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0 by default it's 1
        POST : num and den are initialized
        """
        self.num = num
        self.den = den
        if isinstance(self.num, float) or  isinstance(self.den, float):
            raise ValueError(("numerator and denominator cannot be a float"))
        if self.den == 0:
            raise ValueError("denominator cannot be zero")

    @property
    def numerator(self):
        return self.num
    @property
    def denominator(self):
        return self.den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : Fraction is valide
        POST : string representation : "num" if den == 0 or "num/den" 
        """        
        commun = gcd(self.num, self.den) #calcul du plus grand commun diviseur (PGCD)
        reduced_num = self.num // commun #division entière
        reduced_den = self.den // commun
        if reduced_den < 0: #le dénominateur est gardé positif
            reduced_num = -reduced_num
            reduced_den = -reduced_den
        return str(reduced_num) if reduced_den == 1 else f"{reduced_num}/{reduced_den}"
        

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : Fraction is valid
        POST : string representation : "int + fraction" 
        """
        part_naturel = self.num // self.den
        rest = abs(self.num % self.den)
        if rest == 0:
            return str(part_naturel)
        elif part_naturel == 0:
            return f'{self.num}/{self.den}'
        else:
            return f'{part_naturel} + {rest}/{self.den}'

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is a instance of Fraction
         POST : return the sum in the form of a fraction
         """
        n_num = self.num * other.den + other.num * self.den
        n_den = self.den * other.den
        return Fraction(n_num, n_den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is a instance of Fraction
        POST : return the difference in the form of a fraction
        """
        n_num = self.num * other.den - other.num * self.den
        n_den = self.den * other.den
        return Fraction(n_num, n_den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is a instance of Fraction
        POST : return the product in the form of a fraction
        """
        n_num = self.num * other.num
        n_den = self.den * other.den
        return Fraction(n_num, n_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is a instance of Fraction
        POST : return the division in the form of a fraction
        """
        try:
            if other.num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            n_num = self.num * other.den
            n_den = self.den * other.num
            return Fraction(n_num, n_den)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except AttributeError as e:
            print(f"Error: Invalid operand for division. {e}")


    def __pow__(self, puissance):
        """Overloading of the ** operator for fractions

        PRE : other is an int
        POST : return the fraction raised to the power of other
        """
        try:
            if puissance >= 0:
                return Fraction(self.num ** puissance, self.den ** puissance)
            else:
                n_num = self.den
                n_den = self.num
                puissance = abs(puissance)
                return Fraction(n_num ** puissance, n_den ** puissance)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except AttributeError as e:
            print(f"Error: Invalid operand for division. {e}")

    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : other is a instance of Fraction
        POST : return True when the fractions are equal and False when not 
        """
        return self.num == other.num and self.den == other.den
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : Fraction is valide
        POST : return a float
        """
        return self.num / self.den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : Fraction is valid
        POST : return True if the fraction == 0 and False when not
        """
        return self.num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : Fraction is valid
        POST : return True if the fraction can be simplified to an int and False when not
        """
        return self.num % self.den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : Fraction is valid
        POST : return True when the absolute value of the fraction is < 1, False when not
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : Fraction is valid
        POST : return True when the num is 1, False when not
        """
        return abs(self.num) == 1 and self.den != 0

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other is a instance of Fraction
        POST : return True if the absolute difference a unit fraction, False when not (unit fraction = fraction unitaire ex: 1/6, 1/2)
        """
        diff = self - other
        return abs(diff.num) == 1 and diff.den != 0


def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 10)
    f3 = Fraction(68, 40)

    #opérations
    print("opérations arithmétiques")
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f1} - {f2} = {f1 - f2}")
    print(f"{f1} * {f3} = {f1 * f3}")
    print(f"{f1} / {f3} = {f1 / f3}\n")

    print("as_mixed_number")
    print(f"fraction {f3} en mixte => {f3.as_mixed_number()}\n")

    print("is_adjacent_to")
    f4 = Fraction(1, 3)
    print(f"f1 == Fraction(2, 4) => {f1 == Fraction(2, 4)}")
    print(f"f4 est adjacent à f1 => {f4.is_adjacent_to(f1)}\n")

    print("is_zero, is_integer, is_proper, is_unit")
    f5 = Fraction(3, 1)
    f6 = Fraction(0, 5)
    f7 = Fraction(7, 3)

    print(f"{f6} nul = {f6.is_zero()}")
    print(f"{f5} un entier=? {f5.is_integer()}")
    print(f"{f1} propre = {f1.is_proper()}")
    print(f"{f7} propre = {f7.is_proper()}")
    print(f"{f1} fraction unitaire = {f1.is_unit()}")
    print(f"{f3} fraction unitaire = {f3.is_unit()}\n")

    print("float")
    print(f"décimale de {f1} = {float(f1)}")
    print(f"decimale de {f2} = {float(f2)}\n")

if __name__ == "__main__":
    main()

