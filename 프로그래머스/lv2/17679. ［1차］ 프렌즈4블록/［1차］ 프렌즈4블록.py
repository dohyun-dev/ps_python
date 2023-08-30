def solution(m, n, board):
    
    def pang():
        tmp = []
        for i in range(m-1):
            for j in range(n-1):
                
                if board[i][j] == '0':
                    continue
                
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    flag = True
                    for nx, ny in [(i, j), (i, j+1), (i+1, j), (i+1, j+1)]:
                        tmp.append((nx, ny))
            
        for nx, ny in tmp:
            board[nx][ny] = '0'
            
        return tmp
                        
    
    def fall():
        for i in range(n):
            stack = [board[j][i] for j in range(m) if board[j][i] != '0']
            stack = ['0'] * (m - len(stack)) + stack
            
            for j in range(m-1, -1, -1):
                if not stack:
                    break
                board[j][i] = stack.pop()
                
    
    board = [list(b) for b in board]
    flag = True
    while flag:
        if not pang():
            flag = False
        fall()
    
    return sum(b.count('0') for b in board)