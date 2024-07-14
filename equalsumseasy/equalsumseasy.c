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
  int high = (1 << a_len) - 1;
  while (high > low) {
    int middle = (high + low) / 2;
    // printf("\t h:%d, l:%d, m: %d\n", high, low, middle);
    int res = 0;
    int level = 0;
    int while_middle = middle;
    while (while_middle > 0) {
      if (while_middle & 1)
        res += array[level];
      level++;
      while_middle >>= 1;
    }
    if (res == target) {
      return middle;
    }

    if (res > target) {
      // we're over the target; go down.
      // printf("decrease high");
      high = middle - 1;
    } else {
      // second set is too big, go up.
      // printf("increase low.");
      low = middle + 1;
    }
  }
  return -1;
}

struct res_t {
  int first_size;
  int second_size;
};

struct res_t search(const int sorted_array[], int a_len, int first_set_bitmask,
                    int res_nums[2][20]) {
  int n = first_set_bitmask;
  int first_sum = 0;
  int fs_i = 0;
  int second_opts[20], so_i = 0;
  int i = 0;
  while (i < a_len) {
    if (n & 1) {
      first_sum += sorted_array[i];
      res_nums[0][fs_i] = sorted_array[i];
      fs_i++;
    } else {
      second_opts[so_i] = sorted_array[i];
      so_i++;
    }
    n >>= 1;
    i++;
  }
  int res_bitmask = binary_search(second_opts, so_i, first_sum);
  // ths bitmask has the asnswer for the second set.
  if (res_bitmask == -1) {
    struct res_t res = {-1, -1};
    return res;
  }
  // printf("Masks: %08x, %08x\n", first_set_bitmask, res_bitmask);
  int r_i = 0;
  i = 0;
  while (res_bitmask > 0) {
    if (res_bitmask & 1) {
      res_nums[1][r_i] = second_opts[i];
      r_i++;
    }
    i++;
    res_bitmask >>= 1;
  }
  // printf("%d in first, %d in second\n", fs_i, r_i);
  struct res_t res = {fs_i, r_i};
  return res;
}

int main() {
  int cases;
  scanf("%d", &cases);
  int i = 0;
  while (i < cases) {
    i++;
    printf("Case #%d:\n", i);
    int n;
    scanf("%d", &n);
    int choices[20];

    int i = 0;
    while (i < n) {
      scanf("%d", &choices[i]);
      i++;
    }
    qsort(choices, n, sizeof(int), compare);
    // for (int i = 0; i < n; i++)
    //   printf("%d ", choices[i]);
    // printf("\n");
    // with our sorted set, we want to first select a subset for the first
    const int max_mask = (1 << n);
    int res_nums[2][20];
    int mask;
    for (mask = 1; mask < max_mask; mask++) {
      struct res_t res = search(choices, n, mask, res_nums);
      if (res.first_size != -1) {
        // first list:
        int i = 0;
        // printf("first: %d\t", res);
        while (i < res.first_size) {
          printf("%d ", res_nums[0][i]);
          i++;
        }
        printf("\n");
        i = 0;
        // printf("second: %d\n", n - res);
        while (i < res.second_size) {
          printf("%d ", res_nums[1][i]);
          i++;
        }
        printf("\n");

        // printf("Possible: %04x, %04x\n", mask, res);
        break;
      }
    }
    if (mask == max_mask)
      printf("Impossible\n");
  }

  return 0;
}
