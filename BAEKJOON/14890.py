'''
길 : 한 행 또는 한 열 전부, 한 쪽 끝에서 다른쪽 끝까지 가는 것
길을 지나갈 수 있는 조건
길에 속한 모든 칸의 높이가 모두 같아야 한다
또는 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다
경사로는 항상 높이가 1 이며, 길이는 L 이다
경사로는 낮은 칸과 높은 칸을 연결한다

경사로 조건
1. 낮은 칸에 놓으며, L 개의 연속된 칸에 경사로의 바닥이 모두 접해야함
2. 낮은 칸과 높은 칸의 차이는 1이어야 함
3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어있어야한다

경사로 놓을 수 없을 조건
1. 경사로를 놓은 곳에 또 경사로를 놓는 경우
2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
4. 경사로를 놓다가 범위를 벗어나는 경우
'''