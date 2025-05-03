list1=[25,"Harry","Hello","World"]
print(list1[0])
print(list1[:5])

# tuple methods
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1.count(2))

dic={
    "a":10,
    "b":11,
    "c":12,
    "d":13
    }
print(dic)
print(dic.get("a"))
print(dic.items())
# print(dic[0])
s={} #Empty Dictnary

# Sets
s={1,2,3,4,4,4,4}
print(s)
s.add(5)
s.remove(4)
s1={1,2,3,4}
s2={4,5,6,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)

# Practice 
d1={"SuPrabhat":"GoodMorning",
    "subhratyri":"GoodNight",
    "Namaskar":"Hello"
    }
user=input("you want which translation : SuPrabhat,subhratri,Namaskar")

print(d1[user])