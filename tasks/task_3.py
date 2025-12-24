# Задача: Анализ продаж интернет-магазина

orders = [
    {"id": 1, "customer": "Alice", "product": "Laptop", "price": 1200, "date": "2025-10-01"},
    {"id": 2, "customer": "Bob", "product": "Mouse", "price": 25, "date": "2025-10-01"},
    {"id": 3, "customer": "Alice", "product": "Keyboard", "price": 45, "date": "2025-10-02"},
    {"id": 4, "customer": "Charlie", "product": "Laptop", "price": 1200, "date": "2025-10-03"},
    {"id": 5, "customer": "Bob", "product": "Monitor", "price": 300, "date": "202510-04"},
    {"id": 6, "customer": "Alice", "product": "Mouse", "price": 25, "date": "2025-10-05"},
    {"id": 7, "customer": "Charlie", "product": "Keyboard", "price": 45, "date": "2025-10-05"},
    {"id": 8, "customer": "David", "product": "Mouse", "price": 25, "date": "2025-10-06"},
]

# Базовая статистика
def get_stats(orders_lists):
    total_orders  = len(orders_lists)
    total_revenue = sum(orders_lists["price"] for orders_lists in orders_lists)
    product_counts = {}

    for order in orders_lists:
        product = order["product"]
        product_counts[product] = product_counts.get(product, 0) + 1

    most_popular_product = max(product_counts, key=product_counts.get)

    top_customer = max(product_counts, key=product_counts.get)

    return {"total_orders": total_orders, "total_revenue": total_revenue, "most_popular_product": most_popular_product, "top_customer": top_customer}


stats = get_stats(orders)
print(stats["total_orders"])
print(stats["total_revenue"])
print(stats["most_popular_product"])
print(stats["top_customer"])

# Фильтрация по дате
def get_orders_by_date(orders_lists, start_date, end_date):
    return [
        order for order in orders_lists
        if start_date <= order["date"] <= end_date
    ]


filtered = get_orders_by_date(orders, start_date="2025-10-01", end_date="2025-10-02")
print(filtered)
print(len(filtered))

# Группировка по клиенту
def get_customer_summary(orders_lists):
    customer_summary = {}
    for order in orders_lists:
        customer = order["customer"]
        product = order["product"]
        price = order["price"]

        if customer not in customer_summary:
            customer_summary[customer] = {"orders": [], "total_spent": 0}

        customer_summary[customer]["orders"].append(product)
        customer_summary[customer]["total_spent"] += price

    return customer_summary

summary = get_customer_summary(orders)
print(summary)
print(len(summary))