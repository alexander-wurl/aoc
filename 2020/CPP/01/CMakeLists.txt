CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0)

PROJECT(adventofcode-01)

# copy binary to same path as code/cmakelists file
SET(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

ADD_EXECUTABLE(adventofcode-01 adventofcode-01.cpp)
