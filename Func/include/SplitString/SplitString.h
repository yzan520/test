//
// Created by zps on 23-10-21.
//

#ifndef VERSION_TEST_SPLITSTRING_H
#define VERSION_TEST_SPLITSTRING_H

#include <string>
#include <vector>

/**
 * @brief 对输入的字符串 str 以 c 进行分割
 * @example
 *  [in] "/usr/local/include" "/"
 *  [out] ["", "usr", "local", "include"]
 *  @fun_code 1
 *
 * @param str[in] 输入字符串
 * @param c[in] 以 c 进行分割
 * @param substring[out] 分割后的结果 数组/向量
 */
void splitString(const std::string& src, const char& c, std::vector<std::string>* substring);

#endif //VERSION_TEST_SPLITSTRING_H
