import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] board;
    static int[] dx = new int[] {-1, 0, 1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        M = Integer.parseInt(tmp[0]);   N = Integer.parseInt(tmp[1]);
        board = new int[N][M];

        for(int i = 0; i < N; i++) {
            tmp = br.readLine().split(" ");
            for(int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        int answer = bfs();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(answer);
    }

    public static int bfs() {
        Queue<Point> q = makeQ();
        int maxValue = 0;

        while(!q.isEmpty()) {
            Point cur = q.poll();
            maxValue = Math.max(maxValue, cur.dist);

            for(int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (0 > nx || nx >= N || 0 > ny || ny >= M || board[nx][ny] == -1) {
                    continue;
                }

                q.offer(new Point(nx, ny, cur.dist + 1));
                board[nx][ny] = -1;
            }
        }
        return maxValue;
    }

    public static Queue<Point> makeQ() {
        Queue<Point> q = new LinkedList<>();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if (board[i][j] == 1) {
                    q.offer(new Point(i, j, 0));
                    board[i][j] = -1;
                }
            }
        }
        return q;
    }

    static class Point {
        int x, y, dist;

        Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        int getX() {
            return x;
        }

        int getY() {
            return y;
        }

        int getDist() {
            return dist;
        }

        public String toString() {
            return String.format("(%d, %d, %d)", x, y, dist);
        }
    }
}