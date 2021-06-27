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
            msg = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                   f'калорийностью не более {eaten_today} кКал')
        else:
            msg = 'Хватит есть!'
        return msg
# class CashCalculator(Calculator):
