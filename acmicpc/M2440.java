package acmicpc;

import java.util.Scanner;

public class M2440 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String[] str = new String[n];
		for (int i = 0; i < n; i++) {
			str[i] = "*";
		}
		
		for (int j = n; j>0; j--) {

			for (int z =0; z < j; z++) {
				System.out.print(str[z]);
			}
			System.out.println("");
		}
		
		
	}
}
