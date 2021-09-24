file(REMOVE_RECURSE
  "001.exe"
  "001.exe.manifest"
  "001.pdb"
  "CMakeFiles/001.dir/hello_world.cpp.obj"
  "lib001.dll.a"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/001.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
