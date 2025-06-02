import numpy as np

def generate_data(seed=42, num_samples=100):
    """生成示例数据"""
    np.random.seed(seed)
    X = np.random.rand(num_samples, 1) * 10  # 特征
    y = 3 * X.squeeze() + 5 + np.random.randn(num_samples) * 2  # 带噪声的目标值
    return X, y

def fit_polynomial(X, y, degree):
    """拟合多项式回归模型"""
    X_poly = np.hstack([X**i for i in range(1, degree + 1)])
    X_poly_b = np.c_[np.ones((X_poly.shape[0], 1)), X_poly]  # 添加偏置项
    theta_poly = np.linalg.inv(X_poly_b.T.dot(X_poly_b)).dot(X_poly_b.T).dot(y)
    return theta_poly

def predict_polynomial(X, theta, degree):
    """使用多项式模型进行预测"""
    X_poly = np.hstack([X**i for i in range(1, degree + 1)])
    X_poly_b = np.c_[np.ones((X_poly.shape[0], 1)), X_poly]
    return X_poly_b.dot(theta)

def calculate_mse(y_true, y_pred):
    """计算均方误差 (MSE)"""
    mse = np.mean((y_true - y_pred) ** 2)
    return mse

# 主函数
if __name__ == "__main__":
    X, y = generate_data()

    # 测试不同多项式拟合的均方误差
    degrees = [1, 2, 10]  # 不同的多项式阶数
    for degree in degrees:
        theta = fit_polynomial(X, y, degree)
        y_pred = predict_polynomial(X, theta, degree)
        mse = calculate_mse(y, y_pred)
        print(f"Degree {degree}: Mean Squared Error (MSE) = {mse:.2f}")

# import numpy as np
# from test_lec_10_datascience_111514025v2 import (
#     generate_data,
#     fit_polynomial,
#     predict_polynomial,
#     calculate_mse,
# )

def test_mse_for_different_degrees():
    """测试不同多项式拟合方式的均方误差"""
    X, y = generate_data(seed=42, num_samples=100)
    degrees = [1, 2, 3, 5]
    previous_mse = float('inf')  # 初始化为无穷大
    for degree in degrees:
        theta = fit_polynomial(X, y, degree)
        y_pred = predict_polynomial(X, theta, degree)
        mse = calculate_mse(y, y_pred)
        assert mse >= 0  # MSE 应该为非负值
        assert mse <= previous_mse  # 随着阶数增加，MSE 应该逐渐减小或保持不变
        previous_mse = mse