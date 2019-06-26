import sys

if sys.hexversion < 0x3000000:
    rng = xrange
    inp = raw_input
else:
    rng = range
    inp = input

def getter_fn(datatype):
    if datatype == str:
        return inp
    else:
        def fn(prompt=''):
            while True:
                try:
                    return datatype(inp(prompt))
                except ValueError:
                    print('Please enter a valid value!')
                    pass
        return fn

get_float = getter_fn(float)
get_int   = getter_fn(int)

def main():
    print("It's time to consider your child's education! Let's get started.")

    principal  = get_float("What is your initial investment?")
    deposit = get_float("How much will you be contributing each year?")
    apr = get_float("What do you anticipate your annual return rate to be?") / 100
    periods    = get_int  ("For how many years will you make a contribution?")
    timeleft = get_int  ("How many years will it be until your child receives post-secondary schooling?")

    deposits    = [deposit] * periods
    no_deposits = [0.] * (timeleft - periods)

    if deposit<=2500:
        contribution = deposit*0.2

    if deposit>2500:
        contribution = 500

    amount = principal

    print("The government of Canada matches your contribution by 20% up to $500 per year. This value is included in your saving's total value! Below you will see your amortization per year.")

    for yr, d in enumerate(deposits + no_deposits, 1):
        amount = ((amount + d) * (1. + apr)) + (contribution * (1. + apr))
        print('After {:>2d} year{} you have:   $ {:>10.2f}'.format(yr, 's,' if yr > 1 else ', ', amount))


if __name__ == '__main__':
    main()
