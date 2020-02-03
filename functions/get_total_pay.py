def get_total_pay(working_hours, rate, hours, overtime_rate):
    """Function to calculate emp total pay

    Args:
        working_hours (int): maximum hours per week
        rate (float): pay rate for normal working hours
        hours (int): time worked
        overtime_rate (int): rate for every extra hours worked

    Returns:
        float: Total pay normal plus any overtime
    """

    if hours > working_hours:
        total = (rate * working_hours) + \
            ((hours - working_hours) * overtime_rate)
    else:
        total = rate * hours
    return total


working_hours = 40
rate = 3.5
overtime_rate = 1.5
my_hours = int(input('Enter Hours Worked\n'))

print(get_total_pay(working_hours, rate, my_hours, overtime_rate))
