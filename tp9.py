import unittest
from math import gcd

class TestFraction(unittest.TestCase):

    #test de l'init
    def test_init(self):
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 4)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

        with self.assertRaises(ValueError):
            Fraction(1.5, 2)

    #test de la méthode __str__
    def test_str(self):
        self.assertEqual(str(Fraction(6, 4)), "3/2")
        self.assertEqual(str(Fraction(4, -8)), "-1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")

    #test de la méthode as_mixed_number
    def test_as_mixed_number(self):
        self.assertEqual(Fraction(7, 2).as_mixed_number(), "3 + 1/2")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(-7, 2).as_mixed_number(), "-3 + 1/2")
        self.assertEqual(Fraction(1, 3).as_mixed_number(), "1/3")

    #test de l'addition
    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6))
        self.assertEqual(Fraction(1, 4) + Fraction(-1, 4), Fraction(0, 1))

    #test de la division
    def test_div(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 / f2, Fraction(2, 1))
        self.assertEqual(f2 / f1, Fraction(2, 4))
        
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    #test de l'égalité (__eq__)
    def test_eq(self):
        self.assertTrue(Fraction(3, 4) == Fraction(6, 8))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))
        with self.assertRaises(TypeError):
            Fraction(2, 5) == "bonjour"

    #test de is_integer
    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())

    #test de is_proper
    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    #test de is_adjacent_to
    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(Fraction(2, 10)))

    #test supplémentaire flèmme d'écrire
    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_unit(self):
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_sub(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(1, 2))
        self.assertEqual(f1 - Fraction(2, 4), Fraction(1, 4))

    def test_mul(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)
        self.assertEqual(f1 * f2, Fraction(1, 2))
        self.assertEqual(f2 * f2, Fraction(4, 9))

    def test_float(self):
        self.assertAlmostEqual(float(Fraction(1, 2)), 0.5)
        self.assertAlmostEqual(float(Fraction(3, 4)), 0.75)

    def test_pow(self):
        self.assertEqual(Fraction(2, 3) ** 2, Fraction(4, 9))
        self.assertEqual(Fraction(2, 3) ** -1, Fraction(3, 2))
        with self.assertRaises(ZeroDivisionError):
            Fraction(0, 5) ** -2


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
            raise ValueError("numerator and denominator cannot be a float")
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

        PRE :
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

        PRE :
        POST : string representation : "int + fraction" 
        """
        part_naturel = self.num // self.den
        if self.num < 0 and self.num % self.den != 0:
            part_naturel += 1
        reste = abs(self.num % self.den)
        if reste == 0:
            return str(part_naturel)
        if part_naturel == 0:
            return f"{reste}/{abs(self.den)}"
        return f"{part_naturel} + {reste}/{abs(self.den)}"

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is a instance of Fraction
         POST : return the sum in the form of a new fraction
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

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        n_num = self.num * other.den
        n_den = self.den * other.num
        return Fraction(n_num, n_den)


    def __pow__(self, puissance):
        """Overloading of the ** operator for fractions

        PRE : other is an int
        POST : return the fraction raised to the power of other
        """

        if puissance >= 0:
            return Fraction(self.num ** puissance, self.den ** puissance)
        else:
            if self.num == 0:
                raise ZeroDivisionError
            n_num = self.den
            n_den = self.num
            puissance = abs(puissance)
            return Fraction(n_num ** puissance, n_den ** puissance)

    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : other is a instance of Fraction
        POST :  - return True when the fractions are equal and False when not
                - reduce the fractions before testing if they are equals
        """
        if not isinstance(other, Fraction):
            raise TypeError("Error: type not corresponding to the class fraction")
        gcd_self = gcd(self.num, self.den)
        gcd_other = gcd(other.num, other.den)
        return (self.num // gcd_self == other.num // gcd_other) and \
            (self.den // gcd_self == other.den // gcd_other)
        
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

        Two fractions are adjacents if the absolute value of the difference between them is a unit fraction

        PRE : other is a instance of Fraction
        POST : return True if the absolute difference a unit fraction, False when not (unit fraction = fraction unitaire ex: 1/6, 1/2)
        """
        diff = self - other
        return abs(diff.num) == 1 and abs(diff.den) > 0  # Consider absolute value for denominator


if __name__ == "__main__":
    unittest.main()