""" Convert seconds to hours, minutes, seconds."""

def hr_min_sec(total_seconds):

    """ Enter a number of seconds."""
    if total_seconds == 0:
        return "0s"

    if total_seconds >= 3600:
        hours = total_seconds // 3600
        total_seconds = total_seconds % 3600
    else:
        hours = 0

    if total_seconds >= 60:
        minutes = total_seconds // 60
        total_seconds = total_seconds % 60
    else:
        minutes = 0

    seconds = total_seconds

    hms = []

    if hours > 0:
        hms.append(str(hours) + 'h')

    if minutes > 0:
        hms.append(str(minutes) + 'm')

    if seconds > 0:
        hms.append(str(seconds) + 's')

    return ' '.join(hms)
    # print(f' '.join(hms))

# if hr_min_sec(30) == '30s':
#     print('Test 1 of 8 passed')
# if hr_min_sec(60) == '1m':
#     print('Test 2 of 8 passed')
# if hr_min_sec(90) == '1m 30s':
#     print('Test 3 of 8 passed')
# if hr_min_sec(3600) == '1h':
#     print('Test 4 of 8 passed')
# if hr_min_sec(3601) == '1h 1s':
#     print('Test 5 of 8 passed')
# if hr_min_sec(3661) == '1h 1m 1s':
#     print('Test 6 of 8 passed')
# if hr_min_sec(90042) == '25h 42s':
#     print('Test 7 of 8 passed')
# if hr_min_sec(0) == '0s':
#     print('Test 8 of 8 passed')

assert hr_min_sec(30) == '30s'
assert hr_min_sec(60) == '1m'
assert hr_min_sec(90) == '1m 30s'
assert hr_min_sec(3600) == '1h'
assert hr_min_sec(3601) == '1h 1s'
assert hr_min_sec(3661) == '1h 1m 1s'
assert hr_min_sec(90042) == '25h 42s'
assert hr_min_sec(0) == '0s'

# hr_min_sec(3661)
