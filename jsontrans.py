f = open('./files/beta.json','r')
ar = f.read()
ar.replace(" ","")
an = list(ar)
i = 0;
n = []
m = ""
q = {}
while i < len(an)-1:  #对列表进行遍历
    if an[i] == "[":       #判断json语句的开头
        i += 1
        while an[i] != "]":  #json语句内遍历
            if an[i] == "{":
                i += 1
                while an[i] != "}":
                    if an[i] != " ":
                        n.append(str(an[i]))
                        i += 1
                    elif an[i] == " ":
                        i += 1
                for mem in n:
                    z = str(mem)
                    m = m + z
                q = {m}
                m = ""
                print(q)
                print("\n")
            else:
                i += 1
    else:
        i += 1