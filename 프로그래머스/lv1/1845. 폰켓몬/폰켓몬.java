import java.util.*;

class Solution {

    Set<Integer> check = new HashSet<>();
    
    public int solution(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            check.add(nums[i]);
        }
        
        return Math.min(check.size(), nums.length / 2);
    }
}