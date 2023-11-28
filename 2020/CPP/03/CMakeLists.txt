CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0)

PROJECT(adventofcode-03)

# copy binary to same path as code/cmakelists file
SET(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

ADD_EXECUTABLE(adventofcode-03 main.cpp adventofcode-03.cpp adventofcode-03.h)

TARGET_LINK_LIBRARIES(adventofcode-03)
