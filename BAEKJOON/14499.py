'''
이동한 칸에 쓰여 있는 수가 0 : 바닥면에 쓰여있는 수가 칸에 복사
0이 아닌 경우 : 칸에 있는 수가 주사위의 바닥면에 복사 되며, 칸에 쓰여있는 수는 0 이된다
주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때
주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하라

만약 바깥으로 이동하려고 하는 경우 해당 명령을 무시하며, 출력도 하면 안 된다
'''

N, M, x, y, K = map(int, input().split())
for _ in range(N):
    pass
    # 북쪽부터 남쪽으로
    # 서쪽부터 동쪽

    
# 주어진 명령
# 1 : 동, 2 : 서, 3 : 북, 4 : 남
cmds = list(map(int, input().split()))