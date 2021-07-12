package week14_6_29;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_9625 {
	public static void main(String[] args) {
		int k = 0;
		
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			k = Integer.parseInt(br.readLine());
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		int[] adp = new int[46];
		int[] bdp = new int[46];
		
		adp[0] = 1;
		bdp[1] = 1;
		
		for (int i = 2; i <= k; i++) {
			adp[i] = bdp[i-1];
			bdp[i] = adp[i-1] + bdp[i-1];
		}
		System.out.println(adp[k] + " " + bdp[k]);
	}
	
}
