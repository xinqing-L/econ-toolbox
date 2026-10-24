"""
hello_econ.py —— 你的第一个经济学小工具

零依赖：只用 Python 标准库，不需要 pip install 任何东西。

运行：
    python hello_econ.py

它做五件经济学里天天用的事：
    1. 复利终值        future_value
    2. 现值折算        present_value
    3. 年化增长率      cagr
    4. 通胀后的实际值  real_value
    5. 一元线性回归    ols_simple      <- 计量经济学的第一块砖
"""


# ---------- 1. 货币的时间价值 ----------

def future_value(pv: float, rate: float, years: float) -> float:
    """复利终值：今天的 pv 元，按年利率 rate 复利滚 years 年后是多少钱。"""
    return pv * (1 + rate) ** years


def present_value(fv: float, rate: float, years: float) -> float:
    """现值：years 年后的 fv 元，在年利率 rate 下相当于今天多少钱。"""
    return fv / (1 + rate) ** years


def real_value(nominal: float, inflation: float, years: float) -> float:
    """实际购买力：名义金额 nominal 经过 years 年、年通胀 inflation 后，
    相当于今天的多少钱。这是「名义 vs 实际」这一经济学核心区分的代码版。"""
    return nominal / (1 + inflation) ** years


def cagr(begin: float, end: float, years: float) -> float:
    """复合年均增长率（Compound Annual Growth Rate）。
    注意：它不是 (end-begin)/begin/years —— 那个是算术平均，会高估。"""
    if begin <= 0:
        raise ValueError("期初值必须为正数")
    if years <= 0:
        raise ValueError("年数必须为正数")
    return (end / begin) ** (1 / years) - 1


def doubling_time(rate: float) -> tuple[float, float]:
    """翻倍需要多少年。返回 (精确值, 72法则估计值)。
    72 法则：年增长率 r% 时，翻倍约需 72/r 年。经济学面试常问。"""
    if rate <= 0:
        raise ValueError("增长率必须为正数")
    import math
    exact = math.log(2) / math.log(1 + rate)
    return exact, 72 / (rate * 100)


# ---------- 2. 一元线性回归 ----------

def ols_simple(xs: list[float], ys: list[float]) -> dict:
    """最简单的最小二乘回归：y = alpha + beta * x + 误差

    返回 alpha（截距）、beta（斜率）、r2（拟合优度）、n（样本量）。

    经济学里 beta 就是我们最想要的那个数，比如「多读一年书，工资高多少」。
    记住一句话：这里算出来的 beta 只是相关性，不等于因果性。
    要谈因果，得上学识里的「识别策略」——工具变量、双重差分、断点回归。
    """
    n = len(xs)
    if n != len(ys):
        raise ValueError("xs 和 ys 的长度必须相同")
    if n < 2:
        raise ValueError("至少需要 2 个观测值")

    mx = sum(xs) / n
    my = sum(ys) / n

    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0:
        raise ValueError("x 没有任何变化，斜率无法估计")

    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))

    beta = sxy / sxx
    alpha = my - beta * mx

    ss_res = sum((y - (alpha + beta * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")

    return {"alpha": alpha, "beta": beta, "r2": r2, "n": n}


# ---------- 3. 演示 ----------

def main() -> None:
    print("=" * 58)
    print("  hello_econ.py —— 经济学小工具演示")
    print("=" * 58)

    # 1. 复利
    pv, rate, years = 10000, 0.07, 30
    fv = future_value(pv, rate, years)
    print(f"\n【1】复利：{pv:,.0f} 元，年化 {rate:.0%}，{years} 年后")
    print(f"     终值 = {fv:,.2f} 元，是本金 {fv / pv:.1f} 倍")
    exact, rule72 = doubling_time(rate)
    print(f"     翻倍时间：精确 {exact:.2f} 年 / 72法则估 {rule72:.2f} 年")

    # 2. 现值
    print(f"\n【2】现值：{fv:,.2f} 元在 {years} 年后，贴现率 {rate:.0%}")
    print(f"     现值 = {present_value(fv, rate, years):,.2f} 元（回到起点，验证正确）")

    # 3. 通胀
    nominal, infl, yrs = 1_000_000, 0.03, 20
    real = real_value(nominal, infl, yrs)
    print(f"\n【3】通胀：{nominal:,.0f} 元，{yrs} 年后，年通胀 {infl:.0%}")
    print(f"     实际购买力 = {real:,.2f} 元（缩水 {(1 - real / nominal):.1%}）")

    # 4. CAGR
    print("\n【4】CAGR：2010 年 1000 亿 → 2020 年 2600 亿")
    g = cagr(1000, 2600, 10)
    print(f"     年均复合增长率 = {g:.2%}")
    print(f"     如果用算术平均会误算成 {(2600 - 1000) / 1000 / 10:.2%}（高估了）")

    # 5. 回归
    edu = [9, 12, 12, 15, 16, 16, 19, 19, 12, 15, 16, 18, 9, 11, 14]
    wage = [4200, 6500, 7000, 9000, 11000, 10500, 14000,
            15500, 6800, 8800, 9800, 12500, 3900, 5200, 7600]
    res = ols_simple(edu, wage)
    print(f"\n【5】回归：教育年限 -> 月薪（n = {res['n']}，模拟数据）")
    print(f"     回归方程：月薪 = {res['alpha']:,.0f} + {res['beta']:,.0f} × 教育年限")
    print(f"     R^2 = {res['r2']:.3f}")
    print(f"     解读：多读一年书，平均月薪高约 {res['beta']:,.0f} 元")
    print("     注意：这只是相关关系，不是因果关系。")

    print("\n" + "=" * 58)
    print("  跑通了。接下来打开 START_HERE.md，把这个文件夹变成仓库。")
    print("=" * 58)


if __name__ == "__main__":
    main()
