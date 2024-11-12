### Given org1 = ["ACGTTTCA", "AGGCCTTA", "AAAACCTG"], org2 = ["AGCTTTGA", "GCCGGAAT", "GCTACTGA"].
### Find all similar pairs of genome sequences (one sequence from org1, one from org2) using list comprehension.
### “Similar” means: similarity(seq1, seq2) > threshold

def similar(org1, org2, threshold):
    similar_pairs=[(seq1, seq2)for seq1 in org1 for seq2 in org2 if (sum(1 for i, j in zip(seq1, seq2) if i==j)*100)/len(seq1) > threshold]
    return similar_pairs
def main():
    org1=["ACGTTTCA", "AGGCCTTA", "AAAACCTG"]
    org2=["AGCTTTGA", "GCCGGAAT", "GCTACTGA"]
    threshold=float(input("Enter the similarity threshold (without percentage sign): "))
    print(f"Similar pairs: {similar(org1, org2, threshold)}")
if __name__ == "__main__":
    main()
