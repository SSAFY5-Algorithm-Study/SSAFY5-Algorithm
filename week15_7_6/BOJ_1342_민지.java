package week15_7_6;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BOJ_1342_민지 {
	private static Set<String> wordSet = new HashSet<String>();
	private static int[] visited;
	private static String raw = "";
	
	public static void main(String[] args) {

		
		// Input 받기
		try {
			Scanner sc = new Scanner(System.in);
			raw = sc.next();
			sc.close();
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		visited = new int[raw.length()];
		for (int i = 0; i < visited.length; i++) {
			visited[i] = 0;
		}
		
		for (int i = 0; i < visited.length; i++) {
			visited[i] = 1;
			isLuckyWord(1, raw.charAt(i), String.valueOf(raw.charAt(i)));
			visited[i] = 0;
		};
		System.out.println(wordSet.size());
	}
	
	private static void isLuckyWord(int level, char prev, String word) {
		if (level == visited.length) {
			wordSet.add(word);
			return;
		}
		
		for (int i = 0; i < visited.length; i++) {
			if (visited[i] == 0 & raw.charAt(i) != prev) {
				visited[i] = 1;
				isLuckyWord(level+1, raw.charAt(i), word + String.valueOf(raw.charAt(i)));
				visited[i] = 0;
			}
		}
	};
}
