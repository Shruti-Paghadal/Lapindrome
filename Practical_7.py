# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 
#Github link: 
print ("\n------------------------------------PRACTICAL 7-----------------------------------\n")
A = int(input())
for i in range(A):
    n = input()
    l = len(n)
    if l % 2 == 0:
        b, c = n[:l//2], n[l//2:]
    else:
        b, c = n[:l//2], n[l//2+1:]
    if sorted(b) == sorted(c):
        print("YES, it is a lapindrome")
    else:
        print("NO, it is not a lapindrome")
print("\n------------------------------------------END OF PRACTICAL 7-------------------\n")