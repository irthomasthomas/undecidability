**Prompt:**
Make this content into a pretty gh markdown note:quote:- [ ] [abetlen/llama-cpp-python: Python bindings for llama.cpp](https://github.com/abetlen/llama-cpp-python)

 Python Bindings for llama.cpp

     

Simple Python bindings for @ggerganov's llama.cpp library. This package provides:

Low-level access to C API via ctypes interface.
High-level Python API for text completion
OpenAI-like API
LangChain compatibility
OpenAI compatible web server
Local Copilot replacement
Function Calling support
Vision API support
Multiple Models
Documentation is available at https://llama-cpp-python.readthedocs.io/en/latest.

Installation

llama-cpp-python can be installed directly from PyPI as a source distribution by running:

pip install llama-cpp-python
This will build llama.cpp from source using cmake and your system's c compiler (required) and install the library alongside this python package.

If you run into issues during installation add the --verbose flag to the pip install command to see the full cmake build log.

Installation with Specific Hardware Acceleration (BLAS, CUDA, Metal, etc)

The default pip install behaviour is to build llama.cpp for CPU only on Linux and Windows and use Metal on MacOS.

llama.cpp supports a number of hardware acceleration backends depending including OpenBLAS, cuBLAS, CLBlast, HIPBLAS, and Metal. See the llama.cpp README for a full list of supported backends.

All of these backends are supported by llama-cpp-python and can be enabled by setting the CMAKE_ARGS environment variable before installing.

On Linux and Mac you set the CMAKE_ARGS like this:

CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
On Windows you can set the CMAKE_ARGS like this:

$env:CMAKE_ARGS = "-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"
pip install llama-cpp-python
OpenBLAS

To install with OpenBLAS, set the LLAMA_BLAS and LLAMA_BLAS_VENDOR environment variables before installing:

CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
cuBLAS

To install with cuBLAS, set the LLAMA_CUBLAS=1 environment variable before installing:

CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
Metal

To install with Metal (MPS), set the LLAMA_METAL=on environment variable before installing:

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

#### Suggested labels
#### {   "key": "llm-python-bindings",   "value": "Python bindings for llama.cpp library" }

**Response:**
> **Python Bindings for llama.cpp**
> 
> Simple Python bindings for @ggerganov's llama.cpp library. This package provides:
> 
> - Low-level access to C API via ctypes interface.
> - High-level Python API for text completion
> - OpenAI-like API
> - LangChain compatibility
> - OpenAI compatible web server
> - Local Copilot replacement
> - Function Calling support
> - Vision API support
> - Multiple Models
> 
> Documentation is available at [https://llama-cpp-python.readthedocs.io/en/latest](https://llama-cpp-python.readthedocs.io/en/latest).
> 
> **Installation**
> 
> llama-cpp-python can be installed directly from PyPI as a source distribution by running:
> 
> ```
> pip install llama-cpp-python
> ```
> 
> This will build llama.cpp from source using cmake and your system's c compiler (required) and install the library alongside this python package.
> 
> If you run into issues during installation add the `--verbose` flag to the `pip install` command to see the full cmake build log.
> 
> **Installation with Specific Hardware Acceleration (BLAS, CUDA, Metal, etc)**
> 
> The default `pip install` behaviour is to build llama.cpp for CPU only on Linux and Windows and use Metal on MacOS.
> 
> llama.cpp supports a number of hardware acceleration backends depending including OpenBLAS, cuBLAS, CLBlast, HIPBLAS, and Metal. See the llama.cpp README for a full list of supported backends.
> 
> All of these backends are supported by llama-cpp-python and can be enabled by setting the `CMAKE_ARGS` environment variable before installing.
> 
> On Linux and Mac you set the `CMAKE_ARGS` like this:
> 
> ```
> CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
> ```
> 
> On Windows you can set the `CMAKE_ARGS` like this:
> 
> ```
> $env:CMAKE_ARGS = "-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"
> pip install llama-cpp-python
> ```
> 
> **OpenBLAS**
> 
> To install with OpenBLAS, set the `LLAMA_BLAS` and `LLAMA_BLAS_VENDOR` environment variables before installing:
> 
> ```
> CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
> ```
> 
> **cuBLAS**
> 
> To install with cuBLAS, set the `LLAMA_CUBLAS=1` environment variable before installing:
> 
> ```
> CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
> ```
> 
> **Metal**
> 
> To install with Metal (MPS), set the `LLAMA_METAL=on` environment variable before installing:
> 
> ```
> CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
> ```
> 
> #### Suggested labels
> 
> { "key": "llm-python-bindings", "value": "Python bindings for llama.cpp library" }

<details><summary>Metadata</summary>

- Duration: 16503 ms
- Datetime: 2024-01-11T11:10:13.440968
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.1}
```

