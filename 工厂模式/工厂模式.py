'''
    工厂模式的实现
'''

from abc import ABCMeta, abstractmethod


# 产品抽象类
class Product(object):
    __metaclass__ = ABCMeta

    def __init__(self, factory, type):
        self.factory = factory
        self.type = type

    @abstractmethod
    def get_factory_name(self):
        pass

    @abstractmethod
    def get_factory_type(self):
        pass


class ProductInit(Product):
    def get_factory_name(self):
        return self.factory

    def get_factory_type(self):
        return self.type


# 工厂父类
class Factory(object):
    def __init__(self):
        pass

    def create_product(self):
        pass


# 产品实例化 HP
class ProductHP(ProductInit):
    def __init__(self):
        super().__init__(factory='HP', type='鼠标')


# 产品实例化 ASUS
class ProductASUS(ProductInit):
    def __init__(self):
        super().__init__(factory='ASUS', type='鼠标')


# 产品实例化 ShenZhou
class ProductShenZhou(ProductInit):
    def __init__(self):
        super().__init__(factory='ShenZhou', type='鼠标')


# HP工厂类 继承
class FactoryHP(Factory):
    def create_product(self):
        return ProductHP()


# ASUS 工厂类 继承
class FactoryASUS(Factory):
    def create_product(self):
        return ProductASUS()


class FactoryShenZhou(Factory):
    def create_product(self):
        return ProductShenZhou()


if __name__ == '__main__':
    print(FactoryHP().create_product().get_factory_name())
    print(FactoryASUS().create_product().get_factory_name())
    print(FactoryShenZhou().create_product().get_factory_name())
