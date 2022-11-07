GeneCode=["ATCGGGCAT", "ATCGA", "TTTGCGA"]
def CheckDeletion(sequence):
    result=list(filter(lambda a: len(a)%3!=0,sequence))
    return result
print(CheckDeletion(GeneCode))
