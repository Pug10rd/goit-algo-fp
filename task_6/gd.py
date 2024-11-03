# Food items with their cost and calories
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    """Greedy algorithm to select food items maximizing calories per cost."""
    # Calculate calories per cost for each item
    items_sorted = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = {}
    
    for item, details in items_sorted:
        if details["cost"] <= budget:
            selected_items[item] = details
            total_calories += details["calories"]
            budget -= details["cost"]
    
    return selected_items, total_calories

def dynamic_programming(budget):
    """Dynamic programming algorithm to find the optimal selection of food items."""
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Convert the items dictionary to a list for easier indexing
    item_list = list(items.items())
    
    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost = details["cost"]
        calories = details["calories"]
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # Retrieve the selected items based on the dp table
    selected_items = {}
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item was included
            item, details = item_list[i - 1]
            selected_items[item] = details
            w -= details["cost"]

    return selected_items, dp[n][budget]

# Example usage
budget = 100  # Define the budget

# Greedy algorithm
greedy_selection, greedy_calories = greedy_algorithm(budget)
print("Greedy Algorithm Selection:")
print("Selected Items:", greedy_selection)
print("Total Calories:", greedy_calories)

# Dynamic programming algorithm
dp_selection, dp_calories = dynamic_programming(budget)
print("\nDynamic Programming Selection:")
print("Selected Items:", dp_selection)
print("Total Calories:", dp_calories)