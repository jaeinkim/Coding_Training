package acmicpc;

import java.util.Scanner;

public class M11021 {

	public static void main(String argv[]) {
		//System.out.println("1,5".substring(0,1));
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int i = 1;
		int a = 0;
		int b = 0; 
		while(i <= n) {
			
			a = sc.nextInt();
			b = sc.nextInt();
			System.out.println("Case #"+i+": "+(a+b));
			i++;
		}
		
	}
	
}
