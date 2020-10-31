s = 'django'

print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[-2:])
print(s[::-1])

l = [3,7,[1,4,'hello']]
print(l)
l[2][2]='goodbye'
print(l)

d1 = {'simple_key':'hello'}
print(d1.get('simple_key'))
print(d1['simple_key'])
d2 = {'k1':{'k2':'hello'}}
print(d2.get('k1').get('k2'))
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3.get('k1')[0].get('nest_key')[1][0])

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

age = 4
name = "Sammy"
string = "Hello my dog's name is {} and he is {} years old".format(name,age)
print(string)

mylist = [1,2,3,4,5,6,7,8]


evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))


tweet = "Go Sports! #Sports"
result = tweet.split("#")[1]
print(result)

