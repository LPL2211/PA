// Implement Binary Search for finding 4 numbers in an array which sum up to 0
// Inspired codes here: 
// https://www.programcreek.com/2013/02/leetcode-4sum-java/
// https://stackoverflow.com/questions/11216582/4sum-implementation-in-java-from-leetcode
// https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/
// https://www.geeksforgeeks.org/find-four-numbers-with-sum-equal-to-given-sum/

import java.util.Scanner;
import java.util.Arrays;

public class FourSum {

    public static void main(String[] args) {
        Scanner S = new Scanner(System.in);
        int n = Integer.parseInt(S.nextLine());
        long[] a = new long[n];
        int desired_sum = 0;

        long start = System.nanoTime();

        for (int i = 0; i < n; i++)
        {
            a[i] = S.nextLong();
        }

        if ( a.length < 4) {
            System.out.println("False");
        } else {
            Arrays.sort(a);
            for (int i = 0; i < n-3; i++) {
                for (int j = i + 1; j < n-2; j++) {
                    for (int k = j + 1; k < n-1; k++) {
                        long to_find = desired_sum - a[i] - a[j] - a[k];
                        if (binarySearch(a, k+1, n-1, to_find) != -1) {
                        	System.err.println(a[i] + " " + a[j] + " " + a[k] + " " + to_find);
                            System.out.println("True");
                            long time = System.nanoTime() - start;
                            System.out.println(time);
                            System.exit(0);
                        }
                    }
                }
            }
            System.out.println("False");
            long time = System.nanoTime() - start;
            System.out.println(time);
        }
    }

    static int binarySearch(long arr[], int l, int r, long x)
    {
        if (r>=l)
        {
            int mid = l + (r - l)/2;

            if (arr[mid] == x)
               return mid;

            if (arr[mid] > x)
               return binarySearch(arr, l, mid-1, x);

            return binarySearch(arr, mid+1, r, x);
        }

        return -1;
    }
}
