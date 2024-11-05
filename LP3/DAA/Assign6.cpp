#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

// Utility function to print an array
void printArray(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

// Partition function for deterministic quicksort (last element as pivot)
int deterministicPartition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Deterministic quicksort using last element as pivot
void deterministicQuickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = deterministicPartition(arr, low, high);
        deterministicQuickSort(arr, low, pi - 1);
        deterministicQuickSort(arr, pi + 1, high);
    }
}

// Partition function for randomized quicksort (random pivot selection)
int randomizedPartition(vector<int>& arr, int low, int high) {
    int randomIndex = low + rand() % (high - low + 1);
    swap(arr[randomIndex], arr[high]);  // Move random pivot to end
    return deterministicPartition(arr, low, high);  // Partition as usual
}

// Randomized quicksort using random pivot selection
void randomizedQuickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = randomizedPartition(arr, low, high);
        randomizedQuickSort(arr, low, pi - 1);
        randomizedQuickSort(arr, pi + 1, high);
    }
}

int main() {
    srand(time(0));  // Seed for random number generation

    // Generate an array of random integers
    vector<int> arr;
    int n = 10000;  // Adjust n for larger or smaller tests
    for (int i = 0; i < n; i++) {
        arr.push_back(rand() % 10000);
    }

    // Test deterministic quicksort
    vector<int> arr1 = arr;
    auto start = high_resolution_clock::now();
    deterministicQuickSort(arr1, 0, n - 1);
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Deterministic Quick Sort Time: " << duration.count() << " ms" << endl;

    // Test randomized quicksort
    vector<int> arr2 = arr;
    start = high_resolution_clock::now();
    randomizedQuickSort(arr2, 0, n - 1);
    end = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(end - start);
    cout << "Randomized Quick Sort Time: " << duration.count() << " ms" << endl;

    return 0;
}
