#include <iostream>
using namespace std;

void insertionSort(int array[], int n) {

  int i, key, j;
  for (i = 1; i < n; i++) {
    key = array[i];
    j = i - 1;
    while (j >= 0 && array[j] > key) {
      array[j + 1] = array[j];
      j = j - 1;
    }
    array[j + 1] = key;
  }
}

void printArray(int array[], int n) {
  int i;
  for (i = 0; i < n; i++)
    cout << array[i] << " ";
  cout << endl;
}

int main() {
  int array[] = {4, 1, 4, 6, 2, 4, 7, 8, 3, 4, 2, 2, 6, 7, 9, 4};
  int N = sizeof(array) / sizeof(array[0]);

  insertionSort(array, N);
  printArray(array, N);

  return 0;
}