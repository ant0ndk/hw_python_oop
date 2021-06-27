import datetime as dt


class Record():
    # Констркутор класса Record
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        try:
            date = dt.datetime.strptime(str(date), '%d.%m.%Y').date()
        except Exception:
            date = dt.date.today()
        self.date = date


class Calculator:
    # Констркутор класса Calculator
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    # Добавление записи
    def add_record(self, note):
        self.records.append(note)

    # Получить статистику на текущий день
    def get_today_stats(self):
        today_stats = 0
        for i in self.records:
            if i.date == dt.date.today():
                today_stats += i.amount
        return today_stats

    # Получить статистику на текущую неделю
    def get_week_stats(self):
        week_stats = 0
        date_now = dt.datetime.today().date()
        last_week = date_now - dt.timedelta(days=7)
        for i in self.records:
            if last_week < i.date <= date_now:
                week_stats += i.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        eaten_today = self.limit - self.get_today_stats()
        if eaten_today > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {eaten_today} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 72.0
    EURO_RATE = 86.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        currencies = {'usd': (self.USD_RATE, 'USD'),
                      'eur': (self.EURO_RATE, 'Euro'),
                      'rub': (self.RUB_RATE, 'руб')}
        self.cash = self.get_today_stats()
        if self.cash == self.limit:
            return 'Денег нет, держись'
        try:
            remained_cash = round((
                self.limit - self.cash) / currencies[currency][0], 2)
            debt_cash = round((
                self.cash - self.limit) / currencies[currency][0], 2)
        except KeyError:
            return 'Указанной валюты в базе нет'
        if self.cash < self.limit:
            return (f'На сегодня осталось {remained_cash}'
                    f' {currencies[currency][1]}')
        else:
            return (f'Денег нет, держись: твой долг - '
                    f'{debt_cash} {currencies[currency][1]}')
