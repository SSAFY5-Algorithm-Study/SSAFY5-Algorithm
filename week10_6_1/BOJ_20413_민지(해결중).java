package week10_6_11;

import java.util.HashMap;
import java.util.Scanner;

public class BOJ_20413_민지(해결중) {
  public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		HashMap<Character, Integer> tierMax = new HashMap<>();
		tierMax.put('B', sc.nextInt()-1);
		tierMax.put('S', sc.nextInt()-1);
		tierMax.put('G', sc.nextInt()-1);
		tierMax.put('P', sc.nextInt()-1);
		
		String tierAll = sc.next();
		sc.close();
		
		
		int current = tierMax.get(tierAll.charAt(0));
		int total = current;
		
		
		
		for (int i=1; i<n; i++) {
			char tier = tierAll.charAt(i);
			if (tier == 'D') {
				current = 500; 
			} else {
				current = tierMax.get(tier) - current;
			}
			total += current;
		}
		
		System.out.println(total);
		
	}
}
