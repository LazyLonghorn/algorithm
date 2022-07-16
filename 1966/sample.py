# 프린터 큐 (Easy)
# 큐, 구현, 그리디

# FIFO - First In First Out

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0) 
        else:
            queue.append(queue.pop(0))


# 중요 포인트
# 가장 큰 값이 맨 앞으로 오도록, 계속 밀고 오는 구조 ( 예시. 1,2,3 -> 2,3,1 -> 3,1,2 )
# 맨 앞에 항목이 제일 큰 경우, 제거하면서 해당 Inedx 에 들어오는 Count 를 계산