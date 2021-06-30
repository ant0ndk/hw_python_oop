import datetime as dt


class Record():
    '''Констркутор класса Record.'''
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        try:
            self.date = dt.datetime.strptime(str(date), '%d.%m.%Y').date()
        except Exception:
            self.date = dt.date.today()


class Calculator:
    '''Констркутор класса Calculator.'''
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
        date_now = dt.date.today()
        last_week = date_now - dt.timedelta(days=7)
        for i in self.records:
            if last_week < i.date <= date_now:
                week_stats += i.amount
        return week_stats

    # Получить остаток на текущий день
    def get_today_limit(self):
        sp_today = self.limit - self.get_today_stats()
        return sp_today


class CaloriesCalculator(Calculator):
    # Получить остаток калорий на текущий день
    def get_calories_remained(self):
        if self.get_today_limit() > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {self.get_today_limit()} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    # Курсы валют
    USD_RATE = 72.0
    EURO_RATE = 86.0
    RUB_RATE = 1.0

    # Получить остаток денег на текущий день
    def get_today_cash_remained(self, currency):
        currencies = {'usd': (self.USD_RATE, 'USD'),
                      'eur': (self.EURO_RATE, 'Euro'),
                      'rub': (self.RUB_RATE, 'руб')}
        self.cash = self.get_today_stats()
        if self.cash == self.limit:
            return 'Денег нет, держись'
        if currency not in currencies:
            return 'Указанной валюты в базе нет'
        (rate, name) = currencies[currency]
        self.cash = round((
            self.get_today_limit()) / rate, 2)
        if self.cash > 0:
            return (f'На сегодня осталось {self.cash}'
                    f' {name}')
        else:
            return (f'Денег нет, держись: твой долг - '
                    f'{abs(self.cash)} {name}')
