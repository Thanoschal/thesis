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
CMAKE_SOURCE_DIR = /home/pi/Desktop/thesis/ros_workspace/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/Desktop/thesis/ros_workspace/build

# Include any dependencies generated for this target.
include video_stream_opencv/CMakeFiles/video_stream_opencv.dir/depend.make

# Include the progress variables for this target.
include video_stream_opencv/CMakeFiles/video_stream_opencv.dir/progress.make

# Include the compile flags for this target's objects.
include video_stream_opencv/CMakeFiles/video_stream_opencv.dir/flags.make

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/flags.make
video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o: /home/pi/Desktop/thesis/ros_workspace/src/video_stream_opencv/src/video_stream.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/Desktop/thesis/ros_workspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o"
	cd /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o -c /home/pi/Desktop/thesis/ros_workspace/src/video_stream_opencv/src/video_stream.cpp

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.i"
	cd /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/Desktop/thesis/ros_workspace/src/video_stream_opencv/src/video_stream.cpp > CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.i

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.s"
	cd /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/Desktop/thesis/ros_workspace/src/video_stream_opencv/src/video_stream.cpp -o CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.s

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.requires:

.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.requires

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.provides: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.requires
	$(MAKE) -f video_stream_opencv/CMakeFiles/video_stream_opencv.dir/build.make video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.provides.build
.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.provides

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.provides.build: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o


# Object files for target video_stream_opencv
video_stream_opencv_OBJECTS = \
"CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o"

# External object files for target video_stream_opencv
video_stream_opencv_EXTERNAL_OBJECTS =

/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/build.make
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libcv_bridge.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_core3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgproc3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgcodecs3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libimage_transport.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libmessage_filters.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libcamera_info_manager.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libcamera_calibration_parsers.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libnodeletlib.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libuuid.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libbondcpp.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libtinyxml2.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libclass_loader.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/libPocoFoundation.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libdl.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libroslib.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/librospack.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libpython2.7.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_program_options.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libtinyxml.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libroscpp.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_signals.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/librosconsole.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/liblog4cxx.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_regex.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libdynamic_reconfigure_config_init_mutex.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/librostime.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/libcpp_common.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_system.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_thread.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_chrono.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_date_time.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libboost_atomic.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libpthread.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /usr/lib/arm-linux-gnueabihf/libconsole_bridge.so
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stitching3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_superres3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videostab3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_aruco3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bgsegm3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_bioinspired3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ccalib3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_cvv3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dpm3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_face3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_fuzzy3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_hdf3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_img_hash3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_line_descriptor3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_optflow3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_reg3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_rgbd3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_saliency3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_stereo3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_structured_light3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_surface_matching3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_tracking3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xfeatures2d3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ximgproc3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xobjdetect3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_xphoto3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_shape3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_photo3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_datasets3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_plot3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_text3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_dnn3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_ml3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_video3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_calib3d3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_features2d3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_highgui3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_videoio3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_viz3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_phase_unwrapping3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_flann3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgcodecs3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_objdetect3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_imgproc3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: /opt/ros/kinetic/lib/arm-linux-gnueabihf/libopencv_core3.so.3.3.1
/home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/Desktop/thesis/ros_workspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library /home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so"
	cd /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/video_stream_opencv.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
video_stream_opencv/CMakeFiles/video_stream_opencv.dir/build: /home/pi/Desktop/thesis/ros_workspace/devel/lib/libvideo_stream_opencv.so

.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/build

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/requires: video_stream_opencv/CMakeFiles/video_stream_opencv.dir/src/video_stream.cpp.o.requires

.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/requires

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/clean:
	cd /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv && $(CMAKE_COMMAND) -P CMakeFiles/video_stream_opencv.dir/cmake_clean.cmake
.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/clean

video_stream_opencv/CMakeFiles/video_stream_opencv.dir/depend:
	cd /home/pi/Desktop/thesis/ros_workspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/Desktop/thesis/ros_workspace/src /home/pi/Desktop/thesis/ros_workspace/src/video_stream_opencv /home/pi/Desktop/thesis/ros_workspace/build /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv /home/pi/Desktop/thesis/ros_workspace/build/video_stream_opencv/CMakeFiles/video_stream_opencv.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : video_stream_opencv/CMakeFiles/video_stream_opencv.dir/depend

