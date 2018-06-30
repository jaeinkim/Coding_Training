package acmicpc;

import java.util.Scanner;

public class M1924 {
	public static void main(String argv[]) {
		Scanner	sc = new Scanner(System.in);
		
		int m = sc.nextInt();
		int d = sc.nextInt();
		
		int n = 0;
		
		switch(m) {
		case 1:
			n = d%7;
			break;
		case 2:
			n = (31+d)%7;
			break;
		case 3:
			n = (31 + 28 +d)%7;
			break;
		case 4:
			n = (31 + 28 + 31 + d)%7;
			break;
		case 5:
			n = (31 + 28 + 31 + 30 + d)%7;
			break;
		case 6:
			n = (31 + 28 + 31 + 30 + 31 + d)%7;
			break;
		case 7:
			n = (31 + 28 + 31 + 30 + 31 + 30 + d)%7;
			break;
		case 8:
			n = (31 + 28 + 31 + 30 + 31 + 30 + 31 +d)%7;
			break;
		case 9:
			n = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + d)%7;
			break;
		case 10:
			n = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d)%7;
			break;
		case 11:
			n = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d)%7;
			break;
		case 12:
			n = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d)%7;
			break;
		}
		
		switch(n) {
		case 1:
			System.out.println("MON");
			break;

		case 2:
			System.out.println("TUE");
			break;

		case 3:
			System.out.println("WED");
			break;

		case 4:
			System.out.println("THU");
			break;

		case 5:
			System.out.println("FRI");
			break;

		case 6:
			System.out.println("SAT");
			break;

		case 0:
			System.out.println("SUN");
			break;

		
		}
		
		
		
	}
}
