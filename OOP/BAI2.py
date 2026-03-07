name = input("Nhap vao ten cua ban: ")

# cắt
name = name.strip()

# tách
words = name.split()
words = [w.capitalize() for w in words]

print(f"Ho: {words[0]}")

print("Ten dem:", end=" ")
for i in range(1, len(words)-1):
    print(words[i], end=" ")

print()
print(f"Ten: {words[-1]}")