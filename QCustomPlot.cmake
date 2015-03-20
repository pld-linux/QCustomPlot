project(QCustomPlot)
cmake_minimum_required(VERSION 2.8.0)

find_package ( Qt4 REQUIRED QtCore QtGui)
include ( ${QT_USE_FILE} )

set (QCustomPlot_SRCS
  qcustomplot.cpp
)

set (QCustomPlot_HDRS
  qcustomplot.h
)

set (QCustomPlot_MOCS
  ${QCustomPlot_HDRS}
)

QT4_WRAP_CPP(MOCS ${QCustomPlot_MOCS})

add_library(qcustomplot SHARED ${QCustomPlot_SRCS} ${MOCS})
set_target_properties(qcustomplot PROPERTIES VERSION 1.0.0 SOVERSION 1)
target_link_libraries(qcustomplot ${QT_LIBRARIES})
install(TARGETS qcustomplot LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
install(FILES ${QCustomPlot_HDRS} DESTINATION include)
