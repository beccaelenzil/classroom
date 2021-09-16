def knapsack(weights, values, max_weight):
    max_value = 0
    
    if not weights or not values:
        return max_value
    
    n = len(weights)
    
    
    for i in range(n):
        for j in range(i,n+1):
            total_weight = sum(weights[i:j])
            total_value = sum(values[i:j])
            print(total_weight, total_value)
            if total_weight <= max_weight and total_value >= max_value:
                max_value = total_value
                
    return max_value

print(knapsack(
        [99, 60, 70, 68, 50, 65, 48, 31, 52, 29],
        [104, 105, 138, 135, 82, 73, 103, 52, 57, 136],
        75))