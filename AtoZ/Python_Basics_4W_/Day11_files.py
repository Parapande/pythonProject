# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\gshgshgsh.txt","r")
# print(f.read(10))
#
# print(f.readline())
# print(f.readline())
# print(f.readline())

# for i in f:
#     print(i[0:3])

# write the file
# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\gshgshgsh.txt","a")
#
# f.write("python trainning is on going")

# f.close()
#
# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\gshgshgsh.txt","r")
#
# print(f.read())

# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\gshgshgsh.txt","w")
#
# f.write("i deleted the content from file")
#
# f.close()
#
# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\gshgshgsh.txt","r")
#
# print(f.read())

# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt","x")
#
# f.close()
#
# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt","w")
#
# f.write("new file new content")
#
# f.close()
#
# f= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt","r")
#
# print(f.read())
# print(f.readline())
#
# import os
#
# os.remove("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt")
#

# f1= open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt","x")
# f1.close()
#
# f2 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt","x")
# f2.close()
#
# f1 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt", "w")
# f1.write("hello\nmy\nname\nis\nparag")
# f1.close()
#
# f1 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt", "r")
#
# f2 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "w")
# a = f1.readline()
# print(type(len(a)))
#
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         f2.write(a[i])
# f2.close()
# f2 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "r")
# print(f2.read())
# f2.close()
#
# # f1 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\parag.txt", "r")
# # print(f1.read())


# opening the file
file1 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "r")

# creating another file to store odd lines
file2 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "w")

# reading content of the files
# and writing odd lines to another file
lines = file1.readlines()
type(lines)
for i in range(0, len(lines)):
	if(i % 2 != 0):
		file2.write(lines[i])

# closing the files
file1.close()
file2.close()

# opening the files and printing their content
# file1 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "r")
# file2 = open("C:\\Users\parag.pande\Desktop\Python_Project_Evertz\\ashish.txt", "r")
#
# # reading and printing the files content
# str1 = file1.read()
# str2 = file2.read()
#
# print("file1 content...")
# print(str1)
#
# print() # to print new line
#
# print("file2 content...")
# print(str2)
#
# # closing the files
# file1.close()
# file2.close()
