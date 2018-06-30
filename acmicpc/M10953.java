package acmicpc;

import java.util.Scanner;

public class M10953 {

	public static void main(String argv[]) {
		//System.out.println("1,5".substring(0,1));
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int i = 0;
		int a = 0;
		int b = 0; 
		while(i < n) {
			String str = sc.next();
			a = Integer.parseInt(str.substring(0, 1));
			b = Integer.parseInt(str.substring(2, 3));
			System.out.println(a+b);
			i++;
		}
		
		
		//System.out.println("This number is " + n);
		
		/*String str2 = sc.nextLine();
		System.out.println(str2);*/

		
	}
	
}
