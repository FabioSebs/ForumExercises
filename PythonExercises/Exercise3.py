#Exercise 3
import scipy.constants 

def num_atoms(grams , atomicweight = 196.97):
    total = grams/atomicweight
    atoms = total*scipy.constants.Avogadro
    print(atoms)

num_atoms(10)
num_atoms(10,12.001)
num_atoms(10, 1.008)

    
