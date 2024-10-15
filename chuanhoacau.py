try:
    s=""
    while True:
        s=s+input()+"\n"
except EOFError:
    s=s+" "
    l=[]
    idx=0
    id=0
    for i in s:
        if i in ['\n','?','!','.']:
            l.append(s[idx:id+1])
            idx=id+1
        id=id+1
    for st in l:
        if "\n" not in st :
            vd=" ".join(st.split()).capitalize()
            print(vd[:-1].strip()+vd[-1])
        else:
            if st!="\n":
                vd=" ".join(st.split()).capitalize()
                print(vd+".")