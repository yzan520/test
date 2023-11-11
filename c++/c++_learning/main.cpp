#include <iostream>
#include <fmt/color.h>
#include <filesystem>

//int test();
//
int main() {

//    for (int i = 0; i<10; i++) {
//        test();
//    }
//    return 0;
//}
//
//int test() {
//    static int a = 1;
//    a++;
//    printf("%d ", a);
//}

//#define TRT_ASSERT(expr)                                                      \
//    do{                                                                       \
//        if(!(expr)) {                                                         \
//            fmt::print(fmt::fg(fmt::color::red), "assert fail: '" #expr "'"); \
//            exit(-1);                                                         \
//        }                                                                     \
//    } while(0)
//
//int main() {
//    int x = 10;
//
//    TRT_ASSERT(x>20);

    std::filesystem::path onnx_file_path("home/zps/open_source/CVRM2021-sjtu/asset/model-opt-4.onnx");
    auto cache_file_path = onnx_file_path;
    cache_file_path.replace_extension("cache");
       // 打印结果
    std::cout << "Original Path: " << onnx_file_path << std::endl;
    std::cout << "Modified Path: " << cache_file_path << std::endl;

}