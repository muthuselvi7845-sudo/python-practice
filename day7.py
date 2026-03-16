#1. Check for Anagram

'''def anagram(s1,s2):
    if len(s1)!=len(s2):
        print("Not anaagram")
        return
    count=[0]*256
    for i in s1:
        count[ord(i)] +=1
    for j in s2:
        count[ord(j)] -=1
    for k in count:
        if k!=0:
            print("Not anaagram")
            return 
    print("Anagram")
anagram("eat","tea")'''

# Check for Anagram using functin and only one time using loop
'''def anagram(s1,s2):
    if len(s1)!=len(s2):
        print("Not anaagram")
        return
    for i in s1:
        if s1.count(i)!=s2.count(i):
            print("Not anaagram")
            return
    print("anagram")
anagram("listen","silent")'''

#check for anagram using function and keyword
'''def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("anagram")
    else:
        print("Not Anagram")
anagram("care","race")'''
# check for anagram using functionn not using keyword only one time 
# for looping
'''def anagram(s1, s2):
    if len(s1) != len(s2):
        return "Not anagram"
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1 
    if count!=[0]*256:
            return "Not anagram"  
    return "Anagram"
s1 = input("enter  a string1")
s2 = input("enter  a string2")
print(anagram(s1.lower(),s2.lower()))'''




