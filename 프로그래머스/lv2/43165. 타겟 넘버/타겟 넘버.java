import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        return bfs(numbers, target);
    }
    
    int bfs(int[] numbers, int target) {
        Queue<Element> q = new LinkedList<>();
        q.offer(new Element(numbers[0], 0));
        q.offer(new Element(-numbers[0], 0));
        int count = 0;
        
        while (!q.isEmpty()) {
            Element cur = q.poll();
            
            if (cur.idx == numbers.length - 1 && cur.value == target)
                count++;
            
            if (cur.idx + 1 == numbers.length) 
                continue;
            q.offer(new Element(cur.value + numbers[cur.idx + 1], cur.idx + 1));
            q.offer(new Element(cur.value + -numbers[cur.idx + 1], cur.idx + 1));
        }
        return count;
    }
    
    static class Element {
        int value;
        int idx;
        
        Element(int value, int idx) {
            this.value = value;
            this.idx = idx;
        }
    }
}