marks[]
for i in range(6):
    marks.append(int(input("Enter marks: ")))
   n=len(marks)
for i in range(n):
    for j in range(0,n-1):
        if marks[j]<marks[j+1]:
                 marks[j],marks[j+1]= marks[j+1],marks[j]

                 print("Sorted marks: ")