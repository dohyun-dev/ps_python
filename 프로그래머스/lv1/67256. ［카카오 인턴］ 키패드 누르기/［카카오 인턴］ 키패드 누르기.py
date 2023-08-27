def push(target_x, target_y, hand_type, hand_location, answer):
    if hand_type == "L":
        hand_location[0], hand_location[1] = target_x, target_y
    else:
        hand_location[2], hand_location[3] = target_x, target_y
    answer.append(hand_type)

def solution(numbers, hand):
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
    hand_location = [3, 0, 3, 2]
    answer = []
    
    for num in numbers:
        target_x, target_y = list(filter(
                lambda x: board[x[0]][x[1]] == num, 
                [(i, j) for i in range(4) for j in range(3)]
            ))[0]
        if num in {1, 4, 7}:
            push(target_x, target_y, "L", hand_location, answer)
        elif num in {3, 6, 9}:
            push(target_x, target_y, "R", hand_location, answer)
        else:
            
            left_dist = abs(target_x - hand_location[0]) + abs(target_y - hand_location[1])
            right_dist = abs(target_x - hand_location[2]) + abs(target_y - hand_location[3])
            
            if left_dist < right_dist:
                push(target_x, target_y, "L", hand_location, answer)
            elif left_dist > right_dist:
                push(target_x, target_y, "R", hand_location, answer)
            else:
                push(target_x, target_y, "R" if hand == "right" else "L", hand_location, answer)
    return "".join(answer)