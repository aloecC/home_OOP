class Enployee:
    def __init__(self):
        self.pay = 50000


class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID += 1
        self.order_log()

    def order_log(self):
        print(f'{self.id}-й сотрудник')


class Developer(MixinLog, Enployee):

    def __init__(self):
        super().__init__()

    def work(self):
        print('Write')

    def code(self):
        pass


dev_1 = Developer()
dev_2 = Developer()

print(Developer.__mro__)
