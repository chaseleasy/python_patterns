'''
    简单工厂类实现
    父类      master
    子类      node1 node2 node3
    工厂类    factory

'''


class master(object):
    def __init__(self):
        pass

    def run(self):
        print('im master')


class node1(master):
    def run(self):
        print('im node1')


class node2(master):
    def run(self):
        print('im node2')


class node3(master):
    def run(self):
        print('im node3')


class factory():
    def __init__(self):
        self.handers = {
            'node1': node1,
            'node2': node2,
            'node3': node3
        }

    def get_node(self, x):
        return self.handlers.get(x, lambda n: return None)(x)


if __name__ == '__main__':
    print(factory().get_node('node1'))
    print(factory().get_node('node2'))
    print(factory().get_node('node3'))
