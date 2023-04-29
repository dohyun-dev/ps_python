import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long target = Long.parseLong(br.readLine());
        System.out.println(binarySearch(target));
    }

    public static long binarySearch(long target) {
        long left = 0l;
        long right = target;

        while (left <= right) {
            long mid = (left + right) / 2;
            long result = (long) Math.pow(mid, 2);

            if (result < target) {
                left = mid + 1;
            } else if (result >= target) {
                right = mid - 1;
            }
        }
        return left;
    }
}