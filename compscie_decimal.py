from decimal import Decimal, getcontext

# Higher precision for 100+ decimals
getcontext().prec = 150

def run_lab():
    # My cylinder setup: V = pi * r^2 * h
    r = Decimal('10')
    h = Decimal('20')

    # Pre-calculate (r squared * h) to multiply with pi later
    mult = (r**2) * h
    
    # Accurate pi reference
    pi_val = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808")

    points = [20, 40, 60, 100]

    for p in points:
        # TRUNCATE: Slice string at point p
        pi_s = str(pi_val)
        pi_t = Decimal(pi_s[:p+2]) #point, (2) first number and the decimal point
        v_t = pi_t * mult # Truncated volume
        
        # ROUND: Math rounding at point p
        pi_r = round(pi_val, p) # Rounded pi
        v_r = pi_r * mult
        
        # GAP: Absolute difference
        gap = abs(v_r - v_t)

        # Result output
        print(f"DECIMALS: {p}")
        print(f"TRUNC: {v_t}")
        print(f"ROUND: {v_r}")
        print(f"GAP:   {gap:.2E}")
        print("-" * 15)

if __name__ == "__main__":
    run_lab()