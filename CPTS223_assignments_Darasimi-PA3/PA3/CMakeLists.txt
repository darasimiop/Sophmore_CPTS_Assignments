cmake_minimum_required(VERSION 3.16)
project(PA3)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -Wall")
set(CMAKE_BUILD_TYPE Debug)

add_executable(PA3 main.cpp ChainingHash.hpp Hash.hpp ProbingHash.hpp)
