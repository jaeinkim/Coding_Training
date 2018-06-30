package acmicpc;

import java.util.Scanner;

public class M2439 {
	public static void main(String[] argv) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String star = "*";
		String string = "";
		String str[] = new String[n];
		
		for(int i = 0; i < n; i++) {
			str[i] = " ";
		}
		
		for(int j = n-1; j >= 0; j--) {
			str[j] = star;
			for(String str1 : str) {
				string = string+str1;
			}
			System.out.println(string);
			string = "";
			
		}
		
		
	}
}


