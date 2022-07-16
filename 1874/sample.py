# 스택 수열 (Easy)
# 스택, 그리디

# LIFO, Last in First out
# 그리디(greedy) : 현재 top 에 있는 수가 입력한 목록에서 Pop 하지 않은 가장 앞자리에 있어야 하는 구조

# 예시]  Input : 7 8 1  / Stack : 1 2 7  
# (top 7 과 현재 남아있는 Input 의 앞에 7 과 동일하게 하면서 모두 지울 수 있어야 함)

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1):
    d = int(input())
    
    while count <= d:
        stack.append(count)
        count+=1
        result.append('+')
    if stack[-1] == d:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))



# 중요 포인트
# 가장 Stack 에 가장 위에 있는 값이 Stack 가장 top 값이 입력한 값과 맞아야하고 제일 커야한다.
# 추가된 Count 는 기준 값으로 증가만 하도록 설정해야한다.
