#pak alle characters in de string behalve de laatste en sla deze op in ss
str = "Hallo ik ben een string en ik wordt opgegeten"


def destroyString(tekst):

    newStr = tekst[0:len(tekst)-1]
    print(tekst)

    if tekst != "":
        destroyString(newStr)

destroyString(str)
