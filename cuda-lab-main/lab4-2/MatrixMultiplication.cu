#include <iostream>
#include <chrono>
#include <cmath>

using namespace std;
using namespace chrono;

#define GetIndex(mtx, row, col) ((row) * (mtx).width + (col))
#define BLOCK_SIZE 16

typedef struct {
    int width;
    int height;
    float* elements;
} Matrix;

// Implement matrix multiplication on the CPU
bool MatMulCPU(const Matrix& A, const Matrix& B, Matrix& C) {
    if (A.width != B.height) {
        return false;
    }

    delete[] C.elements; // Free existing memory
    C.height = A.height;
    C.width = B.width;
    C.elements = new float[C.width * C.height]();

    // Matrix multiplication
    for (int i = 0; i < A.height; ++i) {
        for (int j = 0; j < B.width; ++j) {
            float result = 0;
            for (int e = 0; e < A.width; e++) {
                result += A.elements[GetIndex(A, i, e)] * B.elements[GetIndex(B, e, j)];
            }
            C.elements[GetIndex(C, i, j)] = result;
        }
    }

    return true;
}

// Matrix multiplication kernel
_global_ void MatMulKernel(Matrix A, Matrix B, Matrix C) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < C.height && col < C.width) {
        float result = 0;
        for (int e = 0; e < A.width; e++) {
            result += A.elements[GetIndex(A, row, e)] * B.elements[GetIndex(B, e, col)];
        }
        C.elements[GetIndex(C, row, col)] = result;
    }
}

// Matrix multiplication - Host code
bool MatMulGPU(const Matrix& A, const Matrix& B, Matrix& C) {
    if (A.width != B.height) {
        return false;
    }

    delete[] C.elements; // Free existing memory
    C.height = A.height;
    C.width = B.width;
    C.elements = new float[C.width * C.height];

    Matrix d_A, d_B, d_C;
    d_A.width = A.width; d_A.height = A.height;
    d_B.width = B.width; d_B.height = B.height;
    d_C.width = C.width; d_C.height = C.height;

    size_t size_A = A.width * A.height * sizeof(float);
    size_t size_B = B.width * B.height * sizeof(float);
    size_t size_C = C.width * C.height * sizeof(float);

    cudaMalloc(&d_A.elements, size_A);
    cudaMemcpy(d_A.elements, A.elements, size_A, cudaMemcpyHostToDevice);
    
    cudaMalloc(&d_B.elements, size_B);
    cudaMemcpy(d_B.elements, B.elements, size_B, cudaMemcpyHostToDevice);
    
    cudaMalloc(&d_C.elements, size_C);

    dim3 dimBlock(BLOCK_SIZE, BLOCK_SIZE);
    dim3 dimGrid((B.width + BLOCK_SIZE - 1) / BLOCK_SIZE, 
                 (A.height + BLOCK_SIZE - 1) / BLOCK_SIZE);

    MatMulKernel<<<dimGrid, dimBlock>>>(d_A, d_B, d_C);
    cudaDeviceSynchronize(); // Wait for the kernel to finish

    cudaMemcpy(C.elements, d_C.elements, size_C, cudaMemcpyDeviceToHost);

    cudaFree(d_A.elements);
    cudaFree(d_B.elements);
    cudaFree(d_C.elements);

    return true;
}

int main() {
    const int size = 1 << 11;

    const int N = size; 
    const int M = size;
    const int P = size;

    cout << "Matrix dimensions: " << N << " x " << M << " and " << M << " x " << P << endl;
    cout << "Allocating matrices..." << endl;

    Matrix A, B, result_CPU, result_GPU;
    A.width = N; A.height = M; A.elements = new float[N * M]();
    B.width = M; B.height = P; B.elements = new float[M * P]();

    for (int i = 0; i < N * M; ++i) {
        A.elements[i] = i % 100 / 1000.0f;
    }
    for (int i = 0; i < M * P; ++i) {
        B.elements[i] = i % 200 / 1000.0f;
    }

    cout << "Start matrix multiplication..." << endl;

    auto start_cpu = high_resolution_clock::now();
    MatMulCPU(A, B, result_CPU);
    auto end_cpu = high_resolution_clock::now();
    duration<float> duration_cpu = end_cpu - start_cpu;
    cout << "Matrix multiplication on CPU completed in " << duration_cpu.count() << " seconds" << endl;

    auto start_gpu = high_resolution_clock::now();
    MatMulGPU(A, B, result_GPU);
    auto end_gpu = high_resolution_clock::now();
    duration<float> duration_gpu = end_gpu - start_gpu;
    cout << "Matrix multiplication on GPU completed in " << duration_gpu.count() << " seconds" << endl;

    // Verify the result
    bool success = true;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            if (abs(result_CPU.elements[GetIndex(result_CPU, i, j)] - result_GPU.elements[GetIndex(result_GPU, i, j)]) > 1e-5) {
                cout << "Results mismatch at index (" << i << ", " << j << "): " 
                     << result_CPU.elements[GetIndex(result_CPU, i, j)] << " != " << result_GPU.elements[GetIndex(result_GPU, i, j)] << endl;
                success = false;
            }
        }
    }

    if (success) {
        cout << "Matrix multiplication completed successfully!" << endl;
    } else {
        cout << "Matrix multiplication completed with errors!" << endl;
    }

    // Free allocated memory
    delete[] A.elements;
    delete[] B.elements;
    delete[] result_CPU.elements;
    delete[] result_GPU.elements;

    return 0;
}
