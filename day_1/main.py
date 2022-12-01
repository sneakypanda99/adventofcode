#############################
# CONSTANTS
#############################
INPUT_FILENAME = "input"


#############################
# FUNCTIONS
#############################

def findMostCals(filename, number_of_elf=1):
    greatest = []
    with open(filename, "r") as f:
        sum_cals = 0
        for i in f:
            if i != "\n":
                sum_cals += int(i.strip("\n"))
            else:
                greatest.append(sum_cals)
                sum_cals = 0
    return sum(sorted(greatest)[-number_of_elf:])


#############################
# ENTRY POINT
#############################
if __name__ == "__main__":
    print("Elf with most cals:", findMostCals(INPUT_FILENAME))
    print("Sum of 3 Elves with most cals:",
          findMostCals(INPUT_FILENAME, number_of_elf=3))
