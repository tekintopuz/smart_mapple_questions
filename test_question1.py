from question1 import findPowerfullElements


class TestApp:
    def test_findPowerfullElements(self):
        atomicMassesOfElements = {
            "Boron": 5, "Carbon": 6, "Nitrogen": 7, "Oxygen": 8, "Fluorine": 9,
            "Aluminum": 13, "Silicon": 14, "Phosphorus": 15, "Sulfur": 16, "Chlorine": 17,
            "Gallium": 31, "Germanium": 32, "Arsenic": 33, "Selenium": 34, "Bromine": 35,
            "Indium": 49, "Tin": 50, "Antimony": 51, "Tellurium": 52, "Iodine": 53,
            "Thallium": 81, "Lead": 82, "Bismuth": 83, "Polonium": 84, "Astatine": 85,
            "Nihonium": 113, "Flerovium": 114, "Moscovium": 115, "Livermorium": 116, "Tennessine": 117
        }

        groupOfAtomicMasses1 = [[35, 17, 15, 114, 84],
         [13, 14, 113, 32, 33],
         [34, 9, 49, 52, 117],
         [53, 83, 7, 5, 85],
         [116, 31, 82, 51, 81],
         [6, 50, 115, 8, 16]]
        output1 = ["Bromine", "Flerovium", "Nihonium", "Tennessine", "Bismuth", "Livermorium", "Moscovium"]

        assert output1 == findPowerfullElements(atomicMassesOfElements, groupOfAtomicMasses1)

        groupOfAtomicMasses2 = [[53, 52, 115, 31, 83],
                               [8, 51, 34, 113, 14],
                               [84, 114, 117, 85, 9],
                               [5, 116, 82, 7, 13],
                               [16, 81, 32, 6, 35],
                               [17, 49, 50, 33, 15]]

        output2 = ["Iodine", "Moscovium", "Bismuth", "Nihonium", "Tennessine", "Livermorium", "Bromine", "Tin"]

        assert output2 == findPowerfullElements(atomicMassesOfElements, groupOfAtomicMasses2)

