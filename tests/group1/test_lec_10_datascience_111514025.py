import numpy as np
import matplotlib.pyplot as plt

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

def plot_regression(X, y, degrees, X_new):
    """绘制线性和多项式回归结果"""
    plt.scatter(X, y, color="blue", label="Data Points")

    # 线性回归
    theta_linear = fit_polynomial(X, y, degree=1)
    y_pred_linear = predict_polynomial(X_new, theta_linear, degree=1)
    plt.plot(X_new, y_pred_linear, color="red", label="Linear Fit")

    # 多项式回归
    for degree in degrees:
        theta_poly = fit_polynomial(X, y, degree)
        y_pred_poly = predict_polynomial(X_new, theta_poly, degree)
        plt.plot(X_new, y_pred_poly, label=f"Polynomial Fit (degree={degree})")

    # 图形设置
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Linear and Polynomial Regression")
    plt.legend()
    plt.show()

# 主函数
if __name__ == "__main__":
    X, y = generate_data()
    X_new = np.linspace(0, 10, 100).reshape(100, 1)
    plot_regression(X, y, degrees=[2, 10], X_new=X_new)


def test_generate_data():
    """测试数据生成"""
    X, y = generate_data(seed=42, num_samples=100)
    assert X.shape == (100, 1)
    assert len(y) == 100

def test_fit_polynomial():
    """测试多项式拟合"""
    X, y = generate_data(seed=42, num_samples=10)
    theta = fit_polynomial(X, y, degree=2)
    assert len(theta) == 3  # 二次多项式应该有 3 个参数

def test_predict_polynomial():
    """测试多项式预测"""
    X, y = generate_data(seed=42, num_samples=10)
    theta = fit_polynomial(X, y, degree=2)
    X_new = np.linspace(0, 10, 10).reshape(10, 1)
    y_pred = predict_polynomial(X_new, theta, degree=2)
    assert y_pred.shape == (10,)