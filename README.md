# Question-1
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


# Ouestion 2
Given a string comprised of 0s and 1s, check if it contains any substring that starts and ends with "11".

input: “0101101"
output: false


input: “10011001101”
output: true

