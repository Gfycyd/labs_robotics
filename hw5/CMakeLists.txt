cmake_minimum_required(VERSION 2.8.3)
project(fanuc)
find_package(catkin REQUIRED)

catkin_package(
)

include_directories(
)
 install(PROGRAMS
   scripts/main.py
 #  scripts/trajectory_planning.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

 install(FILES
    launch/display.launch
    launch/main.launch
     launch/trajectory_move.launch
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

