
# declare variables
# 1rmx is tested or theoretical
# tmax is traning max that is used in calculations

squat_1rmx = squat_tmax = bench_1rmx = bench_tmax = deadlift_1rmx = deadlift_tmax = ohp_1rm = ohp_tmax = 0
wordlist = {'Squat': squat_1rmx, 'Bench': squat_1rmx, 'Deadlift': deadlift_1rmx, 'OHP': ohp_1rm}

# calculate theoretical 1 rep max with given weight and reps
# using Epley formula
# TO DO - add the McGlothin, Lombardi, Mayhew et al., O'Conner, Wathan and Wendler formulas and average them for a "maybe" more accurate 1rmx
# https://en.wikipedia.org/wiki/One-repetition_maximum
def calc1Rep(weight, reps):
    epley = int(weight) * ( 1 + ( int(reps) / 30) )
    brzycki = int(weight) * ( 36 / ( 37 - int(reps) ) )
    return int((epley + brzycki) / 2)

def calctmax(weight):
    return int(float(weight) * .9)
# get one rep max or actual max
def getMax():
    choice = input( "Using [A]CTUAL MAX or [T]HEORETICAL MAX: " )
    if choice.lower() == 'a':
        for key in wordlist.keys():
            weight = input("Enter weight for " + key + ": " )
            wordlist[key] = weight
        print(wordlist)
    elif choice.lower() == 't':
        for key in wordlist.keys():
            tempWeight, tempReps = input("Enter weight followed by reps for " + key + ': ').split()
            wordlist[key] = calc1Rep(tempWeight, tempReps)
            print(wordlist)
    else:
        getMax()
getMax()
print (calctmax(wordlist['Squat']))
