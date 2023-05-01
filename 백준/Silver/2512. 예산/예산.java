import java.io.*;
import java.util.*;

public class Main {

    static int N, TARGET;
    static int[] ARR;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        ARR = new int[N];

        String[] tmp = br.readLine().split(" ");
        for(int i = 0; i < tmp.length; i++) {
            ARR[i] = Integer.parseInt(tmp[i]);
        }
        TARGET = Integer.parseInt(br.readLine());
        Arrays.sort(ARR);
        if (Arrays.stream(ARR).sum() <= TARGET) {
            System.out.println(Arrays.stream(ARR).reduce((a, b) -> a > b ? a : b).getAsInt());
            return;
        }
        System.out.println(binarySearch(ARR, TARGET));
    }

    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = target;

        while (left <= right) {
            int mid = (left + right) / 2;
            int result = calc(mid);
            if (result <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }

    public static int calc(int num) {
        int total = 0;

        for(int i = 0; i < ARR.length; i++) {
            total += Math.min(ARR[i], num);
        }

        return total;
    }
}