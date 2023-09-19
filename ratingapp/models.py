from django.db import models

from django.db import models


# 图片列表
class ImageList(models.Model):
    name = models.CharField(max_length=100)  # 用于标识 image_list 的名称
    image_names = models.TextField()  # 存储图片名，使用文本字段，可以存储多个图片名，每行一个

    def get_image_names(self):
        return self.image_names.split('\n')


# 被试信息
class Tester(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    age = models.PositiveIntegerField()   # 年龄
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)   # 性别
    school_number = models.CharField(max_length=15)   # 学号
    subject_number = models.CharField(max_length=50)  # 被试编号
    account = models.CharField(max_length=50)   # 支付宝账号



# 打分信息
class Rating(models.Model):
    RATING_CHOICES = [
        (1, 'Very High'),
        (2, 'High'),
        (3, 'Neutral'),
        (4, 'Low'),
        (5, 'Very Low'),
    ]

    image = models.CharField(max_length=50)
    user = models.ForeignKey(Tester, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

# Tester 类存储试验者的信息，包括年龄和性别。
# assigned_images 字段使用 ManyToManyField 来与 Image 类建立多对多关系，表示每个试验者分配到的图片。


# Image 类存储图片信息，包括标题、图片文件和上传日期。


# Rating 类存储评分信息，其中 user 字段是一个外键，关联到试验者，image 字段是一个外键，关联到图片，rating 字段存储评分，comment 字段存储评论。
