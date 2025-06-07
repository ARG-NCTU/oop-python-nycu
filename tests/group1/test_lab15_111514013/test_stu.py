def test_lab15():
    import pandas as pd

    # Create a sample DataFrame
    data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 30, 35, None],
            'salary': [50000, 60000, 75000, 65000]}
    df = pd.DataFrame(data)

    # Display basic info
    print("DataFrame Info:")
    print(df.info())

    # Handle missing values
    df['age'].fillna(df['age'].mean(), inplace=True)

    # Filter employees with salary > 60000
    high_earners = df[df['salary'] > 60000]
    print("\nHigh Earners:")
    print(high_earners)

    # Group by age and calculate average salary
    avg_salary_by_age = df.groupby('age')['salary'].mean()
    print("\nAverage Salary by Age:")
    print(avg_salary_by_age)

    # Save to CSV
    df.to_csv('employees.csv', index=False)

    import matplotlib.pyplot as plt
    import numpy as np

    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Create a figure with two subplots
    plt.figure(figsize=(10, 5))

    # First subplot: Sine wave
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, color='blue', label='sin(x)')
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.grid(True)

    # Second subplot: Cosine wave
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, color='red', label='cos(x)')
    plt.title('Cosine Wave')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.legend()
    plt.grid(True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

    import matplotlib.pyplot as plt

    # 1. 讀取資料
    import os
    this_dir = os.path.dirname(__file__)
    csv_path = os.path.join(this_dir, 'sales_data.csv')
    df = pd.read_csv(csv_path)

    #df = pd.read_csv("sales_data.csv")# Your code here  # 讀取 sales_data.csv

    # 2. 新增 Total_Sales 欄位（Quantity × Price）
    df['Total_Sales'] = df['Quantity'] * df['Price']  # 計算每筆交易的總銷售額
    # 3. 按 Category 分組，計算總銷售額和總數量
    FIXME = 'Category'  # 替換為實際的類別欄位名稱

    category_summary = df.groupby(FIXME)[['Total_Sales', 'Quantity']].sum()  # 分組並計算總和
    print("類別總結：\n", category_summary)

    # 4. 找出銷售額最高的產品

    top_product = category_summary['Total_Sales'].idxmax()  # 找到銷售額最高的產品名稱
    top_sales = category_summary['Total_Sales'].max()  # 找到最高的銷售額

    print(f"銷售額最高的產品是: {top_product}，總銷售額: {top_sales}")

    # 5. 繪製柱狀圖：每個產品的總銷售額
    FIXME = 'Product'  # 替換為實際的產品欄位名稱
    plt.figure(figsize=(10, 5))  # 設定圖表大小
    product_sales = df.groupby(FIXME)['Total_Sales'].sum()  # 按產品分組計算總銷售額

    plt.bar(product_sales.index, product_sales.values, color='skyblue')  # 繪製柱狀圖
    plt.title('Total Sales by Product')  # 圖表標題
    plt.xlabel('Product')  # x 軸標籤
    plt.ylabel('Total Sales')  # y 軸標籤

    plt.savefig('sales_by_product.png')
    plt.show()

    # 6. 繪製折線圖：每天的總銷售額
    FIXME = 'Date'  # 替換為實際的日期欄位名稱
    daily_sales = df.groupby(FIXME)['Total_Sales'].sum()  # 按日期分組計算總銷售額
    plt.figure(figsize=(10,5))  # 設定圖表大小
    x = daily_sales.index  # 日期
    y = daily_sales.values  # 總銷售額

    plt.plot(x,y, marker='o', color='orange')  # 繪製折線圖
    plt.title("Total_Sales per day")  # 圖表標題

    plt.xlabel("Date")  # x 軸標籤

    plt.ylabel("Total Sales")  # y 軸標籤

    plt.xticks(rotation=45)  # 旋轉 x 軸標籤
    plt.savefig('daily_sales_trend.png')
    plt.show()