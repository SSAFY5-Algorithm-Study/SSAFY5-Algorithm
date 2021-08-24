package week20_8_10;

import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_1325_민지 {
    public static void main(String[] args) {
        // input 받기
        // Java에서 변수 초기화 하는 기본적인 문법: <변수 타입> <변수 이름> = <Instance 초기화>
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 컴퓨터의 갯수
        int M = sc.nextInt(); // 연결고리의 갯수
        int maxCnt = 0;
        ArrayList<Integer> maxNodes = new ArrayList<>();

        // 2D 리스트 만들기
        ArrayList<ArrayList<Integer>> AL = new ArrayList<>();
        // 리스트 안에 빈 리스트 채우기
        for (int i=0; i<=N; i++) {
            AL.add(new ArrayList<>());
        }
        // 관계를 AL에 표시하기
        // A가 --> B를 신뢰하는 상황이라면 B를 해킹했을때 --> A도 해킹할 수 있음
        // AL[B]에 A를 추가
        for (int i=0; i<M; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            AL.get(B).add(A);
        }

        // 시작점을 1~N으로 설정해서 각각 DFS를 돈다
        for (int s=1; s<N; s++) {
            // java에서 int array는 자동으로 0으로 초기화된다
            int[] visited = new int[N+1];
            visited[s] = 1;
            ArrayList<Integer> stack = new ArrayList<>();
            stack.add(s);
            int cnt = 1;

            while (stack.isEmpty() == false) {
                int current = stack.remove(stack.size()-1);
                for (int i : AL.get(current)) {
                    if (visited[i] == 0) {
                        visited[i] = 1;
                        stack.add(i);
                        cnt++;
                    }
                }
            }

            if (cnt > maxCnt) {
                maxCnt = cnt;
                maxNodes = new ArrayList<>();
                maxNodes.add(s);
            } else if (cnt == maxCnt) {
                maxNodes.add(s);
            }
        }

        for (int i=0; i<maxNodes.size(); i++) {
            if (i == maxNodes.size()-1) {
                System.out.print(maxNodes.get(i));
            } else {
                System.out.print(maxNodes.get(i) + " ");
            }
        }
    }
}
