s="UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"
sequence=list(s.split(", "))
def HighUracil(seq):
    result=sorted(seq,reverse=True,key=lambda x: sum(let=='U'for let in x))
    return(result)
print(HighUracil(sequence))