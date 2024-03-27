file= open('/Users/ankita/PycharmProjects/testseleniumproject/pythonBasics/textfile.txt')
 #all contents of file
#print(file.read())
print("**********************")
#print(file.read(5)) #reads specific chaaracters by passing parameter as number

# if added read with parameter and readline, interprter will continue reading from the same line.
# for example if curson is ar char  5 when readline exceuted it will from 6 char


#read file line by line
print(file.readline())


file.close()
