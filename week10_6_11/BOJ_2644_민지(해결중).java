package week10;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2644_Minji {
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		 
		int N = sc.nextInt();
		int s = sc.nextInt();
		int e = sc.nextInt();
		int M = sc.nextInt();
		
		ArrayList<Integer>[] AL = new ArrayList[N+1];
		
		for (int i=0; i<M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			AL[x].add(y);
			AL[y].add(x);
		}
		
		int result = calculateChonsu(s, e, N);
		

	}
	
	private static int calculateChonsu(int A, int B, int N) {
		int[] visited = new int[N+1];
		
		Queue<int[]> queue = new LinkedList<int[]>();
		queue.add(new int[] {A,0});
		
		while(queue.isEmpty() == false) {

		}
//		int[][] hello = new int[5][5];
//		ArrayList<String>[] yeguk = new ArrayList[5];
		
		
		return B;
		
	}

}