"""
check_network.py —— 一键检查 GitHub 能不能连上

为什么用 Python 而不是 curl？
因为 Windows 自带的 TLS 组件（Schannel）在国内环境下经常出怪问题，
而 Python 自带独立的 OpenSSL，几乎不受影响。测网络用它最准。

运行：
    python check_network.py
"""

import socket
import sys
import urllib.error
import urllib.request

PROXY_CANDIDATES = [
    ("http://127.0.0.1:7890", "Clash / ikun 常用端口"),
    ("http://127.0.0.1:7891", "Clash socks 混合端口"),
    ("http://127.0.0.1:10809", "v2rayN 常用端口"),
    ("http://127.0.0.1:1080", "通用 SOCKS/HTTP 端口"),
]

TARGETS = [
    ("https://api.github.com/zen", "GitHub API"),
    ("https://github.com", "GitHub 网站"),
    ("https://raw.githubusercontent.com/git/git/master/README.md", "GitHub 原始文件"),
]


def port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        return s.connect_ex(("127.0.0.1", port)) == 0


def try_fetch(url: str, proxy: str | None) -> tuple[bool, str]:
    """返回 (是否成功, 说明)"""
    handlers = []
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    else:
        handlers.append(urllib.request.ProxyHandler({}))  # 强制直连

    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, headers={"User-Agent": "connectivity-check"})
    try:
        with opener.open(req, timeout=15) as r:
            body = r.read(400).decode("utf-8", "ignore").strip()
            return True, f"HTTP {r.status}  内容: {body[:50]!r}"
    except urllib.error.HTTPError as e:
        return True, f"HTTP {e.code}（能连上，只是这个地址返回了错误码）"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def main() -> int:
    print("=" * 60)
    print("  GitHub 连通性检查")
    print("=" * 60)

    # 第一步：找代理
    print("\n[1] 查找本地代理端口")
    found_proxy = None
    for url, note in PROXY_CANDIDATES:
        port = int(url.rsplit(":", 1)[1])
        ok = port_open(port)
        print(f"    {url:<28} {'开着' if ok else '关闭'}   ({note})")
        if ok and found_proxy is None:
            found_proxy = url

    if found_proxy:
        print(f"\n    -> 使用代理: {found_proxy}")
    else:
        print("\n    -> 没有发现任何代理端口。")
        print("       如果 GitHub 连不上，请打开 VPN / 代理软件。")

    # 第二步：试着连
    print("\n[2] 测试连接")
    results = {}

    print("    直连（不走代理）:")
    for url, name in TARGETS:
        ok, msg = try_fetch(url, None)
        results[("直连", name)] = ok
        print(f"      {'OK  ' if ok else '失败'} {name:<20} {msg[:60]}")

    if found_proxy:
        print(f"\n    走代理 {found_proxy}:")
        for url, name in TARGETS:
            ok, msg = try_fetch(url, found_proxy)
            results[("代理", name)] = ok
            print(f"      {'OK  ' if ok else '失败'} {name:<20} {msg[:60]}")

    # 第三步：结论
    print("\n" + "=" * 60)
    proxy_ok = any(v for k, v in results.items() if k[0] == "代理")
    direct_ok = any(v for k, v in results.items() if k[0] == "直连")

    if proxy_ok:
        print("  结论：通了。可以开始用 GitHub。")
        print("  如果浏览器还是打不开，那是浏览器没走代理：")
        print("    - 关掉浏览器重新打开（代理设置改了要重启浏览器才生效）")
        print("    - 或者看浏览器有没有装 SwitchyOmega 之类的插件，关掉它")
        code = 0
    elif direct_ok:
        print("  结论：直连就能通，不需要代理。")
        code = 0
    else:
        print("  结论：不通。请按顺序检查：")
        print("    1. VPN / 代理软件是否真的在运行")
        print("    2. 软件里「系统代理」开关是否打开")
        print("    3. 节点是否选了一个能用的（换个节点试试）")
        print("    4. 订阅是否到期 / 流量是否用尽")
        print("    5. 打开软件里的「日志」，看有没有报错")
        code = 1

    print("=" * 60)
    return code


if __name__ == "__main__":
    sys.exit(main())
