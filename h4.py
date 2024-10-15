with open('A.txt') as filelol:
    ds=filelol.readlines()
with open('B.txt') as filecac:
    k=filecac.readlines()
for i,j in zip(ds,k):
    #for j in k:
        try:
            m=int(i)
            n=int(j)
            print(m**n)
        except:
            print("Khong the thuc hien")
     