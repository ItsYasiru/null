from core import Queue
from core.Formatting import multi_str_ljust, prompt, snakecase_to_camelcase


def question_one() -> None:
    """Employee bonus calculation"""
    years = prompt("How many years have you worked for our company?", int)
    base_pay = prompt("How much is your salary?", int)

    bonus_amount = int(base_pay * (0.2 if years > 5 else 0.1))

    print(f"\nCongratulations! Your bonus is $ {bonus_amount:,}")


def question_two() -> None:
    """Compounding bank interest calculation"""
    balance = starting_balance = prompt("Hom much do you want to deposite as the starting balanace?", int)
    balance_cap, grow_rate = 1_000_000, 2

    years = 0
    while balance < balance_cap:
        balance += balance * grow_rate
        years += 1

    print(f"\nWith a starting balance of ${starting_balance:,} it will take {years:,} years to reach ${balance_cap:,}")


def question_three() -> None:
    """Patterns question"""

    def increment_pattern(init_value: int, increment: int, terms: int = 10):
        pattern, cycles = [init_value], 0
        while cycles < terms:
            pattern.append(pattern[-1] + increment)
            cycles += 1

        print(str(pattern).strip("[]"))

    def cascading_pattern(init_value: int, terms: int = 10):
        pattern, cycles = str(), 0
        while cycles < terms:
            pattern += f"{(str(init_value) + ' ') * init_value}\n"
            init_value += 1
            cycles += 1

        print(pattern)

    increment_pattern(3, 3)
    increment_pattern(20, -4)
    increment_pattern(6, 10)
    cascading_pattern(1, 5)


def question_four() -> None:
    """Simple age calculator"""
    day_check = lambda day: day <= 30
    month_check = lambda month: month <= 12
    year_check = lambda year: len(str(year)) == 4

    prompts = ["Enter todays day", "Enter todays month", "Enter todays year", "Enter birth day", "Enter birth month", "Enter birth year"]
    prompts = Queue(multi_str_ljust(prompts, append=":"))

    with prompts:
        current_day = prompt(prompts.next(), int, check=day_check)
        current_month = prompt(prompts.next(), int, check=month_check)
        current_year = prompt(prompts.next(), int, check=year_check)

        birth_day = prompt(prompts.next(), int, check=day_check)
        birth_month = prompt(prompts.next(), int, check=month_check)
        birth_year = prompt(prompts.next(), int, check=year_check)

    total_days = (current_year - birth_year) * 12 * 30 + (current_month - birth_month) * 30 + (current_day - birth_day)

    years_delta = total_days // (12 * 30)
    months_delta = (total_days - years_delta * 12 * 30) // 30
    days_delta = total_days - years_delta * 12 * 30 - months_delta * 30

    print(f"\nYears : {years_delta:,} Months : {months_delta:,} Days : {days_delta:,}")


def main() -> None:
    questions = [question_one, question_two, question_three, question_four]

    for question in questions:
        print(f">>> {snakecase_to_camelcase(question.__name__, sep=' ')} - {question.__doc__},\n")
        question()


main()
