class QuadraticEquationSolver:
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def solve(self):
        if self.get_discriminant() > 0:
            root1 = ((-1 * self.__b) + self.get_discriminant()) / (2 * self.__a)
            root2 = ((-1 * self.__b) - self.get_discriminant()) / (2 * self.__a)
            return root1, root2
        elif self.get_discriminant() == 0:
            root1 = ((-1 * self.__b) + self.get_discriminant()) / (2 * self.__a)
            return root1
        return "NO REAL SOLUTIONS"

    def get_discriminant(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)

    def get_solution_type(self):
        if self.get_discriminant() > 0:
            return f"In the Equation {self.__a}x² + ({self.__b})x + {self.__c} = 0, there are Two Real Roots."
        elif self.get_discriminant() == 0:
            return f"In the Equation {self.__a}x² + ({self.__b})x + {self.__c} = 0, there is One Real Root (Repeated Roots)."
        return f"In the Equation {self.__a}x² + ({self.__b})x + {self.__c} = 0, the Roots are Complex."