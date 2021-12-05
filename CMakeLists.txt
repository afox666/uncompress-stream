cmake_minimum_required(VERSION 3.3)
project(uncompress)

set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_STANDARD 11)
include_directories(.)

find_package(ZLIB)

add_executable(uncompress uncompress.cpp)
target_link_libraries(uncompress ZLIB::ZLIB)
