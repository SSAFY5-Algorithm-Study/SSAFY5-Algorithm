package week17_7_20;

import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_5567_민지 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        ArrayList<ArrayList<Integer>> friends = new ArrayList<ArrayList<Integer>>(N);

        for (int i=0; i<N+1; i++) {
            friends.add(new ArrayList<Integer>());
        }

        int[] visited = new int[N+1];
        visited[1] = 1;

        for (int i=0; i<M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            friends.get(a).add(b);
            friends.get(b).add(a);
        }

        sc.close();

        int cnt = 0;
        for (int i=0; i<friends.get(1).size(); i++) {
            visited[friends.get(1).get(i)] = 1;
            cnt++;
        }

        for (int i=0; i<friends.get(1).size(); i++) {
            for (int j=0; j<friends.get(i).size(); j++) {
                if (visited[j] == 0) {
                    visited[j] = 1;
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}
