CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0)

PROJECT(adventofcode-04)

# copy binary to same path as code/cmakelists file
SET(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

ADD_EXECUTABLE(adventofcode-04 main.cpp adventofcode-04.cpp adventofcode-04.h)

TARGET_LINK_LIBRARIES(adventofcode-04 ${CMAKE_CURRENT_SOURCE_DIR}/lib.a)
