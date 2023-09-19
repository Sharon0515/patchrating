from django.shortcuts import render, redirect
from .models import ImageList, Tester, Rating
import os
import csv

# 登录页面后先查看实验须知
def experiment_intro(request):
    return render(request, 'experiment_intro.html')

# 确认进入实验后提交被试编号和被试信息
#
def enter_info(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        subject_number = request.POST.get('subject_number')
        school_number = request.POST.get('school_number')
        account = request.POST.get("account")

        tester = Tester.objects.create(age=age, gender=gender, subject_number=subject_number, account=account, school_number=school_number)

        return redirect('experiment', tester_id=tester.id)  # 跳转到实验界面
    return render(request, 'enter_info.html')





def test_temp(request):
    return render(request, 'htmltemp.html')


def thank_you(request):
    return render(request, 'thank_you.html')


def experiment(request, tester_id):
    # 初始化tester
    tester = Tester.objects.get(pk=tester_id)

    # 根据被试输入的编号找到对应的图片列表
    subject_number = tester.subject_number
    image_names = ImageList.objects.get(name=f'image_list_{subject_number}.txt')
    print(image_names)

    # 当点击评分按钮后的反应
    if request.method == 'POST':
        # 处理用户提交的评分数据
        rating_value = request.POST.get('rating')
        rated_image_name = request.session.get('rated_image_name')

        # 保存评分到数据库
        rating = Rating.objects.create(user=tester, image=rated_image_name, rating=rating_value)

    # 从缓存中读取最新的图片列表（包含初始化
    image_list = request.session.get('image_list', image_names.get_image_names())
    # 从缓存中读取当前的图片序号
    no = request.session.get('no',0)
    # print(image_list)
    no = no + 1
    # 获取当前图片的名字和序号
    if no==150:
        current_image_name = "lowmeaning-pacth1.png"
    else:
        current_image_name = image_list[0] if image_list else None  # 默认为第一张图片
        # 更新图片列表，删除已经保存并即将递送显示的第一张图片
        image_list = image_list[1:]
    # 更新图片列表到缓存
    request.session['image_list'] = image_list
    request.session['rated_image_name'] = current_image_name
    request.session['no'] = no
    print(current_image_name)

    return render(request, "experiment.html", {'current_image_name': current_image_name, 'no': no})


def test_rate_single_image(request):
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'outcome.csv')
    print("here")

    if request.method == 'POST':
        # 处理用户提交的评分数据
        rating = request.POST.get('rating')
        rated_image_name = request.session.get('rated_image_name')

        # 保存评分到数据库
        if not os.path.exists(csv_file_path):
            # 如果不存在，创建一个新的csv文件并写入头部信息和当前数据
            with open(csv_file_path, 'w', newline='') as csvfile:
                fieldnames = ['rated_image_name', 'rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'rated_image_name': rated_image_name, 'rating': rating})
        else:
            # 如果已存在，直接追加数据
            with open(csv_file_path, 'a', newline='') as csvfile:
                fieldnames = ['rated_image_name', 'rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # 将current_image_name和rating写入csv
                writer.writerow({'rated_image_name': rated_image_name, 'rating': rating})

    # 从缓存中读取最新的图片列表
    image_list = request.session.get('image_list', ['fine/4_1.png', 'fine/4_2.png', 'fine/4_3.png'])
    print(image_list)
    # 获取当前图片的名字
    current_image_name = image_list[0] if image_list else None  # 默认为第一张图片
    image_list = image_list[1:]  # 删除已经显示的第一张图片
    # 更新图片列表到缓存
    request.session['image_list'] = image_list
    request.session['rated_image_name'] = current_image_name
    print(current_image_name)

    return render(request, 'test_rate_single_image.html', {'current_image_name': current_image_name})
