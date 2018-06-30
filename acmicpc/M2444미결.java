package acmicpc;

import java.util.Scanner;

public class M2444미결 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in); 	
		int n = sc.nextInt();
		String star = "*";
		
		for (int i = n; i < 2*n; i++) {
			System.out.printf("%"+i+"s%n", star);
			star = star + "**";
			
		}
		
		for (int j = 2*n-1; j > 0; j--) {

			System.out.println(star.substring(0, 2*n-1 - (2*j-10)));
//			star = star.substring(j)
			System.out.printf("%"+j+"s%n", star);
			
		}
		
	}
	
	
}
