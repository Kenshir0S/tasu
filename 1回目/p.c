#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *reverse(char *s) {
    int len = strlen(s);
    char *re_s = (char *)malloc(sizeof(char) * len);
    int i = 0;
    while (len != 0) {
        *(re_s + i) = *(s + (len - 1));
        len--;
        i++;
    }

    return re_s;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        return -1;
    }
    char *x = argv[1];
    int len = strlen(x);
    char *re_x = NULL;
    printf("%s\n", x);

    re_x = reverse(x);
    printf("%s\n", re_x);

    free(re_x);
    return 0;
}