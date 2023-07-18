import java.util.*;


class Solution {
    
    Map<String, Integer> counter = new HashMap<>();
    
    public String solution(String[] participant, String[] completion) {
        
        for(int i = 0; i < participant.length; i++) {
            String key = participant[i];
            counter.put(key, counter.getOrDefault(key, 0) + 1);
        }
        
        for(int i = 0; i < completion.length; i++) {
            String key = completion[i];
            counter.put(key, counter.get(key) - 1);
            
            if (counter.get(key) == 0)
                counter.remove(key);
        }
        
        return getAnswer();
    }

    String getAnswer() {
        String answer = "";
        for(String name : counter.keySet()) {
            return name;    
        }
        return null;
    }
}