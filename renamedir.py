import os
import re


def replcaeFileName(pic_path):  # 修改pic_path路径下的文件名
    piclist = os.listdir(pic_path)
    total_num = len(piclist)

    i = 1
    for pic in piclist:
        if pic.endswith(".jpg"):  # 修改成你自己想要重命名的文件格式
            old_path = os.path.join(os.path.abspath(pic_path), pic)
            new_path = os.path.join(os.path.abspath(pic_path), str(1000 + (int(i))) + '.jpg')  # 修改成了1000+N这种格式

            os.renames(old_path, new_path)
            print("把原图片命名格式：" + old_path + u"转换为新图片命名格式：" + new_path)
            i = i + 1


def replaceDirName(rootDir):  # 修改rootDir路径下的文件夹名
    num = 0
    dirs = os.listdir(rootDir)
    for dir in dirs:
        print('oldname is:' + dir)  # 输出老的名字
        # temp = "%03d" % int(num)  # 主要目的是在数字统一为3位，不够的前面补0
        temp = 'id' + str(num)
        oldname = os.path.join(rootDir, dir)  # 老文件夹的名字
        newname = os.path.join(rootDir, temp)  # 新文件夹的名字

        os.rename(oldname, newname)  # 替换
        num = num + 1

if __name__ == '__main__':
    # rootDir = './data'
    replaceDirName('./Celeba_glasses_test')
    # replcaeFileName(rootDir)


