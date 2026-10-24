# Git 命令速查表

> 不用背。忘了就回来查。**只需记住 5 个命令就能干活。**

---

## 核心 5 个命令（背这 5 个就够）

```powershell
git status              # 我现在是什么状态？（最常用，随便敲，只读不破坏）
git add .               # 把改动放进「待提交区」
git commit -m "说明"    # 存档，附一句话说明
git pull                # 把云端的更新拉下来
git push                # 把我的提交推到云端
```

**日常工作流 = `status` → `add` → `commit` → `push`**

---

## 一、开始

| 命令 | 作用 |
| --- | --- |
| `git init` | 把当前文件夹变成 Git 仓库（只需一次） |
| `git clone <网址>` | 把云端的仓库完整下载到本地 |
| `git clone <网址> 新名字` | 下载并改名 |

---

## 二、看状态（安全，随便敲）

| 命令 | 作用 |
| --- | --- |
| `git status` | 哪些文件改了、哪些没被追踪 |
| `git status -s` | 精简版 |
| `git diff` | 具体改了哪几行（红绿显示） |
| `git diff --staged` | 看已经 `add` 的改动 |
| `git log --oneline -10` | 最近 10 次提交，一行一条 |
| `git log --oneline --graph` | 带分支图的历史 |
| `git show <提交号>` | 看某次提交改了什么 |
| `git remote -v` | 我的云端地址是什么 |

---

## 三、提交

```powershell
git add 文件名           # 只提交某个文件
git add .                # 提交所有改动
git add *.py             # 提交所有 py 文件
git commit -m "说明"     # 存档
git commit -am "说明"    # add + commit 二合一（只对已追踪的文件有效）
```

### commit message 怎么写

```
✅ 好的写法：
   修复回归表第三列的标签错误
   加入 2010-2020 省级面板数据清洗脚本
   把图 2 换成灰色调（期刊要求）

❌ 差的写法：
   update
   改了一下
   fix
   asdf
```

**判断标准**：半年后的你能不能看懂这次改了什么。

---

## 四、和云端同步

| 命令 | 作用 |
| --- | --- |
| `git push` | 推上去 |
| `git push -u origin main` | 第一次推送，并记住对应关系 |
| `git pull` | 拉下来并合并 |
| `git pull --rebase` | 拉下来，把我的提交排到后面（历史更干净） |
| `git remote add origin <网址>` | 关联云端仓库 |
| `git remote set-url origin <新网址>` | 换云端地址 |

### 报错 `rejected / fetch first`

意思是云端有你本地没有的提交。解决：

```powershell
git pull --rebase
git push
```

---

## 五、撤销（救命命令）

| 场景 | 命令 |
| --- | --- |
| 改坏了文件，想恢复到上次提交 | `git restore 文件名` |
| 改坏了所有文件 | `git restore .` |
| 已经 `add` 了，想撤回暂存 | `git restore --staged 文件名` |
| 想撤销最近一次提交但保留改动 | `git reset --soft HEAD~1` |
| 想彻底丢弃最近一次提交 | `git reset --hard HEAD~1` ⚠️ 危险 |
| 想看看某个文件以前的样子 | `git show HEAD~1:文件名` |

> ⚠️ `--hard` 会永久丢掉未提交的改动。用之前先 `git status` 确认。

---

## 六、分支

| 命令 | 作用 |
| --- | --- |
| `git branch` | 列出本地分支 |
| `git branch -a` | 列出所有分支（含远程） |
| `git switch -c 新分支名` | 新建并切换（新写法） |
| `git switch 分支名` | 切换 |
| `git branch -M main` | 把当前分支改名为 main |
| `git merge 分支名` | 把某分支合并进当前分支 |
| `git branch -d 分支名` | 删除已合并的分支 |

**新手用分支的场景**：想大改但怕搞坏 → 开个分支折腾，成功了再合并，失败了直接删。

---

## 七、忽略文件

`.gitignore` 的语法：

```gitignore
# 注释
*.csv           # 所有 csv
!small.csv      # 除了这个
data/           # 整个目录
**/temp/        # 任意层级的 temp 目录
```

**规则**：已经被提交过的文件，后来加进 `.gitignore` 也**不会**被移除。要先：

```powershell
git rm --cached 文件名
```

---

## 八、配置

```powershell
# 必配
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 强烈建议
git config --global core.quotepath false     # 中文文件名不乱码
git config --global init.defaultBranch main  # 默认分支名
git config --global core.autocrlf true       # Windows 换行符

# 代理（开了 VPN 但 git 不走系统代理时）
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 关掉代理
git config --global --unset http.proxy
git config --global --unset https.proxy

# 查看所有配置
git config --global --list
```

---

## 九、报错急救

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `not a git repository` | 不在仓库目录里 | `cd` 到项目文件夹 |
| `Please tell me who you are` | 没配 user.name/email | 跑第八节的两条命令 |
| `Authentication failed` | 用了密码 | 用浏览器授权或 Personal Access Token |
| `rejected / fetch first` | 云端更新了 | `git pull --rebase` 再 push |
| `CONFLICT (content)` | 两边改了同一行 | 打开文件手动改，删掉 `<<<<<<<` 标记，再 `add` + `commit` |
| `fatal: remote origin already exists` | 已经关联过 | `git remote set-url origin <新网址>` |
| `Filename too long` | Windows 路径长度限制 | `git config --global core.longpaths true` |
| 中文文件名乱码 | quotepath | `git config --global core.quotepath false` |
| 控制台中文乱码 | 编码不是 UTF-8 | `chcp 65001` |

---

## 十、一条真理

> **拿不准的时候，先敲 `git status`。**
> 它只读不写，永远不会把东西搞坏，而且几乎总是能告诉你下一步该干嘛。
