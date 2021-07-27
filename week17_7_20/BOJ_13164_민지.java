package week17_7_20;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class BOJ_13164_민지 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] children = new int[N];
        for (int i=0; i<N; i++) {
            children[i] = sc.nextInt();
        }
        sc.close();

        PriorityQueue<Integer> deltas = new PriorityQueue<>(Collections.reverseOrder());
        int cost = 0;
        int delta = 0;

        for (int i=1; i<N; i++) {
            delta = children[i] - children[i-1];
            deltas.add(delta);
            cost += delta;
        }

        for (int i=1; i<K; i++) {
            cost -= deltas.poll();
        }

        System.out.println(cost);
    }
}
