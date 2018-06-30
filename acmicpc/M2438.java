package acmicpc;

import java.util.Scanner;

public class M2438 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String star = "*";
		String str = "";
		for(int i = 0; i < n; i++) {
			
			str += star;
			System.out.println(str);
		}
		
	}
}
