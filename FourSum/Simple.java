import java.util.Scanner;
import java.util.Arrays;
 
public class FourSum {
 
    // print distinct 4-tuples (i, j, k, l) such that a[i] + a[j] + a[k] + a[l] = 0
 
    public static void main(String[] args) {
        Scanner S = new Scanner(System.in);
        int n = Integer.parseInt(S.nextLine());
        long[] a = new long[n];
 
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
                                System.err.println(i + " " + j + " " + k + " " + l);
                                System.out.println("True");
                                System.exit(0);
                            } else if (sum > 0) {
                                System.out.println("False");
 
                            } else {
                                System.out.println("False");
 
 
                            }
                        }
                    }
                }
            }
        }
    }
}
