import java.util.*;

class Solution {
    
    int count;
    HashSet<Integer> set;
    
    public int solution(int[] nums) {
        // 입력
        int answer = 0;
        count = nums.length / 2;
        set = new HashSet<>();
        
        // set에 원소 넣기
        for(int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        return Math.min(count, set.size());
    }
}