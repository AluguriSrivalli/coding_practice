import sys

if __name__ == '__main__':
    time_charged = float(sys.stdin.readline().strip())
    
    if time_charged >= 4.00:
        battery_lasted = 8.00
    else:
        battery_lasted = time_charged * 2.0
        
    print(f"{battery_lasted:.2f}")
