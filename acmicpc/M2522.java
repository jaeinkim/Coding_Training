package acmicpc;

import java.util.Scanner;

public class M2522 {
	public static void main(String argv[]) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int t = 1;
		
		String star = "*";
		
		for(int i = 0; i < 2*n - 1 ; i++ ) {
			
			if(i < n) {
			System.out.printf("%"+n+"s%n", star);
			star = star + "*";
			}

			if(i >= n) {
				t++;
				System.out.printf("%"+n+"s%n", star.substring(t));
			}
			
		}
		
		
		
	}
}	
