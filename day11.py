# Convert decimal to binary without bin()
'''def dec_to_bin(n):
    if n==0:
        print("Binary:0")
        return
    binary=""
    while n>0:
        digit=n%2
        binary=str(digit)+binary
        n=n//2
    print("Binary:",binary)
n=int(input("Enter a number:"))
dec_to_bin(n)'''

#  Reverse words in a sentence

'''def reverse_word():
    S=input("Enter a Sentence:")
    word=S.split()
    rev=" ".join(word[::-1])
    print(rev)
reverse_word()'''

#  Count vowels and consonants
'''def count_vowel_consonant():
    S=input("Enter a string:").lower()
    vowel="aeiou"
    v=0
    c=0
    for i in S:
        if i.isalpha():
            if i in vowel:
                v+=1
            else:
                c+=1
    print("Vowel:",v)
    print("Count:",c)
count_vowel_consonant()'''
