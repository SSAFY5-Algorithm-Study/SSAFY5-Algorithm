package week17_7_20;

import java.util.Scanner;

public class BOJ_9655_민지 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        String[] winner = new String[N+1];
        winner[0] = "CY";
        winner[1] = "SK";

        if (N >= 2) {
            for (int i=2; i<=N; i++) {
                winner[i] = winner[i-2];
            }
        }
        System.out.println(winner[N]);
    }
}
