from django.core.paginator import Paginator
from django.conf import settings
from posts.models import *
from posts.serializers import *


def post_list_service(user, page):
    DEFAULT_PER_PAGE = settings.DEFAULT_PER_PAGE

    posts = Post.objects.filter(is_deleted=False)[(page - 1) * DEFAULT_PER_PAGE: page * DEFAULT_PER_PAGE]

    serializer = PostSerializer(posts, many=True)

    response = {
        "currentPage": page,
        "posts": serializer.data
    }
    return response


def rate_a_post_service(user, data):
    post_id = data['postID']
    rate_number = data['rateNumber']

    # check if post exist
    targe_post = Post.objects.filter(id=post_id).first()

    if targe_post is None:
        raise Exception("Sorry, Post doesn't exist!")

    exist_rate = Rate.objects.filter(created_by=user, post=targe_post).first()

    if exist_rate is None:
        exist_rate = Rate.objects.create(value=rate_number, post=targe_post, created_by=user)
        targe_post.rate_count += 1
        targe_post.total_value_raw_rate += rate_number

    else:

        targe_post.total_value_raw_rate -= exist_rate.value
        exist_rate.value = rate_number
        targe_post.total_value_raw_rate += rate_number

    exist_rate.save()
    targe_post.save()
    response = {
        "yourRate": rate_number,
        "message": "successfully registered your rate"
    }
    return response


def rate_list_service(user,post_id, page):
    DEFAULT_PER_PAGE = settings.DEFAULT_PER_PAGE

    post_ = Post.objects.filter(id=post_id ,is_deleted=False).first()

    if post_ is None:
        raise Exception("Sorry, Post doesn't exist!")

    rating_list = post_.ratings.all()[(page - 1) * DEFAULT_PER_PAGE: page * DEFAULT_PER_PAGE]
    print(rating_list)

    serializer = RateSerializer(rating_list, many=True)

    response = {
        "currentPage": page,
        "rates": serializer.data
    }
    return response
