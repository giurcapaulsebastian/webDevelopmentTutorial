def arrayCheck(numbers):
    i=2
    size = len(numbers)
    while i <= size:
        chunk = numbers[i-3:i:1]
        print(numbers[i-3:i:1])
        if [1,2,3] == chunk:
            return True
        i=i+1
    return False

print(arrayCheck([1,1,2,2,1,1]))
# numbers = [1,1,2,3,1]
# chunk = numbers[:4:1]
# print(chunk)

def stringBits(word):
    return word[::2]

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

def end_other(a,b):
     a = a.lower()
     b = b.lower()
     if len(a) > len(b):
        size=len(b)
        string = a[-size:]
        print(string)
        return string==b
     else:
        size=len(a)
        string = b[-size:]
        print(string)
        return string==a

print(end_other('hiabc','abc'))
print(end_other('AbC', 'HiaBc') )
print(end_other('abc', 'abXabc') )

def doubleChar(string):
    result=''
    for i in string:
        result = result + i + i
    return result

print(doubleChar("The"))

def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a+b+c
  

def fix_teen(n):
    if n == 15 or n == 16:
        return n
    if n >= 13 and n <=19:
        return 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

def count_evens(nums):
    count=0
    for i in nums:
        if i % 2 == 0:
            count = count+1
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0