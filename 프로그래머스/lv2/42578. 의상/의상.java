import java.util.*;

class Solution {
    
    Map<String, Integer> clothMap = new HashMap<>();
    
    public int solution(String[][] clothes) {
        int answer = 1;
        
        for(int i = 0; i < clothes.length; i++) {
            String kind = clothes[i][1];
            clothMap.put(kind, clothMap.getOrDefault(kind, 0) + 1);
        }
        
        for(int value : clothMap.values())  answer *= value + 1;
        
        return answer - 1;
    }
}