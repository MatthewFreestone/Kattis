/*
Rating: ~ 2.8 / 10
Link: https://open.kattis.com/problems/equalsumseasy
*/

#include <stdio.h>
#include <stdlib.h>

typedef long long ll;
int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

int binary_search(const int array[], int a_len, int target) {

  int low = 0;
  int high = 1 << a_len;
  while (high > low) {
    int middle = (high + low) / 2;
    int res;
    int level = 0;
    while (middle > 0) {
      if (middle & 1)
        res += array[level];
      level++;
      middle >>= 1;
    }
    if (res == target) {
      printf("%d", (high + low) / 2);
      return (high + low) / 2;
    }

    if (res > target) {
      // we're over the target; go down.
      high = middle - 1;
    } else {
      // second set is too big, go up.
      low = middle;
    }
  }
  return -1;
}

char search(const int sorted_array[], int a_len, int first_set_bitmask) {
  int n = first_set_bitmask;
  int first_sum = 0;
  int second_opts[20], so_i = 0;
  int i = 0;
  while (i < a_len) {
    if (n & 1) {
      first_sum += sorted_array[i];
    } else {
      second_opts[so_i] = sorted_array[i];
      so_i++;
    }
    n >>= 1;
    i++;
  }
  int res_bitmask = binary_search(second_opts, so_i, first_sum);
  if (res_bitmask == -1)
    return 0;
  return 1;
}

int main() {
  int cases;
  scanf_s("%d", &cases);
  int i = 0;
  while (i < cases) {
    i++;
    printf("Case #%d\n", i);
    int n;
    scanf_s("%d", &n);
    // int *choices = malloc(sizeof(int[n]));
    int choices[20];

    int i = 0;
    while (i < n) {
      scanf_s("%d", &choices[i]);
      i++;
    }
    qsort(choices, i + 1, sizeof(int), compare);

    // with our sorted set, we want to first select a subset for the first
    int mask = 1 << n;
    while (mask > 0) {
      char res = search(choices, n, mask);
      if (res) {
        printf("Possible.");
      }
      mask++;
    }
    printf("Impossible.\n");
  }

  return 0;
}
