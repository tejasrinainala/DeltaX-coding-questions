#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // first read size
    
    int a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]); // input elements
    }
    int max1 = a[0], max2 = a[1];
  for (int i = 1; i < n; i++) {
        if (a[i] > max1) {
            max2 = max1;
            max1 = a[i];
        } else if (a[i] > max2 && a[i] != max1) {
            max2 = a[i];
        }
    }


    printf("%d",max2);
    return 0;
}

// input & output:
// 8
// 12 3 4 5 6 10 22 3
// 12
