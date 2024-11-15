#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

// Define execution parameters
const unsigned int N = 1 << 26;

const int threadsPerBlock = 256; // Number of threads per block
const int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock; // Number of blocks per grid

__global__ void VectorAdd(const float *A, const float *B, float *C, int N) {
    // Calculate the index for the current thread
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < N) {
        C[i] = A[i] + B[i]; // Perform vector addition
    }
}

int main() {
    size_t size = N * sizeof(float);
    cout << "Length of vector: " << N << endl;

    // Allocate memory for host vectors
    float *h_A = (float *)malloc(size);
    float *h_B = (float *)malloc(size);
    float *h_C = (float *)malloc(size);

    // Initialize host vectors
    for (int i = 0; i < N; i++) {
        h_A[i] = i / 1000.0f;
        h_B[i] = i * 2 / 1000.0f;
    }

    float *d_A, *d_B, *d_C;

    // Allocate memory on the device
    auto malloc_start = high_resolution_clock::now();
    // cudaMalloc((void **)&d_A, size);
    cudaMalloc(&d_A, size);
    cudaMalloc(&d_B, size);
    cudaMalloc(&d_C, size);
    auto malloc_end = high_resolution_clock::now();

    // Copy data from host to device
    auto copy_htod_start = high_resolution_clock::now();
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
    auto copy_htod_end = high_resolution_clock::now();

    // Launch the CUDA kernel for vector addition
    cout << "CUDA kernel launch with " << blocksPerGrid << " blocks of " << threadsPerBlock << " threads" << endl;
    auto add_start = high_resolution_clock::now();
    VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
    cudaDeviceSynchronize(); // Wait for the kernel to complete
    auto add_end = high_resolution_clock::now();

    // Copy the result from device to host
    auto copy_dtoh_start = high_resolution_clock::now();
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
    auto copy_dtoh_end = high_resolution_clock::now();

    // Print the elapsed time for various operations
    cout << "Time elapsed for memory allocation: " 
         << duration_cast<milliseconds>(malloc_end - malloc_start).count() << " ms" << endl;

    cout << "Time elapsed for data transfer from host to device: " 
         << duration_cast<milliseconds>(copy_htod_end - copy_htod_start).count() << " ms" << endl;

    cout << "Time elapsed for kernel execution: " 
         << duration_cast<milliseconds>(add_end - add_start).count() << " ms" << endl;

    cout << "Time elapsed for data transfer from device to host: " 
         << duration_cast<milliseconds>(copy_dtoh_end - copy_dtoh_start).count() << " ms" << endl;

    cout << "Total time elapsed: " 
         << duration_cast<milliseconds>(copy_dtoh_end - malloc_start).count() << " ms" << endl;

    // Verify the result
    for (int i = 0; i < N; ++i) {
        if (h_C[i] != h_A[i] + h_B[i]) {
            cerr << "Error at index " << i << endl;
            exit(1);
        }
    }

    // Free allocated memory
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    free(h_A);
    free(h_B);
    free(h_C);

    cout << "Vector addition completed successfully!" << endl;
    return 0;
}
