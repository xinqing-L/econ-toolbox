# GitHub 对经济学 / 量化分析到底有什么用

> 一句话回答你最初的问题：**有用，而且越来越是必需品。但它的用处和你想象的不太一样。**

---

## 一、为什么经济学特别依赖 GitHub

### 1. 学术界的「可复现性」要求已经成了硬规定

经济学是社会科学里最早强制要求共享代码的学科。

- **AEA（美国经济学会）** 从 2005 年起要求投稿论文提交数据与代码，2019 年后升级为 **AEA Data and Code Repository**，全部托管在 openICPSR 和 GitHub 上
- **《经济研究》《经济学（季刊）》** 等国内顶刊近年也在推数据与代码附件
- 你以后如果读研、写论文，**导师第一句话往往是「把代码放 GitHub 上」**

意思很直白：**只给结论不给代码的实证研究，现在发不出去。**

### 2. 你的「作品集」比成绩单更有说服力

经济学求职（尤其是量化、政策研究、咨询、数据岗）看三样：

| 项 | GitHub 上的呈现 |
| --- | --- |
| 会什么 | 你的仓库列表 = 技能树 |
| 做过什么 | 一个从抓数据到出图的完整项目 |
| 会不会沟通 | README 写得好不好 |

**一个干净的仓库 > 十张证书。**

### 3. 你会天天看到别人写的代码

GitHub 上有全世界经济学家的复现包。你想知道某个 DID 模型怎么实现、某个数据怎么清洗——**去看原作者的仓库，比看教科书快十倍。**

---

## 二、三条使用路线（按你的目标选）

### 路线 A：只当资料库（**第 1 天就能用**，0 代码）

- 搜关键词 → Star → 下载 ZIP / clone
- 读 README 和 Issues
- 关注几个大牛和组织

**收益**：找到别人整理好的数据、复现代码、教程。这一条已经足够让你比 90% 的同学强。

### 路线 B：用它管理自己的分析项目（**2–4 周**）

每个实证项目一个仓库，结构大概长这样：

```
my-paper/
├── README.md          # 项目说明：研究问题、数据来源、怎么跑
├── requirements.txt   # 依赖包版本（复现的关键）
├── data/
│   ├── raw/           # 原始数据，只读不改
│   └── processed/     # 清洗后数据
├── code/
│   ├── 01_clean.py
│   ├── 02_describe.py
│   └── 03_regress.py
├── output/
│   ├── tables/
│   └── figures/
└── paper/
    └── main.tex
```

**为什么这个结构重要**：一年后你自己回来，还能跑通。这就是「可复现」。

### 路线 C：做量化 / 参与开源（**1–3 个月**）

- 用别人的因子库、回测框架
- 给开源项目提 Issue、修文档、提 Pull Request
- 发自己的小工具包

---

## 三、具体推荐哪些仓库

> 名字记不准就直接把 `owner/repo` 粘到地址栏，或者在 GitHub 搜索框搜关键词。
> 这些我都会在你通网后帮你逐个验证。

### 📊 数据获取

| 仓库 / 工具 | 用途 |
| --- | --- |
| `mortada/fredapi` | 美联储 FRED 数据库的 Python 接口，宏观数据标配 |
| `talbano/wbgapi` | 世界银行 WDI 数据，跨国面板必备 |
| `akfamily/akshare` | **A股/国内宏观/期货数据，免费，国内直连不用代理** |
| `waditu/tushare` | 国内金融数据（部分要积分） |
| `ranaroussi/yfinance` | 雅虎财经行情 |
| `pandas-dev/pandas-datareader` | 一堆数据源的统一接口 |
| `owid/owid-catalog` | Our World in Data 的全量数据 |

### 📐 计量经济学 / 因果推断

| 仓库 | 用途 |
| --- | --- |
| `statsmodels/statsmodels` | Python 计量基础库，OLS/面板/时间序列 |
| `bashtage/linearmodels` | 面板数据、工具变量、系统 GMM —— **实证论文主力** |
| `py-econometrics/pyfixest` | 高维固定效应，对标 R 的 `fixest`，快 |
| `DoubleML/doubleml-for-py` | **双重机器学习**，因果推断前沿方法 |
| `py-why/EconML` | 微软的异质性处理效应估计 |
| `py-why/dowhy` | 因果图 + 因果推断框架 |
| `bashtage/arch` | GARCH 波动率模型 |

### 📈 量化金融 / 回测

| 仓库 | 用途 |
| --- | --- |
| `microsoft/qlib` | 微软的 AI 量化平台，**自带 A 股数据**，中文文档 |
| `mementum/backtrader` | 老牌回测框架，教程多 |
| `polakowo/vectorbt` | 向量化回测，速度极快 |
| `stefan-jansen/zipline-reloaded` | Zipline 的维护版 |
| `QuantConnect/Lean` | 机构级开源引擎，C#/Python |
| `ranaroussi/quantstats` | 一键生成回测业绩报告 |
| `OpenBB-finance/OpenBB` | 开源版彭博终端 |

### 📚 学习资源

| 资源 | 说明 |
| --- | --- |
| `QuantEcon/lecture-python` | **强烈推荐**。QuantEcon 的完整经济学计算课程，免费，从 Python 基础到动态规划 |
| `wesm/pydata-book` | 《利用 Python 进行数据分析》官方代码，pandas 作者写的 |
| `scunning1975/mixtape` | 《Causal Inference: The Mixtape》配套代码，因果推断入门神书 |
| `matteocourthoud/awesome-causal-inference` | 因果推断资源大全 |

> ⚠️ 提醒：仓库名可能随作者改名而变化。搜不到就用关键词搜，别死磕。

---

## 四、给你的 4 周计划（每天 30–45 分钟）

### 第 1 周：只读 + Git 基础

| 天 | 做什么 |
| --- | --- |
| 1–2 | 走完 `START_HERE.md`，把本项目推上 GitHub |
| 3 | 逛 5 个经济学相关仓库，Star 收藏，读 README |
| 4 | 学 `git status` / `diff` / `log` —— 三个命令看懂自己在干嘛 |
| 5 | 故意改坏一个文件，然后用 `git restore` 救回来（**这是最重要的练习**） |
| 6 | 装 GitHub Desktop，用图形界面重复一遍上面的操作 |
| 7 | 休息，或者看 QuantEcon 的第一讲 |

### 第 2 周：Python 数据分析

- 装 `pandas`、`matplotlib`：`pip install pandas matplotlib`
- 目标：**读一个 CSV、算描述统计、画三张图**
- 数据就用国家统计局的公开数据，或者 `akshare` 抓 A 股
- 每完成一步 commit 一次，commit message 写人话

### 第 3 周：一个真实的小项目

选题（挑一个，别贪多）：

- 「中国各省 GDP 增速的收敛性」—— 用世界银行或统计局数据
- 「A 股某行业的动量效应」—— 用 `akshare` + `vectorbt`
- 「教育回报率的 Mincer 方程」—— 用 CGSS/CHIP 公开数据，跑 OLS

要求：**有 README、有图、能一键跑通。** 就这一条，超越大部分人。

### 第 4 周：复现一篇论文

找一篇有公开代码的实证论文（AEA 期刊的 replication package 最好），
把它的表和图跑出来。**跑不通是常态，卡住就在 Issues 里搜或提问。**

复现成功那一刻，你对计量的理解会跳一个台阶。

---

## 五、几条真心建议

1. **一个烂尾的小项目 > 十个教程。** 教程给你幻觉，项目给你能力。
2. **commit 要小要勤。** 一次改一个东西，写清楚为什么改。别攒一个月再提交。
3. **README 是写给别人（和未来的自己）的。** 花 20 分钟写，回报十倍。
4. **别怕公开。** 早期代码丑是正常的，所有人都是。可以先建 private 仓库，成熟了再转 public。
5. **Issues 是最好的老师。** 你想问的问题，八成有人问过了。
6. **网络问题就开代理。** 别把时间浪费在折腾镜像上，那会把你学歪。

---

## 六、国内环境的两个实用配置

你用的是 Miniconda（装在 `C:\Users\20235\miniconda3 cn`），建议配国内源：

```powershell
# pip 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# git 走本地代理（如果开了代理但 git 不走系统代理）
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 关代理时记得清掉，否则断网
# git config --global --unset http.proxy
# git config --global --unset https.proxy
```

**注意**：端口 `7890` 是 Clash 系的默认值。你的软件具体端口去软件设置里看一眼，别照抄。
