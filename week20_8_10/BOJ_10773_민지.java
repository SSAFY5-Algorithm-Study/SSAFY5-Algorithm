package week20_8_10;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_10773_민지 {
    public static void main(String[] args) throws Exception{
        // input 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer> stack = new ArrayList<Integer>();
        for (int i=0; i<N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                stack.remove(stack.size()-1);
            } else {
                stack.add(num);
            }
        }
        br.close();
        int sum = 0;
        for (int i : stack) {
            sum += i;
        }
        System.out.println(sum);
    }
}
