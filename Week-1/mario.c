#include <stdio.h>
#include <cs50.h>

int main(void) {
  int height;

  do {
    height = get_int("How high? (1-8)\n");
  } while (height < 1 || height > 8);

  for (int i = 1; i <= height; i++) {
    for (int j = height; j > i; j--) {
      printf(" "); // Spaces
    }
    for (int k = 1; k <= i; k++) {
      printf("#"); // Hashtags
    }
    printf("\n");
  }
}
