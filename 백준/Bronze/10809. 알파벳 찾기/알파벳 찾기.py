w = input()
alst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nlst = []

for i in alst:
    a = w.find(i)
    nlst.append(str(a))
    
print(" ".join(nlst))