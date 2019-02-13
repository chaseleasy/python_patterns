'''
    抽象工程模式

    具体工厂返回具体的产品
        抽象产品

        抽象工厂

        具体工厂实现具体产品



'''

from abc import ABCMeta, abstractmethod


class Product(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class ProductTom(Product):
    pass


class ProductMax(Product):
    pass


class ProductTomPlus(Product):
    pass


class ProductMaxPlus(Product):
    pass


# 定义抽象工厂


class Factory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_product_tom(self):
        pass

    @abstractmethod
    def create_product_max(self):
        pass


# 实例化抽象工厂

class FactoryTomAndMax(Factory):

    def create_product_max(self):
        return ProductMax(name='Max')

    def create_product_tom(self):
        return ProductTom(name='Tom')


class FactoryTomAndMaxPlus(Factory):

    def create_product_max(self):
        return ProductMaxPlus(name='MaxPlus')

    def create_product_tom(self):
        return ProductTomPlus(name='TomPlus')


if __name__ == '__main__':
    factory = FactoryTomAndMax()
    print(factory.create_product_max())
    print(factory.create_product_tom())

    factory_plus = FactoryTomAndMaxPlus()
    print(factory_plus.create_product_max())
    print(factory_plus.create_product_tom())
