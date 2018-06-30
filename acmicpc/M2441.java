package acmicpc;

import java.util.Scanner;

public class M2441 {

	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String spc = " ";
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n-i; j++) {
				System.out.print("*");
			}
				System.out.print(((char) 10) + spc);
				spc= " "+spc;
				
		}
	}
	
}
