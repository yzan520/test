所有编程技术不断优化与升级都在做三件事情：提升效率  减少重复  减轻依赖

```markdown
"低耦合" 是软件工程中一个重要的设计原则，指的是系统中的各个组件或模块之间的相互依赖性尽可能地降低。低耦合的设计有助于提高代码的灵活性、可维护性和可重用性。

以下是一些实现低耦合设计的常见方法：

1. 模块化设计：将系统分解成相互独立的模块或组件，每个模块只关注特定的功能。模块之间的依赖关系应该尽可能地简单明了。

2. 接口定义：使用清晰的接口定义模块之间的交互。接口应该是简洁的，不涉及过多的实现细节，同时提供足够的信息以满足调用方的需求。

3. 依赖注入： 将模块所需的依赖项从外部传递给模块，而不是在模块内部直接创建依赖。这样可以减少模块之间的直接耦合，使得模块更容易替换和测试。

4. 事件驱动架构： 使用事件和消息机制进行模块之间的通信。模块只需发布和订阅感兴趣的事件，而不直接调用其他模块的方法，从而降低耦合度。

5. 松散耦合的设计模式：使用设计模式，如观察者模式、策略模式等，以实现松散耦合。这些模式通过定义清晰的接口和抽象来降低组件之间的依赖性。

6. 面向接口编程：鼓励使用接口而不是具体实现进行编程。这样，实现可以随时更改，而不会影响其他模块。

7. 依赖反转：使用依赖反转原则，即高层模块不应该依赖于低层模块，两者都应该依赖于抽象。这有助于减少直接依赖，提高系统的灵活性。

通过这些方法，可以创建一个更加灵活、可维护和可测试的系统，使得系统中的各个部分能够更独立地变化而不会对其他部分造成过多的影响。

```

# Cmake

```cmake
# 定义项目
cmake_minimum_required(VERISON 3.0) # 进行编译所需要的CMake最低版本，如果不指定的话系统会自己指定一个，但是也会扔出一个warning。

project(myProject C CXX) # 该命令会影响 PROJECT_SOURCE_DIR、PROJECT_BINARY_DIR、PROJECT_NAME等变量。另外要注意的是，对于多个project嵌套的情况，CMAKE_PROJECT_NAME是当前 CMakeLists.txt 文件回溯至最顶层 CMakeLists.txt 文件中所在位置之前所定义的最后一个project的名字。

add_subdirectory() # 用于添加子目录，它告诉 CMake 在当前项目中包含其他目录中的 CMakeLists.txt 文件，从而构建这些子目录中的代码。

include_directories()

add_executable(executable_name source1.cpp source2.cpp ...) # 添加可执行文件，并指定源文件


add_library(library_name source1.cpp source2.cpp ...) # 生成静态库文件

link_libraries(library1 library2 ...) # 将目标（例如可执行文件和库）链接到特定库

target_link_libraries(target_name library1 library2 ...) # 它提供了更具有针对性的库链接方式，可以在每个目标级别上指定链接关系



```