def find_outlier(integers):
    is_odd = len([num for num in integers[:3] if num%2]) < 2
    return next(num for num in integers if bool(num%2) == is_odd)