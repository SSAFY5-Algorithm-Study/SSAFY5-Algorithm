package week15_7_6;

import java.util.ArrayList;

public class PRG_게임맵최단거리_민지 {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) {
        int[][] input = {
                {1,0,1,1,1},
                {1,0,1,0,1},
                {1,0,1,1,1},
                {1,1,1,0,1},
                {0,0,0,0,1}
        };
        System.out.println(solution(input));
    }

    static public int bfs(int[][] maps) {
        // R = row의 갯수, C = col의 갯수
        int R = maps.length;
        int C = maps[0].length;
        int nr = 0;
        int nc = 0;

        int[][] visited = new int[R][C];
        for (int r=0; r<R; r++) {
            for (int c=0; c<C; c++) {
                visited[r][c] = 0;
            }
        }
        visited[0][0] = 1;

        ArrayList<int[]> queue = new ArrayList<>();
        queue.add(new int[] {0,0,1});
        while (queue.isEmpty() == false) {
            int[] current = queue.remove(0);
            if (current[0] == R-1 && current[1] == C-1) {
                return current[2];
            }
            for (int i=0; i<=3; i++) {
                nr = current[0] + dr[i];
                nc = current[1] + dc[i];
                if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                    if (visited[nr][nc] == 0 && maps[nr][nc] == 1) {
                        queue.add(new int[]{nr, nc, current[2] + 1});
                        visited[nr][nc] = 1;
                    }
                }
            }
        };
        return -1;
    };

    static public int solution(int[][] maps) {
        int answer = bfs(maps);
        return answer;
    }
}
