#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
    cv::Mat a = cv::imread("/home/zps/test/c++/opencv_test/apple.jpg");
    if(a.empty())
    {
        printf("failed to load image!");
    }
    else
    {
        cv::imshow("test",a);
        cv::waitKey(0);
    }
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
