load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//pybazel:__subpackages__"])

py_library(
    name = "logger",
    srcs = ["logger.py"],
    deps = [
        requirement("colorama"),
    ],
)
