p = {2:1/36,3:2/36,4:3/36,5:4/36,6:5/36,7:6/36,8:5/36,9:4/36,10:3/36,11:2/36,12:1/36}
s = input()
x = [int(i) for i in input().split()]
print(sum(p[i] for i in x))