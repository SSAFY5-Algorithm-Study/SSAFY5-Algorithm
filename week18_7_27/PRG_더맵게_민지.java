package week18_7_27;

import java.util.PriorityQueue;

public class PRG_더맵게 {
    public static void main(String[] args) {
        int[] scoville = {1, 2, 3, 9, 10, 12};
        int K = 7;

        // Python에서 heapify 함수를 쓰는것과 같은 원리
        // 메모리 절약을 위해서는 heap을 직접 배열에 구현하여 쓰는게 좋음
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        for (int i=0; i<scoville.length; i++) {
            heap.add(scoville[i]);
        }

        int cnt = 0;
        while (heap.peek() < K) {
            if (scoville.length < 2) {
                cnt = -1;
                break;
            }

            int a = heap.poll();
            int b = heap.poll();
            heap.add(a + b*2);
            cnt++;
        }

        System.out.println(cnt);
    }
}
