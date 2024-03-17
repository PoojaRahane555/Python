# SET:
# 1)UNION: return two set in one set i.e,combine each other,duplicate does not consider
setA = {1,2,3}
setB = {4,5,1}
aa = setA.union(setB)
print(aa)

# 2)INTERSECTION: return same element in set
setC = {1,2,3,4}
setD = {5,2,6,1}
bb = setC.intersection(setD)
print(bb)

# 3)INTERSECTION UPDATE: update value for given set which is same in both set 
setE = {11,33,22,66}
setF = {66,44,88,33}
cc = setE.intersection_update(setF)
print(setE)
print(setF)

# 4)SYMMETRIC DIFFERENCE: removes same element from both set and return in single set
setG = {1,2,3,4}
setH = {5,7,2,1}
dd = setG.symmetric_difference(setH)
print(dd)

# 5)SYMMETRIC DIFFERENCE UPDATE: removes same element from both set,return in single set and update the given set.
ee = setG.symmetric_difference_update(setH)
print(ee)
print(setG)
print(setH)

# 6)DIFFERENCE: removes same element for given set and return as it is element which is not present in others
setI = {11,22,33,66}
setJ = {44,55,22,88}

ff = setI.difference(setJ)
print(ff)

# 7)SYMMETRIC DIFFERENCE UPDATE: removes same element and written remaining element from both set
gg = setI.symmetric_difference_update(setJ)
print(setI)
print(setJ)

# 8)ISSUBSET: every element of this set should be present in next set
setK = {"a","b","c"}
setL = {"a","b","c","d"}
hh = setK.issubset(setL)
print(hh)

# 9)ISSUPERSET: some element should be present in another set
ii =  setL.issuperset(setK)
print(ii)

# 10)ISDISJOINT: return boolean value true for both set has different element rest return false
setM = {11,22,33}
setN = {44,55,66}
jj = setM.isdisjoint(setN)
print(jj)

# 11)Add: add given element in the set
name = {"Pooja","Kavita","Savita","Babita"}
name.add("Vanita")
print(name)

# 12)Pop: removes the random element
kk = name.pop()
print(kk)
print(name)

# 13)Remove: removes the given element
ll = name.remove("Pooja")
print(name)

# 14)Clear: clear the all set
name.clear()
print(name)

# 15)Update: update the given set but can not update single element from set
num = {1,2,3,4}
print(num)

num.update({3,4,5,6,7})
print(num)

# 16)Discard: removes the element from set if it is present and not present still does not give any error
num.discard(8)
print(num)

