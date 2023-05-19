import datetime


def timer(func):
    def inner(*args):
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()
        print(f"打斗时间为{end_time - start_time}")
    return inner


# @timer
# def demo(name):
#     print("demo_name")
#
#
# demo("a")

