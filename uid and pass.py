def strong():
    global pas
    al , dig , sp = [] ,[] ,[]
    pas = input("enter password: ")
    if len(pas)<8:
        print("password must be of 8 characters")
        return strong()
    else:
        for i in pas:
            if i.isalpha():
                al.append(i)
            elif i.isdigit():
                dig.append(i)
            else:
                sp.append(i)
        if len(al)!=0 and len(dig)!=0 and len(sp)!=0:
            print("Password is strong!" )
        else:
            print("Password is weak. Try making a combo of alphabets, digits and special characters")
            return strong()

def uid(): 
    f = open("sec.txt","r")
    a = f.readlines()
    f.close()
    userid = input("enter user id: ")
    b = open("sec.txt" , "a")
    for data in a:
        eid = data.split()[0]
        if eid == userid:
            print("userid taken, try another")
            return uid()
    strong()
    store = userid + " " + pas + "\n"
    b.write(store)
    print("ID and Password sucessfully stored")
    b.close()
uid()
     
