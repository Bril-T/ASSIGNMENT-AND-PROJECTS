#FORMULAS
import math

# Base class
class PetroleumFormula:
    def calculate(self):
        raise NotImplementedError("Subclasses must implement this method")

# Darcy's Law
class DarcysLaw(PetroleumFormula):
    def __init__(self, k, A, delta_P, mu, L):
        self.k = k
        self.A = A
        self.delta_P = delta_P
        self.mu = mu
        self.L = L

    def calculate(self):
        try:
            return (self.k * self.A * self.delta_P) / (self.mu * self.L)
        except Exception as e:
            print("Error in Darcy's Law:", e)

# Hydrostatic Pressure
class HydrostaticPressure(PetroleumFormula):
    def __init__(self, density, gravity, height):
        self.rho = density
        self.g = gravity
        self.h = height

    def calculate(self):
        try:
            return self.rho * self.g * self.h
        except Exception as e:
            print("Error in Hydrostatic Pressure:", e)

# Gas Compressibility
class GasCompressibility(PetroleumFormula):
    def __init__(self, P, V, n, R, T):
        self.P = P
        self.V = V
        self.n = n
        self.R = R
        self.T = T

    def calculate(self):
        try:
            return (self.P * self.V) / (self.n * self.R * self.T)
        except Exception as e:
            print("Error in Gas Compressibility:", e)

# Volumetric Gas Reservoir
class VolumetricGasReservoir(PetroleumFormula):
    def __init__(self, A, h, phi, S_w, B_g):
        self.A = A
        self.h = h
        self.phi = phi
        self.S_w = S_w
        self.B_g = B_g

    def calculate(self):
        try:
            return (43560 * self.A * self.h * self.phi * (1 - self.S_w)) / self.B_g
        except Exception as e:
            print("Error in Volumetric Gas Reservoir:", e)

# Material Balance Equation
class MaterialBalance(PetroleumFormula):
    def __init__(self, P_i, P, E_t):
        self.P_i = P_i
        self.P = P
        self.E_t = E_t

    def calculate(self):
        try:
            return (self.P_i - self.P) / self.E_t
        except Exception as e:
            print("Error in Material Balance:", e)

# API Gravity
class APIGravity(PetroleumFormula):
    def __init__(self, SG):
        self.SG = SG

    def calculate(self):
        try:
            return (141.5 / self.SG) - 131.5
        except Exception as e:
            print("Error in API Gravity:", e)

# Polymorphic function
def display_result(formula_obj):
    result = formula_obj.calculate()
    print(f"{formula_obj.__class__.__name__} result: {result}")

# Testing all formulas
formulas = [
    DarcysLaw(k=100, A=50, delta_P=200, mu=1.2, L=30),
    HydrostaticPressure(density=1000, gravity=9.81, height=3000),
    GasCompressibility(P=500, V=0.1, n=1, R=10.73, T=300),
    VolumetricGasReservoir(A=640, h=50, phi=0.2, S_w=0.3, B_g=0.005),
    MaterialBalance(P_i=3000, P=2500, E_t=0.0005),
    APIGravity(SG=0.85)
]

for f in formulas:
    display_result(f)
