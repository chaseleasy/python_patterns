'''
    抽象工厂模式
'''
from abc import ABCMeta, abstractmethod


# 抽象工厂类
class Factory(object):
    __metaclass__ = ABCMeta

    def __init__(self, factory_name):
        self.factory_name = factory_name

    @abstractmethod
    def get_factory_name(self):
        pass

    @abstractmethod
    def get_factory_product(self):
        pass

    @abstractmethod
    def return_mouse_product(self):
        pass

    @abstractmethod
    def return_keyborad_product(self):
        pass


# 抽象产品类
class Product(object):
    __metaclass__ = ABCMeta

    def __init__(self, product_type, product_firm):
        self.product_type = product_type
        self.product_firm = product_firm

    @abstractmethod
    def get_product_type(self):
        pass

    def get_product_firm(self):
        return self.product_firm if self.product_firm else None


# 鼠标产品
class ProductMouse(Product):
    def __init__(self, product_firm):
        super().__init__(product_type='Mouse', product_firm=product_firm)

    def get_product_type(self):
        return self.product_type


# 键盘产品
class ProductKeyborad(Product):
    def __init__(self, product_firm):
        super().__init__(product_type='Keyborad', product_firm=product_firm)

    def get_product_type(self):
        return self.product_type


# 惠普工厂
class FactoryHP(Factory):
    def __init__(self):
        super().__init__(factory_name='HP')

    def get_factory_name(self):
        return self.factory_name

    def get_factory_product(self):
        return [self.return_keyborad_product(), self.return_mouse_product()]

    def return_mouse_product(self):
        return ProductMouse(product_firm='HP')

    def return_keyborad_product(self):
        return ProductKeyborad(product_firm='HP')


# 华硕工厂
class FactoryASUS(Factory):
    def __init__(self):
        super().__init__(factory_name='ASUS')

    def get_factory_name(self):
        return self.factory_name

    def get_factory_product(self):
        return [self.return_keyborad_product(), self.return_mouse_product()]

    def return_mouse_product(self):
        return ProductMouse(product_firm='ASUS')

    def return_keyborad_product(self):
        return ProductKeyborad(product_firm='ASUS')


if __name__ == '__main__':
    factory_hp = FactoryHP()
    print(factory_hp.return_mouse_product())
    print(factory_hp.return_keyborad_product())
    print(factory_hp.return_keyborad_product().get_product_firm())
    print(factory_hp.return_keyborad_product().get_product_type())

    factory_asus = FactoryASUS()
    print(factory_asus.return_mouse_product())
    print(factory_asus.return_keyborad_product())
    print(factory_asus.return_keyborad_product().get_product_firm())
    print(factory_asus.return_keyborad_product().get_product_type())
