package acmicpc;

import java.util.Scanner;

public class M10818 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int min = 0;
		int max = 0;
		int i = 0 ;
		int[] li = new int[n];
		while (i < n) {
			li[i] = sc.nextInt();
			i++;
		}
		
		max = li[0];
		min = li[0];
		for (int j = 1; j<n; j++) {
			if(max < li[j]) {
				max = li[j];
			}
			if(min > li[j]) {
				min = li[j];
			}
		}
		System.out.println(min + " " + max);		
		
	}
}
