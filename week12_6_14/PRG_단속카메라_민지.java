import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[][] routes) {
        int answer = 1;
		Arrays.sort(routes, Comparator.comparing(o -> o[1]));
		int lastCam = routes[0][1];
		        
        for (int[] route: routes) {
            if (route[0] > lastCam) {
                lastCam = route[1];
                answer++;
            }
        }
        return answer;
    }
}