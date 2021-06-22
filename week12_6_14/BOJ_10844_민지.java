package week12;

import java.util.Arrays;
import java.util.Scanner;

public class BOJ_10844 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[][] dp = new int[N+1][10];
		
		for (int i = 1; i <= 9; i++) {
			dp[1][i] = 1;
		}
		
		
		for (int i = 2; i < dp.length; i++) {
			for (int j = 0; j < 10; j++) {
				if (j == 0) {
					dp[i][j] = dp[i-1][j+1];
				}
				else if (j == 9) {
					dp[i][j] = dp[i-1][j-1];
				}
				else {
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000;
				}
			}
		}
		
		int cnt = Arrays.stream(dp[N]).sum() % 1000000000;
		
		System.out.println(cnt);
	}

}