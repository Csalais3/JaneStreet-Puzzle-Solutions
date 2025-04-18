def path_probability (p, tol, max_iter):
    if p <= 0.5:
        return 0
    
    p1 = (2 * p - 1) / p
    p0 = 0.5
    
    contrib_p1 = 1.0 - (1.0 - p1) ** 2
    
    for i in range(max_iter):
        new_p0 = p * (1.0 - (1.0 - p0) ** 2) + (1.0 - p) * contrib_p1
        
        if abs(new_p0 - p0) < tol:
            p0 = new_p0
            break
        
        p0 = new_p0
        
    return p0


def solve_for_p_half (tol):
    
    left, right = 0.5, 1.0
    
    while right - left > tol:
        mid = 0.5 * (left + right)
        val = path_probability(mid)
    
        if val < 0.5:
            left = mid
        else:
            right = mid
    
    return 0.5 * (left + right)

if __name__ == "main":
    p_star = solve_for_p_half()
    print(f"p is approximately {p_star}")
    