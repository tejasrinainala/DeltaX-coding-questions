#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // first read size
    
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]); // input elements
    }

    int left = 0, right = n - 1, temp;

    while (left < right) {
        if (a[left] < 0 && a[right] < 0) {
            left++; // both negative, move left
        } 
        else if (a[left] > 0 && a[right] < 0) {
            // swap
            temp = a[left];
            a[left] = a[right];
            a[right] = temp;
            left++;
            right--;
        } 
        else if (a[left] > 0 && a[right] > 0) {
            right--; // both positive, move right
        } 
        else { 
            // a[left] < 0 && a[right] > 0
            left++;
            right--;
        }
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}


// input & output
// 8
// -1 2 -3 4 5 -6 7 -8
// -1 -8 -3 -6 5 4 7 2 

