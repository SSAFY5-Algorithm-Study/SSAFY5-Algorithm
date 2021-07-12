package week15_7_6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_13301_민지 {
    public static void main(String[] args) {
        int N = 0;
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            N = Integer.parseInt(br.readLine());
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        };

        long[] length = new long[N+1];
        length[0] = 1;
        length[1] = 1;

        if (N >= 2) {
            for (int i=2; i<=N; i++) {
                length[i] = length[i-1] + length[i-2];
            }
        }

        long parameter = length[N] * 2 + length[N-1] * 2;

        System.out.println(parameter);
    }
}