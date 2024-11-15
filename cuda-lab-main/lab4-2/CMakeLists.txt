# Specify the minimum required version of CMake
cmake_minimum_required(VERSION 3.20)

# Project name and languages used (C++ and CUDA)
project(MatrixMultiplication LANGUAGES CXX CUDA)

# Export compile commands for editor support
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Set the C++ standard to C++14
set(CMAKE_CXX_STANDARD 14)  # Specify the C++ standard version
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # Enforce the specified C++ standard version

# Set the CUDA standard to CUDA 14
set(CMAKE_CUDA_STANDARD 14)  # Specify the CUDA standard version
set(CMAKE_CUDA_STANDARD_REQUIRED ON)  # Enforce the specified CUDA standard version

# Set CUDA compilation flags
set(CMAKE_CUDA_FLAGS "${CMAKE_CUDA_FLAGS} -O3 --ptxas-options=-v")
# Uncomment the following line for debugging
# set(CMAKE_CUDA_FLAGS_DEBUG="-G -g -O0")

# Find CUDA package
find_package(CUDA REQUIRED)
if (CUDA_FOUND)
    message(STATUS "CUDA_INCLUDE_DIRS: ${CUDA_INCLUDE_DIRS}")  # Print CUDA include directories
    message(STATUS "CUDA_LIBRARIES: ${CUDA_LIBRARIES}")  # Print CUDA libraries
    message(STATUS "CUDA_LIBRARY_DIRS: ${CUDA_LIBRARY_DIRS}")  # Print CUDA library directories
else()
    message(FATAL_ERROR "Cannot find CUDA")  # Fatal error if CUDA is not found
endif()

# Add the executable target
add_executable(MatrixMultiplication MatrixMultiplication.cu)

# Include CUDA directories for the target
target_include_directories(MatrixMultiplication PRIVATE ${CUDA_INCLUDE_DIRS})

# Link CUDA libraries to the target
target_link_libraries(MatrixMultiplication PRIVATE ${CUDA_LIBRARIES})
