import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int maximum = 0;
		
		// 배열 초기화
		int[][] tri = new int[N][N];
		
		tri[0][0] = sc.nextInt();
		
		// input 받기
		for (int r=1; r<N; r++) {
			for (int c=0; c<=r; c++) {
				tri[r][c] = sc.nextInt();
				
				if (c==0) {
					tri[r][c] = tri[r][c] + tri[r-1][c];
				}
				else if (r==c) {
					tri[r][c] = tri[r][c] + tri[r-1][c-1];
				}
				else {
					tri[r][c] = tri[r][c] + Math.max(tri[r-1][c-1], tri[r-1][c]);
				}
				
				// 현재 max랑 비교하기
				if (tri[r][c] > maximum) {
					maximum = tri[r][c];
				}
			}
		}
		System.out.println(maximum);
	}
}
