#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &array, int left, int right) {
  int pivot_value = array[right];
  int i = left - 1;
  int j;
  for (j = left; j < right; j++) {
    if (array[j] <= pivot_value) {
      i = i + 1;
      swap(array[i], array[j]);
    }
  }
  swap(array[i + 1], array[right]);
  return i + 1;
}

void quickSort(vector<int> &array, int left, int right) {
  if (left < right) {
    int pivot_index = partition(array, left, right);
    quickSort(array, left, pivot_index - 1);
    quickSort(array, pivot_index + 1, right);
  }
}

void printVector(const vector<int> &arr) {
  for (int val : arr) {
    cout << val << " ";
  }
  cout << endl;
}

int main() {
  vector<int> array = {4, 1, 4, 6, 2, 4, 7, 8, 3, 4, 2, 2, 6, 7, 9, 4};
  int left = 0;
  int right = array.size() - 1;

  quickSort(array, left, right);
  printVector(array);

  return 0;
}