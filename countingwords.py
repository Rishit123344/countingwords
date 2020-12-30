introstring=input("enter you'r intoduction")
print(introstring)
charactercount=0
wordcount=1
for i in introstring:
    charactercount=charactercount+1
    if (i==" "):
     wordcount=wordcount+1
     charactercount=charactercount-1

print(charactercount)
print(wordcount)