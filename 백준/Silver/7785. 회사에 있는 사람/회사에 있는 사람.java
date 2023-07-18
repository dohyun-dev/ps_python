import java.io.*;
import java.util.*;

public class Main {

    static Set<String> checkMap = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            if (input[1].equals("enter")) {
                checkMap.add(input[0]);
            } else {
                checkMap.remove(input[0]);
            }
        }

        List<String> answer = new ArrayList<>(checkMap);
        Collections.sort(answer, Collections.reverseOrder());
        for(String p : answer) {
            System.out.println(p);
        }
    }
}