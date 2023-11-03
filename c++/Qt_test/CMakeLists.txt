cmake_minimum_required(VERSION 3.25)
project(Qt_test)

set(CMAKE_CXX_STANDARD 17)

find_package(Qt5 COMPONENTS Core Gui Widgets SerialPort REQUIRED)

include_directories(${Qt5_INCLUDE_DIRS})

# 添加Qt的配置文件
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(
        SOURCES
        main.cpp
)

add_executable(Qt_test ${SOURCES})
target_link_libraries(Qt_test Qt5::Core Qt5::Gui Qt5::Widgets Qt5::SerialPort)
