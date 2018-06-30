package acmicpc;

import java.util.Scanner;

public class M2440_2 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < n; i++) {
			for (int j = 0; j< n-i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		
	}
}
