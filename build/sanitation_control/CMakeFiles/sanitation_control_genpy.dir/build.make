# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/Ubiquity-Pi/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/Ubiquity-Pi/build

# Utility rule file for sanitation_control_genpy.

# Include the progress variables for this target.
include sanitation_control/CMakeFiles/sanitation_control_genpy.dir/progress.make

sanitation_control_genpy: sanitation_control/CMakeFiles/sanitation_control_genpy.dir/build.make

.PHONY : sanitation_control_genpy

# Rule to build all files generated by this target.
sanitation_control/CMakeFiles/sanitation_control_genpy.dir/build: sanitation_control_genpy

.PHONY : sanitation_control/CMakeFiles/sanitation_control_genpy.dir/build

sanitation_control/CMakeFiles/sanitation_control_genpy.dir/clean:
	cd /home/ubuntu/Ubiquity-Pi/build/sanitation_control && $(CMAKE_COMMAND) -P CMakeFiles/sanitation_control_genpy.dir/cmake_clean.cmake
.PHONY : sanitation_control/CMakeFiles/sanitation_control_genpy.dir/clean

sanitation_control/CMakeFiles/sanitation_control_genpy.dir/depend:
	cd /home/ubuntu/Ubiquity-Pi/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/Ubiquity-Pi/src /home/ubuntu/Ubiquity-Pi/src/sanitation_control /home/ubuntu/Ubiquity-Pi/build /home/ubuntu/Ubiquity-Pi/build/sanitation_control /home/ubuntu/Ubiquity-Pi/build/sanitation_control/CMakeFiles/sanitation_control_genpy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sanitation_control/CMakeFiles/sanitation_control_genpy.dir/depend

