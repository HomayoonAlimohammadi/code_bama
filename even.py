start = int(input('Enter Start: '))
end = int(input('Enter end: '))

### With if:
for i in range(start, end+1):
    if not i % 2:
        print(i)

print()
print()
### With Step:
if start % 2:
    start += 1

for i in range(start, end+1, 2):
    print(i)