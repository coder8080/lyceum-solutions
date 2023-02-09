import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=int, default=0)
parser.add_argument('--per-week', type=int, default=0)
parser.add_argument('--per-month', type=int, default=0)
parser.add_argument('--per-year', type=int, default=0)
parser.add_argument('--get-by', type=str, default="day",
                    choices=['day', 'month', 'year'])
args = parser.parse_args()
per_day = args.per_day
per_day += args.per_week / 7
per_day += args.per_month / 30
per_day += args.per_year / 360
result = 0
if args.get_by == "day":
    result = per_day
elif args.get_by == "month":
    result = per_day * 30
elif args.get_by == "year":
    result = per_day * 360
print(int(result))
