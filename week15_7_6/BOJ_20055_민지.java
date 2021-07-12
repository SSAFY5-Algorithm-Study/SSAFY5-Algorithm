package week15_7_6;

import java.util.ArrayList;
import java.util.Scanner;

public class BOJ_20055 {
    static int N = 0;
    static int K = 0;
    static ArrayList<Integer> belt = new ArrayList<>();
    static ArrayList<Integer> robots = new ArrayList<>();
    static int zeroCnt = 0;

    public static void removeRobot() {
        if (robots.get(N-1) == 1) {
            robots.set(N-1, 0);
        }
    }

    public static void moveBelt() {
        belt.add(0, belt.remove(2*N-1));
        robots.add(0, robots.remove(2*N-1));
        removeRobot();
    }

    public static void moveRobots() {
        for (int i=N-2; i>=1; i--) {
            if (robots.get(i) == 1 && robots.get(i+1) == 0 && belt.get(i+1) >= 1) {
                robots.set(i, 0);
                robots.set(i+1, 1);
                belt.set(i+1, belt.get(i+1)-1);
                if (belt.get(i+1) == 0) {
                    zeroCnt++;
                }
            }
        }

        if (robots.get(0) == 0 && belt.get(0) >= 1) {
            robots.set(0, 1);
            belt.set(0, belt.get(0)-1);
            if (belt.get(0) == 0) {
                zeroCnt++;
            }
        }
        removeRobot();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();

        for (int i=0; i<(2*N); i++) {
            belt.add(sc.nextInt());
        }
        sc.close();

        for (int i=0; i < (2*N); i++) {
            robots.add(0);
        }

        int loop = 0;

        while (zeroCnt < K) {
            moveBelt();
            moveRobots();
            loop++;
        }
        System.out.println(loop);
    }
}