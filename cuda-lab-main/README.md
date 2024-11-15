# AOOP CUDA LAB 4 & LAB 5
This CUDA lab is only for AOOP course.
Click this prerequisite installation guide [link](https://docs.google.com/document/d/14m-kjJbjojLJl_LSmwoj7bR52nFT2PK0UD0UJU3S2Jk/edit?usp=sharing) if you have not installed the nvidia docker.

Clone the repo
```bash
git clone git@github.com:zhuchi76/cuda-lab.git
```

Enter the directory
```bash
cd cuda-lab
```

## LAB 4
Run the docker
```bash
source gpu_run.sh
```

### LAB 4-1
Run directly
```bash
g++ lab4-1_cpu.cpp -o ./lab4-1_cpu.out
./lab4-1_cpu.out
```

```
Length of vector: 67108864
Time elapsed for vector addition: 151 ms
Vector addition completed successfully!
```

Run directly
```bash
nvcc lab4-1.cu -o lab4-1.out
./lab4-1.out
```

```
Length of vector: 67108864
CUDA kernel launch with 262144 blocks of 256 threads
Time elapsed for memory allocation: 73 ms
Time elapsed for data transfer from host to device: 33 ms
Time elapsed for kernel execution: 0 ms
Time elapsed for data transfer from device to host: 65 ms
Total time elapsed: 172 ms
Vector addition completed successfully!
```

### LAB 4-2
Make sure fill in your code, then run
```bash
cmake -S ./lab4-2 -B ./build
cmake --build build/
./build/MatrixMultiplication
```

```
Matrix dimensions: 2048 x 2048 and 2048 x 2048
Allocating matrices...
Start matrix multiplication...
Matrix multiplication on CPU completed in 16.509 seconds
Matrix multiplication on GPU completed in 0.0857489 seconds
Matrix multiplication completed successfully!
```

## LAB 5
Run the docker
```bash
source gpu_run.sh
```

Open the jupyter notebook
```bash
source jupyter_notebook.sh
```

Make sure fill-in your code, then run every cell of notebook "lab5-1.ipynb"

## Reference
<https://developer.nvidia.com/blog/even-easier-introduction-cuda/>
<https://edoras.sdsu.edu/~mthomas/docs/cuda/cuda_by_example.book.pdf>