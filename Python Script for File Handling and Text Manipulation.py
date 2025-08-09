import os 

path=input("paste the path")

if os.path.exists(path):
    os.chdir(path)
    lst=os.listdir()
    print(lst)
    choice=input("enter the file with extention as in the directory")
    if os.path.exists(choice):
        with open(choice,'r') as f:
              for alter in f:
                   print("1.search a word \n2.replace the word\n3.count words\n4.separate point by point")
                   ch=int(input("enter the service now "))
                   if(ch==1):
                        fi=f.read()
                        search=input("enter the word to search")
                        if search in fi:
                             print(search,"it is present")
                        else:
                             print("it is not present")
                    
                   if(ch==2):
                        rep=f.read()
                        originalwrd=input("enter the original word")
                        if originalwrd in rep:
                            replacewrd=input("enter the replacement word")
                            r=rep.replace(originalwrd,replacewrd)
                            with open("replaced1.txt",'w') as s:
                                 s.write(r)

                        else:
                             print("word is not present")
                    
                   if(ch==3):
                        count=f.read()
                        entr=input("enter the word ")
                        if entr in count:
                             print("this much present then the whole file",count.count(entr))
                        else:
                             print("word not found")

                   if(ch==4):
                        split=f.read()
                        sp=split.replace(".","\n * ")
                        with open("splited1.txt","w") as spi:
                             spi.write(sp)




                    
                             
                        
                      


    else:
         print("file doesn't exists")
    


else:
     print(path," does n't exists")