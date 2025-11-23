


def split_before_uppercases(formula):
    formula = "H2OCO2NH3Fe"
    result = split_before_each_uppercases(formula)
    assert result == ['H2', 'O', 'C', 'O2', 'N', 'H3','Fe'], f"Test 1 Failed: {result}"

    # Test 2: Single part formula with no uppercase letters
    formula = "water"
    result = split_before_each_uppercases(formula)
    assert result == ['water'], f"Test 2 Failed: {result}"

    # Test 3: Formula starting with an uppercase letter
    formula = "NaCl"
    result = split_before_each_uppercases(formula)
    assert result == ['Na', 'Cl'], f"Test 3 Failed: {result}"

    # Test 4: Formula with multiple uppercase letters together
    formula = "C6H12O6B"
    result = split_before_each_uppercases(formula)
    assert result == ['C6', 'H12', 'O6', 'B'], f"Test 4 Failed: {result}"

    # Test 5: Empty string
    formula = ""
    result = split_before_each_uppercases(formula)
    assert result == [], f"Test 5 Failed: {result}"

    print("All tests passed!")
  # replace the pass with your code

def split_at_digit(formula):
    assert split_at_first_digit("H2") == ("H", 2)
    assert split_at_first_digit("He23") == ("He", 23)
    assert split_at_first_digit("Fe") == ("Fe", 1)
    assert split_at_first_digit("Fe1") == ("Fe", 1)
    assert split_at_first_digit("F") == ("F", 1)
    assert split_at_first_digit("He10000") == ("He", 10000)
    print("All tests passed!")  # replace the pass with your code

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
