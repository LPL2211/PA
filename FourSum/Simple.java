// Requirement: Find in a given array 4 numbers which sum up to 0
// Problem: Test with input Bfalse.txt, get wrong outcome. Expected outcome should be False but mine is True. 
// Is that because Bfalse.txt contains duplicates(2 times of number 4)?
// Can you implement Binary Search in Java for this assignment:?

import java.util.Scanner;
import java.util.Arrays;

public class FourSum {

    // print distinct 4-tuples (i, j, k, l) such that a[i] + a[j] + a[k] + a[l] = 0

    public static void main(String[] args) { // Provided by teacher, don't change
        Scanner S = new Scanner(System.in); // Provided by teacher, don't change
        int n = Integer.parseInt(S.nextLine()); // Provided by teacher, don't change
        long[] a = new long[n]; // Provided by teacher, don't change

        if ( a.length < 4) {
            System.out.println("False");
        } else {
            Arrays.sort(a);
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    for (int k = j + 1; k < n; k++) {
                        for (int l = k + 1; l < n; l++) {
                            long sum = a[i] + a[j] + a[k] + a[l];
                            if (sum == 0) {
                                System.err.println(i + " " + j + " " + k + " " + l); // Provided by teacher, don't change
                                System.out.println("True"); // Provided by teacher, don't change
                                System.exit(0); // Provided by teacher, don't change
                            }
                        }
                    }
                }
            }
            System.out.println("False");
        }
    }
}
