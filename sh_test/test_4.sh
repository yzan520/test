#!/bin/bash
echo "Shell传递参数并比较大小实例"
echo "执行的文件名 $0"
echo "第一个参数为：$1"
echo "第二个参数为：$2"

if test $1 -eq $2
then
	echo "$1等于$2"
elif test $1 -gt $2
then
	echo "$1大于$2"
else 
	echo "$1小于$2"
fi
