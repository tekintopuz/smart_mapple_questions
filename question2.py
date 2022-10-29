'''

Given a string comprised of 0s and 1s, check if it contains any substring that starts and ends with "11".

input: “0101101"
output: false


input: “10011001101”
output: true


'''

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

print(hasDuplicate("11"))
# print(hasDuplicate("0101101"))
# print(hasDuplicate("10011001101"))