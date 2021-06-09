package week10_6_11;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2644_Minji {
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		 
		int N = sc.nextInt();
		int s = sc.nextInt();
		int e = sc.nextInt();
		int M = sc.nextInt();
		
		List<Integer>[] AL = new ArrayList[N+1];
		for (int i=0; i<=N; i++) {
			AL[i] = new ArrayList<Integer>();
		}
		
		for (int i=0; i<M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			AL[x].add(y);
			AL[y].add(x);
		}
		
		int result = calculateChonsu(s, e, N, AL);
		System.out.println(result);
		
		

	}
	
	private static int calculateChonsu(int s, int e, int N, List<Integer>[] AL) {
		int[] visited = new int[N+1];
		visited[s] = 1;
		
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] {s,0});
		
		while(queue.isEmpty() == false) {
			int[] next = queue.remove();
			
			if (next[0] == e) {
				return next[1];
			}
			
			for (int i: AL[next[0]]) {
				if (visited[i] == 0) {
					queue.add(new int[] {i, next[1]+1});
					visited[i] = 1;
				}
			}
		}
		return -1;
		
//		int[][] hello = new int[5][5];
//		ArrayList<String>[] yeguk = new ArrayList[5];
		
	}

}
