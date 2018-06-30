package acmicpc;

import java.util.Scanner;

public class M1924_2 {
	public static void main(String argv[]) {
		
		Scanner sc = new Scanner(System.in);
		
		int day[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 12};
		String mon[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
		
		int m = sc.nextInt();
		int d = sc.nextInt();
		
		for ( int i = 0; i<m-1; i++ ) {
			d += day[i];
		}
		System.out.println(mon[d%7]);
		
		
	}
}
