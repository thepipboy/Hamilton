import LHS
import midHS
import RHS
import sigma
import multiply
import equation
class H(HS, HW):
    def __init__(self):
        self.LHS = LHS()
        self.midHS = midHS()
        self.RHS = RHS()
        self.equation = self.midHS  # Assuming midHS is an instance of a class
        self.sigma = self.LHS        # Assuming LHS is an instance of a class
        self.multiply = self.RHS      # Assuming RHS is an instance of a class

