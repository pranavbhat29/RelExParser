fileindex=0
print "\t======> Relation Algebra Evaluator <======\n"
def document():
    print "This is the documentation of the R.A Evaluator\n"
    doc = open("Help.txt","r")
    print doc.read()
    doc.close()
    return
def assume():
    print "This is the list of assumptions"
    doc = open("Assumptions.txt","r")
    print doc.read()
    doc.close()
    return
def displayfile(filename):
    multitoset(filename)
    print "\n\n\t  Relation name : "+filename+"   \n"
    print "=============================================================\n\n"
    target = open(filename,"r")
    k = target.readlines()
    target.close()
    j=0
    for nr in range(len(k)) :
        if nr==0 or nr in range(3,len(k)) :
            if nr!=0 :
                j+=1
                print str(j)+"  |  "+k[nr].replace("|","  |  ").replace("\n","")
                if nr==1:
                    print "\n"
            else :
                print "Record.No."+"  |  "+k[nr].replace("|","  |  ")
        if nr==2:
            print "\n____________________________________________________________________________________________________________________________\n\n"
    return
def multitoset(filename) :
    target = open(filename,"r")
    k = target.readlines()
    target.close()
    nvec = [k[0],k[1],k[2]]
    for nr in range(3,len(k)) :
        repeats=0
        for nl in range(3,nr) :
            if k[nl].replace("\n","").replace(" ","")==k[nr].replace("\n","").replace(" ","") :
                repeats=1
                break
        if repeats == 0 :
            nvec.append(k[nr])
    target = open(filename,"w")
    target.writelines(nvec)
    target.close()
    return
def sumup(attribute,filename):
    multitoset(filename)
    target = open(filename,"r")
    k = target.readlines()
    target.close()
    nvec = [k[0].replace("\n","")+"|Sum\n",k[1].replace("\n","")+"|(int)\n",k[2]]
    attr = k[0].replace("\n","").replace(" ","").split("|")
    domic = k[1].replace("\n","").replace(" ","").split("|") 
    flag = 0
    for i in range(len(attr)) :
        if attr[i] == attribute and domic[i] == "(int)" :
            flag = 1
            break
    if flag == 0:
        return 1
    sumin = 0
    for j in range(3,len(k)):
        tempo = k[j].replace("\n","").replace(" ","").split("|")
        sumin+=int(tempo[i])
    for j in range(3,len(k)):
        nvec.append(k[j].replace("\n","")+"|"+str(sumin)+"\n")
    target = open(filename,"w")
    target.writelines(nvec)
    target.close()
    return 0
def filemaker(outputvector,filename):
    tr = open(filename,"w")
    tr.writelines(outputvector)
    tr.close
    return
def fileappender(outputvector,filename):
    tr = open(filename,"a")
    tr.write("\n")
    tr.writelines(outputvector)
    tr.close
    return
def select(targetfile , condition ):
    global fileindex
    target = open(targetfile , "r" )
    attrib = target.readline()
    attributes = attrib.replace("\n","").split("|")
    domaintype = target.readline()
    dump = target.readline()
    domaintypes = domaintype.replace("\n","").split("|")
    lines = target.readlines()
    target.close()
    op = [attrib,domaintype,"----------------------------------------------------------------\n"]
    linenumber = 0
    while linenumber < len(lines):
        x = condition
        fieldinline = lines[linenumber].replace("\n","").split("|")
        #print linenumber,fieldinline,"for testing"
        for j in range(len(domaintypes)):
            if domaintypes[j] == "(string)" :
                fieldinline[j] = fieldinline[j].replace(fieldinline[j],'"'+fieldinline[j]+'"')
            if attributes[j] in x  :
                x=x.replace(attributes[j],fieldinline[j])
        x=x.replace("and"," and ")
        x=x.replace("or"," or ")
        if  eval(x) :
            op.append(lines[linenumber])
        if linenumber == len(lines) - 1 :
            break
        linenumber+=1
    return op
def project( targetfile , listattr ):
    lst=listattr.replace(",","|")
    listattr=listattr.replace("'","")
    listattr = listattr.replace("\n","").split(",")
    global fileindex
    target = open(targetfile , "r" )
    attrib = target.readline()
    attributes = attrib.replace("\n","").split("|")
    domaintype = target.readline()
    dump = target.readline()
    domaintypes = domaintype.replace("\n","").split("|")
    lines = target.readlines()
    target.close()
    op=[lst+'\n']
    dom=""
    flag = [] 
    for k in range(len(attributes)) :
        flag.append(int(0))
    domain = []
    for l in range(len(listattr)) :
        domain.append("")
    for l in range(len(listattr)) :
        for k in range(len(attributes)):
            if listattr[l] == attributes[k] :
                domain[l]=domaintypes[k]
                flag[k]=1
                dom=dom+domain[l]+"|"
    dom=dom+"\n"
    dom=dom.replace("|\n","\n")
    op.append(dom)
    #print flag
    op.append("-----------------------------------------------------------\n")
    linenumber = 0
    while linenumber < len(lines):
        fieldinline = lines[linenumber].replace("\n","").split("|")
        #print fieldinline
        linn=""
        for j in range(len(domaintypes)):
            if flag[j] :
                linn=linn+str(fieldinline[j])+"|"
        linn=linn+"\n"
        #print linn
        linn=linn.replace("|\n","\n")
        op.append(linn)     
        linenumber+=1
    return op
def cross(file1,file2):
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    silt=[ ]
    for initial in range(3) :
        destn[initial]=destn[initial].replace("\n","")
        src[initial]=src[initial].replace("\n","")
        if initial==2:
            mid="-"
        else :
            mid="|"
        silt.append(destn[initial]+mid+src[initial]+"\n")
    for nr in range(3,len(destn)):
        for nd in range(3,len(src)):
            tttt=destn[nr].replace("\n","")+"|"+src[nd].replace("\n","")+"\n"
            silt.append(tttt)
    t1 = open(file1,"w")    
    t1.writelines(silt)
    t1.close
    return
def copyfile(destn,src):
    t1=open(destn,"w")
    t2=open(src,"r")
    t1.writelines(t2.readlines())
    t1.close()
    t2.close()
    return
def renameop(newname,oldname,listattr):
    old = open(oldname,"r")
    yut = old.readlines()
    old.close
    new = open(newname,"w")
    old = open(oldname,"r")
    if len(listattr)==0 : 
            new.writelines(old.readlines())
            return 0
    listatr=listattr.split(",")
    if len(old.readline().split("|")) != len(listatr) :
        return 1
    satir = [listattr.replace(",","|").replace("\n","")+"\n",old.readline(),old.readline()]
    for indexing in range(3,len(yut)) :
        satir.append(yut[indexing].replace("\n","")+"\n")
    new.writelines(satir)
    new.close()
    old.close()
    old = open(oldname,"w")
    old.close()
    return 0
def nat(file1,file2):
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    attrlistdestn = destn[0].replace("\n","").split("|")
    attrlistsrc = src[0].replace("\n","").split("|")
    domlistdestn = destn[1].replace("\n","").split("|")
    domlistsrc = src[1].replace("\n","").split("|")
    for nr in range(len(attrlistdestn)):
        flg=0
        for nl in range(len(attrlistsrc)):
            xt1=attrlistsrc[nl].split(".")
            xt2=attrlistdestn[nr].split(".")
            if xt1[1]==xt2[1] and domlistsrc[nl]==domlistdestn[nr] :
                flg=1
                break
        if flg:
            break
    copyfile("int1",file1)
    cross("int1",file2)
    if flg==0:
        copyfile(file1,"int1")
        return
    else:
        llll=""
        for i in range(len(attrlistsrc)) :
            if i==nl :
                continue
            llll=llll+attrlistsrc[i]+"|"
        llll=llll+"\n"
        llll=llll.replace("|\n","")
        txt1=select("int1",attrlistsrc[nl]+"=="+attrlistdestn[nr])
        filemaker( txt1 , "txt1" )
        multitoset("txt1")
        txt1=project("txt1",destn[0].replace("|",",").replace("\n","")+","+llll.replace("|",",").replace("\n",""))
        filemaker( txt1 , "txt1")
        multitoset("txt1")
        copyfile(file1,"txt1")
    return
def union(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    ksrc=src[0].split(".")
    kdestn=destn[0].split(".")
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ","") or ksrc[1].replace(" ","") != kdestn[1].replace(" ","") :
        return 1
    t1 = open(file1,"a")
    t1.write("\n")
    t1.writelines(src[3:len(src)])
    t1.close()
    return 0
def diff(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    ksrc=src[0].split(".")
    kdestn=destn[0].split(".")
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ","") or ksrc[1].replace(" ","") != kdestn[1].replace(" ","") :
        return 1
    silt = [destn[0],destn[1],destn[2]]
    for i in range(3,len(src)):
                   src[i]=src[i].replace("\n","")
    for i in range(3,len(destn)):
                   destn[i]=destn[i].replace("\n","")                   
    for nr in range(3,len(destn)):
        if destn[nr] in src[3:len(src)]:
            continue
        silt.append(destn[nr].replace("\n","")+"\n")
    filemaker(silt,file1)
    return 0
def intersect(file1,file2) :
    t1 = open(file1,"r")
    t2 = open(file2,"r")
    destn = t1.readlines()
    src = t2.readlines()
    t1.close()
    t2.close()
    ksrc=src[0].split(".")
    kdestn=destn[0].split(".")
    if src[1].replace("\n","").replace(" ","")!=destn[1].replace("\n","").replace(" ","") or ksrc[1].replace(" ","") != kdestn[1].replace(" ","") :
        return 1
    silt = [destn[0],destn[1],destn[2]]
    for nr in range(3,len(destn)):
        for nd in range(3,len(src)):
            if destn[nr].replace("\n","")==src[nd].replace("\n",""):
                silt.append(destn[nr].replace("\n","")+"\n")
    filemaker(silt,file1)
    return 0
def divide(destination,dividend,divisor):
    t1 = open(dividend,"r")
    t2 = open(divisor,"r")
    numer = t1.readlines()
    denom = t2.readlines()
    t1.close()
    t2.close()
    listnumer=numer[0].replace("\n","").split("|")
    listdenom=denom[0].replace("\n","").split("|")
    for n1 in range(len(listdenom)) :
        if listdenom[n1] not in listnumer :
            return 1
    newattr=[ ]
    newlist=""
    for n1 in range(len(listnumer)) :
        if listnumer[n1] not in listdenom :
            newattr.append(listnumer[n1])
            newlist=newlist+listnumer[n1]+"|"
    newlist=newlist+"\n"
    newlist=newlist.replace("|\n","\n")
    newlist=newlist.replace("\n\n","\n").replace("|",",")
    t1=project(dividend,newlist.replace("\n",""))
    filemaker(t1,"t1")
    multitoset("t1")
    filemaker(t1,"t2a")
    multitoset("t2a")
    copyfile("sct1",divisor)
    cross("sct1","t2a")
    multitoset("sct1")
    sink=diff("sct1",dividend)
    multitoset("sct1")
    t2=project("sct1",newlist.replace("\n","").replace("|",","))
    filemaker(t2,"t2")
    multitoset("t2")
    sink=diff("t1","t2")
    multitoset("t1")
    temp1=open("t1","r")
    temp2=open(destination,"w")
    temp2.writelines(temp1.readlines())
    temp1.close()
    temp2.close()            
def expression(expvector,index):
     tt = []
     k=0
     global fileindex
     if expvector[0]=="help" or expvector[0]=="HELP" or expvector[0]=="Help" or expvector[0]=="hELP" :
        document()
        return tt,1
     if expvector[0]=="assumptions" or expvector[0]=="ASSUMPTIONS" or expvector[0]=="Assumptions" or expvector[0]=="aSSUMPTIONS" :
        assume()
        return tt,1
     if expvector[0]=="display" or expvector[0]=="DISPLAY" or expvector[0]=="Display" or expvector[0]=="dISPLAY" :
        if len(expvector) == 2:
            filenaming = expvector[1]
        else :
            k=fileindex
            fileindex+=1
            xxx,dump = expression(expvector[1:len(expvector)],fileindex)            
            if len(xxx)==0:
                return tt,1
            filenaming = xxx[0]
        displayfile(filenaming)
        return tt,0
     if expvector[0] == "sig" or expvector[0] == "select":
         if expvector[len(expvector) - 2]!="on"   :
             print "# SyntaxError in Expresion.System Rolling Back "
             errno = [' argument instead of " on " ',' length of the expression: number of arguments ']
             print "Unexpected"+errno[len(expvector) % 2 + 1]+'\n'
             return tt,1
         elif len(expvector) == 4 :
             fil = expvector[1]
         else :
             k=fileindex
             fileindex+=1
             xxx,dump = expression(expvector[1:len(expvector)-2],fileindex)
             if len(xxx)==0 :
                 return tt,1
             fil = xxx[0]
         output = select(fil , expvector[len(expvector) - 1])
         filemaker(output,"temp"+str(k))
         tt.append("temp"+str(k))
         return tt,1    
# Projection
     elif expvector[0] == "pi" or expvector[0] == "project" :
        if   expvector[2]!="from"   :
             print "# SyntaxError in Expresion.System Rolling Back "
             errno = ' argument instead of " from " '
             print "Unexpected"+errno+'\n'
             return tt,1
        elif len(expvector) == 4 :
             fil = expvector[3]
        else :
             k=fileindex
             fileindex+=1
             xxx,dump = expression(expvector[3:len(expvector)],fileindex)
             if len(xxx)==0 :
                 return tt,1
             fil = xxx[0]
        output = project(fil , expvector[1])
        filemaker(output,"temp"+str(k))
        tt.append("temp"+str(k))
        return tt,1    
# Rename
     elif expvector[0] == "rho" or expvector[0] == "rename":
         #print "Rho for Rename operator"
         if len(expvector)< 5 :
             print "    # Error in the number of arguments . Try Again "
             return tt,1
         if expvector[len(expvector)-3]!="to":
             print "    # SyntaxError : Expected 'to' at this place "
             return tt,1
         listofattr=expvector[len(expvector)-1]
         if len(expvector)==5 :
             oldname=expvector[1]
         else :
             hyt,uhu = expression(expvector[1:len(expvector)-3],fileindex)
             if len(hyt)==0 :
                 return tt,1
             oldname=hyt[0]
         k=renameop(expvector[len(expvector)-2],oldname,listofattr)
         if k==1:
             print "  # SyntaxError : Error in the number of new attribute names . Type again "
             return tt,1
         tt.append(expvector[len(expvector)-2])
         return tt,1 
# Union
     elif expvector[0] == "union" or expvector[0] == "U":
         #print "Union from Set Theory "
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=union("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Union compatibility.Type again the filetype "
                 return tt,1         
         tt.append("crosstemp")
         return tt,1            
# Intersection
     elif expvector[0] == "intersect" or expvector[0] == "n":
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")         
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=intersect("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Set Difference compatibility.Type again the filetype "
                 return tt,1
         tt.append("crosstemp")
         return tt,1        
# Difference
     elif expvector[0] == "-" or expvector[0] == "minus" or expvector[0] == "diff" or expvector == "difference":
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         if len(fillist)!=2:
             print "     # SyntaxError : Error in the number of relations.Use only 2 relations.Type again "
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             errorflag=diff("crosstemp",fillist[fileptr])
             if errorflag:
                 print "     # SyntaxError : Error in the Set Difference compatibility.Type again the filetype "
                 return tt,1
         tt.append("crosstemp")
         return tt,1
# Cross Product
     elif expvector[0] == "X" or expvector[0] == "cross" :
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             cross("crosstemp",fillist[fileptr])
         tt.append("crosstemp")
         return tt,1
# Sum
     elif expvector[0] == "+" or expvector[0] == "sum" :
         if expvector[len(expvector) - 2] != "in" :
             print "  #    SyntaxError : Expected 'in' here "
             return tt,1
         if "," in expvector[len(expvector)-1] :
             print " # SyntaxError : Number of summing attributes "
             return tt,1
         if len(expvector) == 4 :
             filename = expvector[3]
         else :
             k=fileindex
             fileindex+=1
             xxt,dmp = expression(expvector[1:len(expvector)-2],fileindex)
             if len(xxt)==0 :
                 return tt,1
             filename = xxt[0]
             k = sumup(expvector[len(expvector)-1],filename)
             if k==1 :
                 print " # Error in the summing attribute "
                 return tt,0
             tt.append(filename)
             return tt,1 
# Theta Join
     elif expvector[0] == "(-)" or expvector[0] == "theta" :
         if len(expvector) != 4:
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         if expvector[len(expvector) - 2]!="on"   :
             print "# SyntaxError in Expresion.System Rolling Back "
             errno = [' argument instead of " on " ',' length of the expression: number of arguments ']
             print "Unexpected"+errno[len(expvector) % 2 + 1]+'\n'
             return tt,1
         k=fileindex
         fileindex+=1
         newexpr = "select|cross|"+expvector[1]+"|on|"+expvector[len(expvector)-1]
         newexpr = newexpr.replace(" ","")
         expvector = newexpr.split("|")
         return expression(expvector,fileindex)
# Natural Join
     elif expvector[0] == "*" or expvector[0] == "join" :
         if len(expvector) == 2 :
             fillist = expvector[1]
         else :
             print "     # SyntaxError : Error in the number of arguments.Type again "
             return tt,1
         fillist = fillist.split(",")
         t1 = open(fillist[0],"r")
         t2 = open("crosstemp","w")
         t2.writelines(t1.readlines())
         t1.close()
         t2.close()
         for fileptr in range(1,len(fillist)) :
             nat("crosstemp",fillist[fileptr])
         k=fileindex
         fileindex+=1
         tt.append("crosstemp")
         return tt,1 
# Division Operator
     elif expvector[0] == "%" or expvector[0] == "div" :
         if len(expvector) != 3 :
             print "    # SyntaxError : Error in the number of arguments.Rolling Back. "
             return tt,1
         if divide("divtemp",expvector[1],expvector[2]):
                 print "     # SyntaxError : Error in the Division compatibility.Type again the filetype "
                 return tt,1
         tt.append("divtemp")
         return tt,1
     else :
         print "SyntaxError in Expression.System Rolling Back !!!!!"
         return tt,1
#Program execution starts here
choc=1
print "1. Enter your Expressions \n2. Enter 'help' for help,\n\t 'assumptions' to get the list of assumptions \n\t and 'display <relation r> ' to display relation r.This means you have ended the query .\n\n"  
while choc:
    expr = raw_input("> :Relational_Algebra: >> ")
    expr = expr.replace(" ","")
    expv = expr.split('<--')
    if len(expv)==2:
     expr = expv[1]
    else :
     expr = expv[0]
    expvector = expr.split('|')
    if len(expvector) == 1 and len(expv) == 2:
        copyfile(expv[0].replace("\n","").replace(" ",""),expvector[0].replace("\n","").replace(" ",""))
        choc = 1
        continue
    if len(expv)==1 and  expvector[0]!="display" and expvector[0]!="help" and expvector[0]!="assumptions"  :
        expr="display|"+expr 
        expvector = expr.split("|")
    fileindex = 0
    ll,choc = expression(expvector,fileindex)
    if choc==0 :
        break
    if len(expv)==2:
        ttt=open(ll[0],"r")
        tmt = open(expv[0],"w")
        tmt.writelines(ttt.readlines())
        tmt.close()
        ttt.close()    
print " \n---- Thank You. That ends the program. Press any key to close ----\n"
n = raw_input("")
