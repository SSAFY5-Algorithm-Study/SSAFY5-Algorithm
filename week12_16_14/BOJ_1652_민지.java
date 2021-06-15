package week12_16_14;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1652 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// 입력 받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String[] room = new String[N];
		
		for (int i = 0; i < room.length; i++) {
			room[i] = br.readLine();
		}
		br.close();
		
		int cnt;
		int row_cnt = 0;
		int col_cnt = 0;
		
		// 가로 탐색 
		for (int i=0; i<N; i++) {
			cnt = 0;
			for (int j=0; j<N; j++) {
				if (room[i].charAt(j) == '.') {
					cnt++;
				} else {
					if (cnt >= 2) {
						row_cnt += 1;
					}
					cnt = 0;
				}
			}
			if (cnt >= 2) {
				row_cnt++;
			}
		}
		
		// 세로 탐색 
		for (int i=0; i<N; i++) {
			cnt = 0;
			for (int j=0; j<N; j++) {
				if (room[j].charAt(i) == '.') {
					cnt++;
				} else {
					if (cnt >= 2) {
						col_cnt += 1;
					}
					cnt = 0;
				}
			}
			if (cnt >= 2) {
				col_cnt++;
			}
		}	
		System.out.println(row_cnt + " " + col_cnt);
	}
}
