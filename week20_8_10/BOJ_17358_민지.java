package week20_8_10;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_17358 {
    public static void main(String[] args) throws Exception{
        // 입력 코드
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        br.close();

        // dp 리스트 초기화
        double[] dp = new double[N+1];
        for (int i=0; i<N; i++) {
            dp[i] = 1;
        }

        // 점화식으로 값 도출하기
        // 2씩 건너뛰면서 for loop 작성하려면 아래 문법같이 작성해야됨
        for (int i=2; i<=N; i+=2) {
            dp[i] = (dp[i-2] * (i-1)) % (Math.pow(10,9)+7);
        }
        System.out.println((int) dp[N]);
    }
}
