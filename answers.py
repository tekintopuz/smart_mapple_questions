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


def hasDuplicate(string: str) -> bool:
    length = len(string)
    for i in range(length-1):
        if string[i:i+2] == "11":
            # find starting with double 11, now look at any double 11 after
            if i + 2 == length:
                return True
            else:
                # look up the rest of string but with i+1
                for j in range(i+1, length-1):
                    if string[j:j+2]=="11":
                        return True

    return False