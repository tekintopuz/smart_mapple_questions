"""
Given a dictionary of ['element','mass'] containing elements of the periodic table and their atomic masses.

AtomicMassesOfElements = {
    "Boron": 5, "Carbon": 6, "Nitrogen": 7, "Oxygen": 8, "Fluorine": 9,
    "Aluminum": 13, "Silicon": 14, "Phosphorus": 15, "Sulfur": 16, "Chlorine": 17,
    "Gallium": 31, "Germanium": 32, "Arsenic": 33, "Selenium": 34, "Bromine": 35,
    "Indium": 49, "Tin": 50, "Antimony": 51, "Tellurium": 52, "Iodine": 53,
    "Thallium": 81, "Lead": 82, "Bismuth": 83, "Polonium": 84, "Astatine": 85,
    "Nihonium": 113, "Flerovium": 114, "Moscovium": 115, "Livermorium": 116, "Tennessine": 117
}

Also, a randomized matrix of their atomic masses.

groupOfAtomicMasses = [[8, 17, 115, 51, 13],
                       [50, 53, 16, 7, 82],
                       [49, 14, 114, 31, 5],
                       [113, 32, 6, 84, 117],
                       [81, 116, 15, 9, 83],
                       [35, 34, 52, 33, 85]]


Find each element that has the greatest mass in relation to its neighbors and return a list of the elements' names.

Input:
[[35, 17, 15, 114, 84],
 [13, 14, 113, 32, 33],
 [34, 9, 49, 52, 117],
 [53, 83, 7, 5, 85],
 [116, 31, 82, 51, 81],
 [6, 50, 115, 8, 16]]

 Output:
["Bromine","Flerovium","Nihonium","Tennessine","Bismuth","Livermorium","Moscovium"]

Input:
[[53, 52, 115, 31, 83],
 [8, 51, 34, 113, 14],
 [84, 114, 117, 85, 9],
 [5, 116, 82, 7, 13],
 [16, 81, 32, 6, 35],
 [17, 49, 50, 33, 15]]

 Output:
["Iodine","Moscovium","Bismuth","Nihonium","Tennessine","Livermorium","Bromine","Tin"]

"""


def findPowerfullElements(AtomicMassesOfElements: dict, groupOfAtomicMasses: list) -> list:
    newAtomicMassesOfElements = {}
    # atomic numbers are unique, so they can be accessible as hashable key for a dictionary
    for k, v in AtomicMassesOfElements.items():
        newAtomicMassesOfElements[v] = k

    row = len(groupOfAtomicMasses)
    col = len(groupOfAtomicMasses[0])
    greatestMass = []

    for i in range(row):
        for j in range(col):
            # look up neighbours
            #                             North Neighbour(i-1, j)
            # West Neighbour(row, col-1) <- X -> East Neighbour (row, col+1)
            #                             South Neighbour(i+1, j)
            if i - 1 >= 0 and groupOfAtomicMasses[i][j] < groupOfAtomicMasses[i - 1][j]:
                # North Neighbour(i-1, j) is greater
                continue
            if j + 1 < col and groupOfAtomicMasses[i][j] < groupOfAtomicMasses[i][j+1]:
                # East Neighbour (row, col+1) is greater
                continue
            if j - 1 >= 0 and groupOfAtomicMasses[i][j] < groupOfAtomicMasses[i][j - 1]:
                # West Neighbour (row, col+1) is greater
                continue
            if i + 1 < row and groupOfAtomicMasses[i][j] < groupOfAtomicMasses[i+1][j]:
                # West Neighbour (row, col+1) is greater
                continue

            greatestMass.append(newAtomicMassesOfElements[groupOfAtomicMasses[i][j]])
    return greatestMass

