import java.util.*;

class Solution {
    
    Set<String> check = new HashSet<>();
    
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book, (a, b) -> a.length() - b.length());
        for(int i = 0; i < phone_book.length; i++) {
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < phone_book[i].length(); j++) {
                sb.append(phone_book[i].charAt(j));
                if (check.contains(sb.toString()))
                    return false;
            }
            check.add(sb.toString());
        }
        return true;
    }
}