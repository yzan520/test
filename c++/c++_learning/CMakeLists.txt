cmake_minimum_required(VERSION 3.25)
project(c___learning)

set(CMAKE_CXX_STANDARD 17)


find_package(fmt REQUIRED)

add_executable(c___learning main.cpp)
target_link_libraries(c___learning fmt::fmt)
