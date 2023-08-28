

def solution(board, moves):
    def peek(idx):
        for i in range(len(board)):
            if board[i][idx] != 0:
                result = board[i][idx]
                board[i][idx] = 0
                return result
        return None
    
    stack = []
    answer = 0
    
    for move in moves:
        result = peek(move-1)
        
        if result != None:
            stack.append(result)
            
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop(); stack.pop() 
    return answer