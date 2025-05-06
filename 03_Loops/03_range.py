for n in range(10):
    print(n)

#print(list(range(0,10,2)))
print(list(range(-5,0)))
[print(f"[{x}]={n}") for x,n in enumerate(list(range(10,0,-1)))]

print("\nLista Reversa:")
print(list(range(12)[:0:-1]))

for _ in range(5): print("**")