package acmicpc;

import java.util.Scanner;

public class M2442 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a = (2*n)-1;
		String star = "*";
		
		for(int i = n; i < 2*n; i++) {
		
		System.out.printf("%" + i + "s%n", star);
		
		star = star + "**";	
			
		}
		
	}
}
