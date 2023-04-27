import java.util.*;

class Solution {
    
    HashMap<String, Integer> map = new HashMap<>();
    
    public String solution(String[] participant, String[] completion) {
        
        // map 초기화
        for(int i = 0; i < participant.length; i++) {
            String person = participant[i];
            if (!map.containsKey(person))
                map.put(person, 0);
            map.put(person, map.get(person) + 1);
        }
        
        // 완주자 빼기
        for(int i = 0; i < completion.length; i++) {
            String person = completion[i];
            map.put(person, map.get(person) - 1);
        }
        // 미완주자 출력
        for(String p : map.keySet()) {
            if (!map.get(p).equals(0)) {
                return p;   
            }
        }
        return "0";
    }
}