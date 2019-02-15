'''
    简单工厂模式的实现

'''


# 产品类 初始化
class Product(object):

    def __init__(self, name):
        self.name = name

    def get_product_name(self):
        print(self.name)
        return self.name


class ProductTom(Product):
    pass


class ProductMax(Product):
    pass


class ProductLiu(Product):
    pass


# 工厂方法

def factory(product):
    handlers = {
        'Tom': ProductTom,
        'Max': ProductMax,
        'Liu': ProductLiu,
    }
    return handlers.get(product, lambda x: None)(product)


def has_product(product):
    handler = factory(product)
    if handler:
        handler.get_product_name()
    else:
        raise ValueError('Product Error')


if __name__ == '__main__':
    has_product('Tom')
    has_product('Max')
    has_product('Liu')
    has_product('TTT')
