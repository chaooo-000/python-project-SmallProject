import time as t


class Timer:
    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.prompt = '还没开始计时'
        self.lasted = []
        self.lasted_all = []
        self.begin = 0
        self.end = 0

    def __add__(self, other):
        self.prompt = '一起运行了'
        for index in range(6):
            self.lasted_all.append(self.lasted[index] + other.lasted[index])
            if self.lasted_all[index]:
                self.prompt += str(self.lasted_all[index]) + self.unit[index]
        return self.prompt

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def start(self):  # 计时
        self.prompt = '先停止计时'
        self.begin = t.localtime()
        print('开始计时')

    def stop(self):
        if not self.begin:
            self.prompt = '先开始计时'
        else:
            self.end = t.localtime()
            print('停止计时')
            self.cal()

    def cal(self):
        self.prompt = '运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
        self.begin = 0
        self.end = 0
