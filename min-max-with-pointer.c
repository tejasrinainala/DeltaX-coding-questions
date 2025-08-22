#include <stdio.h>

int main() {
    int a[5];
    int *s, max;

    // input
    for (int i = 0; i < 5; i++) {
        scanf("%d", &a[i]);
    }
    
    s = &a[0];
    max = *s;
    
    for (int i = 1; i < 5; i++) {
        if (*(s + i) > max) {
            max = *(s + i);
        }
    }

    printf("Max element is %d", max);
    return 0;
}
