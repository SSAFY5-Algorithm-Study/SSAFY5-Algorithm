package week15_7_6;

public class PRG_징검다리건너기_민지 {
    static public int max(int[] stones, int s, int e) {
        int max = stones[s];
        for (int i=s; i<e; i++) {
            if (stones[i] > max) {
                max = stones[i];
            }
         }
        return max;
    }

    static public int solution(int[] stones, int k) {
        int partMax = max(stones, 0, k);
        int minMax = partMax;

        for (int i=0; i<(stones.length-k); i++) {
            if (partMax == stones[i]) {
                partMax = max(stones, i+1, i+k+1);
                if (partMax < minMax) {
                    minMax = partMax;
                }
            }
        }
        return minMax;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[] {2,4,5,3,2,1,4,2,5,1}, 3));
    }
}

