import keyword

# print(1111);
# print(keyword.kwlist);
#
# print("324243ww2"[0:-2]);

while True:
    str = input("请用2个字评价下自己\n");
    if len(str) == 2:
        print(str, end="?还是去照照镜子吧")
        break
    else:
        print("让你输入2个字,看不懂中文吗？再来一次!")