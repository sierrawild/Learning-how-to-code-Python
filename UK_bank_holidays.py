from govuk_bank_holidays.bank_holidays import BankHolidays

CHOSE_YEAR = 2026

bank_holidays = BankHolidays()
bank_holidays = BankHolidays(locale='en')
for bank_holiday in bank_holidays.get_holidays():
    year = bank_holiday['date'].year
    if year == CHOSE_YEAR:
        print(bank_holiday['title'], 'is on', bank_holiday['date'])
print(bank_holidays.get_next_holiday())

# see govuk_bank_holidays/bank_holidays.py source file for more methods and argument details…

# choose a different locale for holiday titles and notes
bank_holidays = BankHolidays(locale='en')

# use cached holidays if internet connection is not desired
bank_holidays = BankHolidays(use_cached_holidays=True)