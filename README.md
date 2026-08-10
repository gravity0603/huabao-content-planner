# 华为画报内容策划助手

[![Version](https://img.shields.io/badge/version-v6.0.1-2f6f6d.svg)](CHANGELOG.md) [![Structure](https://img.shields.io/badge/structure-single--source-2f6f6d.svg)](SKILL.md)

> 面向华为杂志锁屏运营的内容策划 Skill：从最新素材和数据出发，完成选题、来源核验、概念去重、双目标评分和出街前审核。

当前版本：**v6.0.1**（2026-08-10）

## 能力总览

| 工作模式 | 输入 | 产出 |
|----------|------|------|
| 批量选题 | 品类、数量、方向、最新素材 | 候选卡、标题、副标题、落地页、信息源、自检报告 |
| 内容审核 | 标题、锁屏文案、落地页或图片 Brief | 通过/不通过/需补证、命中规则和修改建议 |
| 数据与知识库更新 | 周数据、月报、审核反馈 | 更新后的规则、品类方法和版本记录 |

**核心流程**：最近新增素材优先 → 原文验证 → 概念级去重 → P/月报双目标评分 → 内容包输出。

## 本次结构调整

v6.0.0/v6.0.1 将仓库改为单一真源结构，并补充最近新增素材优先读取规则，解决旧版本中多份 `SKILL.md`、知识库和打包副本互相漂移的问题：

- 根目录只有一个运行入口：`SKILL.md`
- 业务知识统一放在 `references/knowledge-base.md`
- 明星/影视/动漫专题放在 `references/star-movie-anime-methodology.md`
- 随 Skill 分发的源账号样例放在 `assets/source-accounts.csv`
- `README.md` 只负责安装和维护说明，不复制 Skill 正文
- 删除旧的 `skills/`、`workspace-files/` 安装镜像和过期 standalone prompt

## 目录

```text
huabao-content-planner/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── assets/
│   └── source-accounts.csv
└── references/
    ├── knowledge-base.md
    └── star-movie-anime-methodology.md
```

`SKILL.md` 控制任务路由和执行顺序；参考文件按场景读取。不要把完整知识库再次复制到其他目录。

## 安装

### Proma / Claude Code

将整个仓库目录放入工作区的 `skills/` 目录，保持目录名为 `huabao-content-planner`。运行时会读取：

```text
skills/huabao-content-planner/SKILL.md
```

### 其他 AI 工具

推荐使用支持外部参考文件的系统提示词配置，并同时提供：

- `SKILL.md`
- `references/knowledge-base.md`
- `references/star-movie-anime-methodology.md`（处理对应品类时）
- 用户当前的素材库和已做标题表

仓库不再维护一份容易过期的 standalone prompt。若目标工具不能读取参考文件，应先将需要的章节按任务临时合并，不要把合并结果提交回仓库。

## 使用

```text
给我 10 个旅行类选题，侧重反常识和强画面
检查这个选题：标题 xxx，副标题 xxx，落地页 xxx
根据本周 P 数据，找出动物类高表现标题结构
我有一份新月报，请更新知识库
```

批量策划时，Skill 会先读取相关规则和最新数据，按素材库链接的添加时间倒序优先读取最近新增素材，优先检索对应源账号，建立临时候选卡，完成来源核验、概念级去重和双目标评分，再输出标题、副标题、落地页、来源与自检报告。不要求维护额外运营表。

## 外部数据

仓库中的 `assets/source-accounts.csv` 是分发用的源账号样例，不代表用户当前最新数据。实际工作优先读取用户授权目录中的最新文件：

- `D:\yiyouliao working\工作内容\每周数据`
- `D:\yiyouliao working\工作内容\参考文件\华为画报月报`
- 用户在当前会话提供的素材库、已做标题和上传标题表

## 维护规则

1. 规则和数据只写入 `references/knowledge-base.md` 的对应章节。
2. 明星/影视/动漫的独立数据专题写入 `references/star-movie-anime-methodology.md`。
3. 运行流程、触发条件和输出契约只写入根 `SKILL.md`。
4. 安装、目录和版本说明只写入 `README.md`；历史变更写入 `CHANGELOG.md`。
5. 修改根 `SKILL.md` 时同步更新版本号和 README；提交前检查仓库内只有一个 `SKILL.md` 和一个主知识库。
6. 不创建 `skills/`、`workspace-files/` 或 `package/` 下的镜像副本。

## 质量底线

- 标题硬上限 10 字，副标题硬上限 25 字；性能目标通常为 7-9 字，具体按品类数据调整。
- 每个成品选题必须有可点击的信息源链接；搜索摘要不能标记为已验证。
- 先做概念级去重，再做标题生成；标题不同不代表选题不同。
- 素材库检索按链接添加时间倒序优先；没有明确日期字段时，按文件后出现的记录近似判断新增顺序，不伪造精确时间。

## 版本历史

详见 [`CHANGELOG.md`](CHANGELOG.md)。
