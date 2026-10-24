# START HERE · 第一天怎么用 GitHub

> 你没有任何编程基础，这份文档就是为你写的。全程只有两条命令需要你敲，其余都是点点鼠标。

---

## 0. 先排除三个误解

| 误解 | 事实 |
| --- | --- |
| 「我得下载 GitHub」 | **不用。** GitHub 是一个网站。要装的是 Git（一个命令行工具）和可选的 GitHub Desktop（图形界面）。 |
| 「没学过编程用不了」 | **能用了。** 第一周你完全可以只用它「看别人 + 下载别人的东西」，一行代码都不写。 |
| 「Git 和 GitHub 是一个东西」 | **不是。** Git 装在你自己电脑上，管本地文件的版本；GitHub 是云端网站，管协作和分享。 |

### 一个比喻，记住就不乱了

- **Git = 游戏存档系统。** 你每打一关就存一次档（commit），玩崩了可以读档回去，还能开平行存档（branch）。
- **GitHub = 存档的云盘 + 玩家社区。** 把存档传上去（push），换台电脑能接着玩（clone），别人也能看你的存档、提意见（Issue）、改建自己的版本（Fork）。

**你现在电脑上的状态（我已经查过了）**

| 组件 | 状态 |
| --- | --- |
| Git | ✅ 已装，版本 2.55.0 |
| Python | ✅ 已装，3.14.6 |
| VS Code | ✅ 已装 |
| GitHub Desktop | ❌ 没装（可选，建议装） |
| GitHub 网络 | ❌ **直连不通，需要开代理** |

---

## 1. 第一件事：开代理

我实测过你的网络：

```
https://github.com          → 失败（TLS 连接被重置）
https://api.github.com      → 失败
https://raw.githubusercontent.com → 失败
```

TCP 端口能握手，但 HTTPS 一来就被掐断，这是很典型的**被干扰**现象。
而你系统里已经存了代理地址 `127.0.0.1:7890`，但 `ProxyEnable = 0` —— 说明代理软件没在跑，或者没开「系统代理」。

**所以：去 ikun 把 VPN 打开，选一个节点，确认「系统代理」是开的状态。**

开好后在 PowerShell 里跑这一句验证：

```powershell
curl.exe -I -m 10 https://github.com
```

看到 `HTTP/1.1 200 OK` 或 `HTTP/2 200` 就通了。

> 💡 替代方案（不想开 VPN 时）：
> - **Gitee（码云）**：国内版 GitHub，能当练习场，但生态和资源远不如 GitHub
> - **镜像加速**：只适合下载，不适合学习流程
> - **pip 用清华源**：`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
>
> 说实话：**学 GitHub 就老老实实开代理**，镜像会让你学歪。

---

## 2. 注册账号（10 分钟）

打开 <https://github.com/signup>

**用户名怎么取？很重要，因为以后会出现在简历、论文代码链接、求职邮件里。**

- ✅ 好：`zhangsan-econ`、`san.zhang`、`zs-econ`
- ❌ 差：`xiaoming2003`、`asdfgh123`（以后想改要重新积累关注度）

然后：

1. **邮箱**用你常用的（学校邮箱最好，能申请 GitHub Student Pack，白拿一堆付费服务）
2. **务必开 2FA**（Settings → Password and authentication）——不开的话你 push 代码会被强制要求
3. **传个头像**
4. 建一个和你用户名同名的仓库，里面写个 `README.md`——它会显示在你的主页上，叫 Profile README，效果很专业

---

## 3. 第一天只做「只读」操作（不碰代码）

这一天的目标不是写代码，是**看懂一个仓库的页面**。

### 3.1 找一个仓库逛逛

随便打开一个，比如 <https://github.com/pandas-dev/pandas>

你要认得的 6 个区域：

| 区域 | 意思 |
| --- | --- |
| **README** | 项目说明书。页面往下滚就是。九成问题在这里有答案 |
| **Code 标签页** | 所有文件的列表。这就是「仓库」的本质：一个文件夹 |
| **Star ⭐** | 收藏/点赞。你的 Star 列表就是你的资源库 |
| **Watch** | 订阅，有更新通知你 |
| **Fork** | 复制一份到你自己账号下，随便改，不影响原项目 |
| **Issues** | 别人报的 bug 和提的需求。**读 Issues 是学东西最快的路径** |

### 3.2 两种下载方式的区别

| 方式 | 操作 | 适用 |
| --- | --- | --- |
| **Download ZIP** | 绿色 `Code` 按钮 → Download ZIP | 只想看看、跑一次。缺点：没历史记录，不能更新 |
| **git clone** | 命令行 `git clone 网址` | 正经用法。能拉更新、能提交、能切分支 |

对经济学数据项目，**一定要 clone 而不是下 ZIP**——因为论文的数据/代码会更新，你要能拉取最新版。

### 3.3 怎么读 README 才不浪费时间

按顺序找这四块：

1. **一句话简介**（最顶上那一行）——这是不是我要的？
2. **Installation** ——怎么装
3. **Quickstart / Usage** ——复制那段示例代码直接跑
4. **Citation / 引用** ——学术项目如果有这个，说明是真项目不是玩具

---

## 4. 配 Git 身份（现在就能做，不需要网络）

打开 PowerShell，逐条粘贴。**把引号里的内容换成你自己的。**

```powershell
git config --global user.name "你的名字或昵称"
git config --global user.email "你的GitHub邮箱"
```

为什么不配不行：**每一次提交都要记录「谁改的」**，没配就 commit 不了。

再配 4 个必改项，每条我都解释：

```powershell
# 让中文文件名正常显示，而不是 \346\226\207 这种乱码
git config --global core.quotepath false

# 新仓库默认分支叫 main（GitHub 的默认，跟 master 有别）
git config --global init.defaultBranch main

# Windows 换行符自动转换，避免和 Mac/Linux 用户互相打架
git config --global core.autocrlf true
```

验证一下：

```powershell
git config --global --list
```

---

## 5. 装 GitHub Desktop（强烈建议，省掉 90% 的痛苦）

下载：<https://desktop.github.com>（需要代理）

为什么对你特别有用：

- **不用背命令**，改了什么文件一眼看到，勾选就提交
- **push 时自动弹浏览器登录**，不用折腾 Token
- 把「哪个文件改了什么」用红绿颜色画出来，对新手理解 Git 极有帮助

> 你 VS Code 里也有内置的源代码管理面板（左侧第三个图标），功能类似。
> **建议：先用 GitHub Desktop 建立直觉，再慢慢过渡到命令行。**

---

## 6. 第一次完整流程：把这个文件夹变成你的仓库

假设你已经开好代理。在 PowerShell 里执行（**一行一行来，看懂每行在干嘛**）：

```powershell
# 进入项目文件夹
cd "C:\Users\20235\Documents\deepseek-harness\默认工作区\github-starter"

# 1. 初始化：把这个普通文件夹变成一个 Git 仓库
#    此刻会多出一个隐藏的 .git 文件夹，所有历史都在里面
git init

# 2. 看看当前状态：哪些文件没被追踪
git status

# 3. 把文件放进「待提交区」（暂存区）
git add .

# 4. 真正存档：给这次修改写一句话说明
git commit -m "第一次提交：经济学小工具和入门笔记"

# 5. 确认改名成功（应该显示 main）
git branch -M main
```

到这一步，**东西已经在你的电脑上存档了**，还没上网。

接下来在网页上建仓库：<https://github.com/new>

- Repository name：`econ-toolbox`（或任何你喜欢的）
- **不要勾** Add a README / .gitignore / license（勾了会和你本地的冲突）

然后在 PowerShell 里：

```powershell
# 6. 告诉本地仓库：云端在哪
git remote add origin https://github.com/你的用户名/econ-toolbox.git

# 7. 推上去（第一次会弹浏览器让你登录授权）
git push -u origin main
```

`-u` 的意思是「记住这个对应关系」，以后只要敲 `git push` 就行。

**看到 `branch 'main' set up to track 'origin/main'` 就成功了。** 刷新网页，你的代码在上面了。

---

## 7. 认证：别再用密码了

GitHub 2021 年就取消了密码推送。三种方式：

| 方式 | 难度 | 建议 |
| --- | --- | --- |
| 浏览器弹窗授权（Git Credential Manager） | ⭐ | **就用这个**，Windows 上 Git 装好就自带了 |
| Personal Access Token | ⭐⭐ | 弹出输入密码时，密码栏填 Token |
| SSH Key | ⭐⭐⭐ | 熟练之后再弄 |

如果 `git push` 弹出要你输入密码，去 <https://github.com/settings/tokens> 生成一个 Token（勾 `repo` 权限），把它当密码用。

---

## 8. 新手必踩的 6 个坑

1. **把 Excel 数据文件传上去了** → 大文件永久留在历史里，删都删不干净。**先写 `.gitignore`**（本项目已经写好了）。万一手滑，搜 `git filter-repo`。
2. **中文文件名显示成 `\346\226\207`** → 跑一次 `git config --global core.quotepath false`。
3. **`git push` 报 `rejected` / `fetch first`** → 云端有你本地没有的提交。先 `git pull --rebase` 再 push。
4. **`fatal: not a git repository`** → 你没在项目文件夹里，`cd` 过去。
5. **把 API Key / 密码提交上去了** → 立刻去那个网站**吊销 Key**，光删文件没用，历史里还在。
6. **分支叫 `master` 但云端是 `main`** → `git branch -M main` 再推。

---

## 9. 你的进度清单

- [ ] 代理打开，`curl -I https://github.com` 返回 200
- [ ] 注册账号 + 开 2FA + 传头像
- [ ] 建 Profile README
- [ ] `git config` 五条配好
- [ ] 装 GitHub Desktop
- [ ] `python hello_econ.py` 跑通
- [ ] `git init` → `commit` → `push` 走完一遍
- [ ] 在网页上看到自己的文件

全打勾之后，打开 **`ECON_ROADMAP.md`**，开始把它用起来。
