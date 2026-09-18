# 自动展开论文链接

Python 脚本要求 Python 3.9 或更高版本，不需要安装第三方依赖。启动后，在任意 Markdown 文件中粘贴一行论文网页 URL：

```markdown
https://arxiv.org/abs/2402.15852
```

保存后会自动替换为：

```markdown
- **NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation** & Jiazhao Zhang,  He Wang & **RSS 2024** & [Arxiv](https://arxiv.org/abs/2402.15852)
```

使用 Python 持续监听整个仓库：

```powershell
python scripts/watch_paper_links.py
```

只扫描一次后退出：

```powershell
python scripts/watch_paper_links.py --once
```

也可以使用 Node.js 版本：

```powershell
node scripts/watch-paper-links.mjs
```

Node.js 只扫描一次后退出：

```powershell
node scripts/watch-paper-links.mjs --once
```

使用 `--dry-run` 可以只预览结果。为了避免误改正文、表格或已有链接，只有“整行只有 URL”（前面可以有 `-`）时才会触发。脚本优先支持 arXiv，也支持带有标准 `citation_*` 元数据的 OpenReview、CVF 等论文页面。

Python 版本不会输出完整作者列表：一至两位作者会保留，三位及以上只保留第一作者和末位作者。不同作者之间使用逗号分隔；单个姓名内部不使用逗号，如果网页元数据写成 `Zhang, Jiazhao`，脚本会输出为 `Jiazhao Zhang`。由于 arXiv 和多数论文网页通常不提供结构化的通讯作者标记，脚本将末位作者作为通讯作者的最佳近似；如果网页上的作者顺序不遵循这一惯例，仍需手动修正。

会议或期刊信息只在网页明确提供且脚本能够识别时填写。没有明确会议/期刊信息时，会议字段统一写作 `Arxiv`，不会用提交年份推测会议。

运行 Python 单元测试：

```powershell
python -m unittest discover -s scripts -p "test_watch_paper_links.py" -v
```
