import LHS
import midHS
import RHS
import sigma
import multiply
import equation
import n
class H(HS, HW):
    def __init__(self):
        self.LHS = LHS(n)
        self.midHS = midHS(n)
        self.RHS = RHS(n)
        self.equation = self.midHS  # Assuming midHS is an instance of a class
        self.sigma = self.LHS        # Assuming LHS is an instance of a class
        self.multiply = self.RHS      # Assuming RHS is an instance of a class

