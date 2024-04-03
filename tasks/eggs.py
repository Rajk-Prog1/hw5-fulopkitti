def eggs_solution(breaks):
    low_ = 1
    high_ = 100

    while low_ < high_:
        mid = (low_ + high_)//2
        if breaks(mid):
            high_ = mid
        else:
            low_ = mid+1
        
    return low_- 1



