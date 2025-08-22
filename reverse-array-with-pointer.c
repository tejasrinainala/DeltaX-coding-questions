#include <stdio.h>

int main() {
    int a[5];
    int *s, *e, temp;

    // input
    for (int i = 0; i < 5; i++) {
        scanf("%d", &a[i]);
    }

    // pointers at start and end
    s = &a[0];
    e = &a[4];

    // reverse
    while (s < e) {
        temp = *s;
        *s = *e;
        *e = temp;
        s++;
        e--;
    }

    // output
    for (int i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }

    return 0;
}
