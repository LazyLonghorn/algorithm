# 음계 (Easy)
# 배열, 구현

inVal = list(map(int, input().split()))

ascType = True
descType = True

for idx in range(1, len(inVal)):
    if inVal[idx] > inVal[idx - 1]:
        descType = False
    elif inVal[idx] < inVal[idx - 1]:
        ascType = False

if ascType:
    print("ascending")
elif descType:
    print("descending")
else:
    print("mixed")