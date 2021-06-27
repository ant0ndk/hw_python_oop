import datetime as dt


class Record():
    def __init__(self, amount, comment, date):
        '''Констркутор класса Record'''
        self.amount = amount
        self.comment = comment
        self.date = dt.date.today()


class Calculator:
    def __init__(self, limit):
        '''Констркутор класса Calculator'''
        self.limit = limit
        self.records = []
        self.today = dt.date.today()


    def add_record(self, note):
        '''Добавление записи'''
        self.record.append(note)


    '''Получить статистику на текущий день'''
    def get_today_stats(self):
        today_stats = 0
        for i in self.records:
            if i.date == dt.date.today():
                today_stats += i.amount
        return today_stats


    def get_week_stats(self):
        '''Получить статистику на текущую неделю'''
        week_stats = 0
        for i in self.records:
            if i.date <= self.week <= dt.date.today():
                week_stats += i.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        eaten_today = self.limit - self.get_today_stats()
        if eaten_today > 0:
            msg = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                   f'калорийностью не более {eaten_today} кКал')
        else: 
            msg = 'Хватит есть!'
        return msg
# class CashCalculator(Calculator):
