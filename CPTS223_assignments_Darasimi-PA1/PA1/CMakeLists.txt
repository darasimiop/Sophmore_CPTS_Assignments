cmake_minimum_required(VERSION 3.16)
project(PA1)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
set(CMAKE_BUILD_TYPE Debug)

# Use double quotes to enclose file paths
configure_file("/mnt/c/Users/daras/OneDrive/Desktop/CPTS 223/PA1/commands.csv" "/mnt/c/Users/daras/OneDrive/Desktop/CPTS 223/PA1/build/commands.csv" COPYONLY)

add_executable(PA1 main.cpp linked_list.hpp PA1.hpp node.hpp data.hpp commands.csv)
