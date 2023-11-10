import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('-ele-phant', 'relev--ant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))



def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    if (S, T) in MED: #if the difference between these two strings has already been calculated (added to dictionary)
        return MED[(S,T)] #return value of the (S, T) key in MED. Which is equal to the edit distance of these two strings
    if (S == ""): #if S is an empty string the edit distance is equal to the length of T
        MED[(S,T)] = len(T) #add key-value pair to the dictionary
    elif (T == ""): #if T is an empty string the edit distance is equal to the length of S
        MED[(S,T)] = len(S) #add key-value pair to the dictionary    
    else:
        if (S[0] == T[0]): #if characters are equal, the edit distance of S and T is equal to the edit distance of the remaining characters
            MED[(S,T)] = fast_MED(S[1:], T[1:], MED)
        else: #The edit distance is equal to 1 + the minimum of either an insertion or deletion
            MED[S, T] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
    return MED[(S,T)] #return the edit distance for S and T




def fast_align_MED(S, T, MED={}, alignments={}):
    # TODO -  keep track of alignments
    if (S,T) in alignments:
       return alignments[(S,T)] #if alignment has already been found, return it
    if (S == ""):
        MED[(S,T)] = len(T)
        alignments[S,T] = ("-" * len(T), T) #if S is an empty string, T will remain unchanged and S will have len(T) insertions, represented by "-"
    elif (T == ""):
        MED[(S,T)] = len(S)
        alignments[S,T] = (S, "-" * len(S)) #if T is an empty string, S will remain unchanged and T will have len(S) insertions, represented by "-"
    else:
        if (S[0] == T[0]):
            MED[S, T] = fast_MED(S[1:], T[1:], MED) #same as fast_MED
            alignments[S,T] = (S[0] + fast_align_MED(S[1:], T[1:], MED, alignments)[0], T[0] + fast_align_MED(S[1:], T[1:], MED, alignments)[1]) #if first characters are the same, leave the first character unchanged and find the alignment for the remaining characters
        else:
            #need to determine if it is more efficient to perform an insertion or deletion
            if fast_MED(S[1:], T, MED) < fast_MED(S, T[1:], MED): #if deletion is more efficient than insertion
                MED[S, T] = 1 + fast_MED(S[1:], T, MED) #cost calculation
                #alignment: delete from S and insert to T, for insertions add "-", no edits for deletions
                alignments[S,T] = (S[0] + fast_align_MED(S[1:], T, MED, alignments)[0], "-" + fast_align_MED(S[1:], T, MED, alignments)[1])
            else: #if insertion is more efficient than deletion
                MED[S,T] = 1 + fast_MED(S, T[1:], MED) #cost calculation
                #alignment: delete from T and insert to S, for insertions add "-", no edits for deletion
                alignments[S,T] = ("-" + fast_align_MED(S, T[1:], MED, alignments)[0], T[0] + fast_align_MED(S, T[1:], MED, alignments)[1])
    return alignments[S,T]



for S, T in test_cases:
        print(fast_align_MED(S, T))

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
