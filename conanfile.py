from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import apply_conandata_patches, copy, export_conandata_patches, get, replace_in_file, rm, rmdir
import os

class UpClientDummy(ConanFile):
    name = "up-client-dummy-cpp"
    package_type = "library"
    license = "Apache-2.0 license"
    homepage = "https://github.com/eclipse-uprotocol"
    url = "https://github.com/conan-io/conan-center-index"
    description = "C++ Client Library for dummy to make a wrapper from"
    topics = ("ulink client", "transport")
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    conan_version = None
    generators = "CMakeDeps"
    version = "0.1"
    exports_sources = "CMakeLists.txt", "lib/*"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "build_testing": [True, False],
        "build_unbundled": [True, False],
        "build_cross_compiling": [True, False],
    }

    default_options = {
        "shared": False,
        "fPIC": False,
        "build_testing": False,
        "build_unbundled": False,
        "build_cross_compiling": False,
    }

    # def configure(self):
    #     self.options["up-cpp"].shared = True

    def requirements(self):
        if self.options.build_unbundled:
            self.requires("up-cpp/0.1.5.0-dev")
            self.requires("protobuf/3.21.12" + ("@cross/cross" if self.options.build_cross_compiling else ""))
        else:
            self.requires("up-cpp/0.1")
            self.requires("spdlog/1.13.0")
            self.requires("protobuf/3.21.12")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["up-client-dummy-cpp"]