#include <stdio.h>

int main(void) {
  char name[50];
  printf("What's your name?\n");
  scanf("%49s", name);
  printf("Hello, %s\n", name);
  return 0;
}