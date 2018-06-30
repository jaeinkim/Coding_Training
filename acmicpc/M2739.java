package acmicpc;

import java.util.Scanner;

public class M2739 {
	public static void main(String argv[]) {
		Scanner	sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 1; i<=9; i++) {
			System.out.println(n + " * " + i + " = " + (n * i));
		}
		
	}
}
