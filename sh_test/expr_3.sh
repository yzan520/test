#! /bin/bash
a=10
b=20

if [ $a != $b ]
then
	echo "$a != $b : a不等于b"
else 
	echo "$a == $b : a等于b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then 
	echo "$a 小于100且 $b 大于15 ：返回true"
else 
	echo "$a 小于100且 $b 大于15 ：返回false"
fi
