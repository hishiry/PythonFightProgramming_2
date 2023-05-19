from ad import Ad
from hero import Hero


if __name__ == '__main__':
    ad_name = input("请输入 名称: ")
    ad_hp = input("请输入 血量: ")
    ad_power = input("请输入 战斗力: ")

    ad = Ad(ad_name, int(ad_hp), int(ad_power))
    ad.fight("ad_1", int(110), int(10))
