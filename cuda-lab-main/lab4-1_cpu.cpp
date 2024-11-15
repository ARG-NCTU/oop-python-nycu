#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace chrono;

// Define the size of the vector using a power of 2
const unsigned int N = 1 << 26; // 2^26 elements

// Function to perform vector addition
void VectorAdd(const vector<float>& A, 
               const vector<float>& B, 
               vector<float>& C, int N) {
    for (int i = 0; i < N; ++i) {
        C[i] = A[i] + B[i];
    }
}

int main() {
    size_t size = N * sizeof(float); // Calculate the size of the data in bytes
    cout << "Length of vector: " << N << endl;

    vector<float> A(N), B(N), C(N); // Declare vectors A, B, and C with N elements

    // Initialize vectors A and B with some values
    for (int i = 0; i < N; i++) {
        A[i] = i / 1000.0f;
        B[i] = i * 2 / 1000.0f;
    }

    // Perform vector addition and measure the time taken
    auto add_start = high_resolution_clock::now(); // Start the timer
    VectorAdd(A, B, C, N); // Add vectors A and B, store the result in C
    auto add_end = high_resolution_clock::now(); // Stop the timer

    // Output the time taken for the vector addition
    cout << "Time elapsed for vector addition: " 
         << duration_cast<milliseconds>(add_end - add_start).count() << " ms" << endl;

    // Verify the result of the addition
    for (int i = 0; i < N; ++i) {
        // Exit the program if there is an error
        if (C[i] != A[i] + B[i]) { 
            cerr << "Error at index " << i << endl;
            exit(1); 
        }
    }

    cout << "Vector addition completed successfully!" << endl;
    return 0;
}
