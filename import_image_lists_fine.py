# import_image_lists.py
# 导入图片列表到数据库
# 直接运行python manage.py前先运行python import_image_lists.py

# 导入 Django 的设置，以便脚本可以运行在 Django 环境中
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patchrating.settings")
django.setup()

# 导入您的模型
from ratingapp.models import ImageList


# 读取 image_list_x.txt 文件并导入数据库
def import_image_list(file_name):
    with open(file_name, 'r') as file:
        image_names = file.read()

    # 获取文件名中的数字，以确定 name 字段
    list_number = int(file_name.split('_')[3].split('.')[0])

    # # 创建并保存 ImageList 对象
    # image_list, created = ImageList.objects.get_or_create(name=f'image_list_{list_number}.txt', defaults={'image_names': image_names})
    # if not created:
    #     # 如果记录已存在，可以选择更新它或跳过
    #     pass

    # 尝试获取现有记录
    try:
        image_list = ImageList.objects.get(name=f'image_list_{list_number}.txt')
        image_list.image_names = image_names  # 更新 image_names 字段
        image_list.save()  # 保存更新
        print(f'Updated existing record for {file_name}')
    except ImageList.DoesNotExist:
        # 如果记录不存在，则创建新记录
        image_list = ImageList.objects.create(name=f'image_list_{list_number}.txt', image_names=image_names)
        print(f'Created new record for {file_name}')


if __name__ == '__main__':

    # list_path = os.path.join(os.path.abspath(__file__),"/static/image_list")
    list_path = "/home/www/patchrating/static/image_list"
    print(list_path)
    # 指定要导入的文件列表
    file_list = [os.path.join(list_path, "image_list_" + str(i) + ".txt") for i in range(1, 56)]

    # 循环导入文件
    for file_name in file_list:
        import_image_list(file_name)
