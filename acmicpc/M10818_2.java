package acmicpc;

import java.util.Arrays;
import java.util.Scanner;

public class M10818_2 {
	public static void main(String[] argv) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int i = 0 ;
		int[] li = new int[n];
		while (i < n) {
			li[i] = sc.nextInt();
			i++;
		}
		Arrays.sort(li);
		
		System.out.println(li[0] + " " + li[n-1]);		
		
	}
}
