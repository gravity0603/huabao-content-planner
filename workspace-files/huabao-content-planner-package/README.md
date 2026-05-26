# 华为杂志锁屏内容策划助手 - 分享包

## 包含文件

| 文件 | 用途 |
|------|------|
| `SKILL.md` | Skill 定义文件，用于 Proma / Claude Code |
| `huabao-knowledge-base.md` | 知识库，含全部规则、数据、案例 |
| `standalone-prompt.md` | 合体通用版，**可直接粘贴到任何 AI 工具使用** |

---

## 安装方式

### 方式一：Proma 工作区（推荐）

1. 将 `SKILL.md` 复制到你的 Proma 工作区 `skills/huabao-content-planner/SKILL.md`
2. 将 `huabao-knowledge-base.md` 复制到 `workspace-files/.context/huabao-knowledge-base.md`
3. 重启或刷新会话，skill 自动加载
4. 使用：直接对话 `/huabao-content-planner 给我10个美食选题`

### 方式二：Claude Code

1. 将本目录放到 `~/.claude/skills/huabao-content-planner/`
2. Claude Code 启动后自动识别
3. 使用同上

### 方式三：通用 AI 工具（GPT / Dify / Coze / 豆包 / Kimi 等）

1. 打开 `standalone-prompt.md`
2. 复制全部内容
3. 粘贴到 AI 工具的「系统提示词 / Instructions / 人设」设置中
4. 或者直接粘贴到对话开头，然后输入你的需求

---

## 快速上手

```
给我10个{品类}类选题，侧重{方向}
```

示例：
- `给我10个美食类选题，侧重冷知识和猎奇`
- `给我5个插画类选题，侧重互动猜谜，匹配Emoji猜谜专栏`
- `检查这个选题：标题"xxx" 文案"xxx"`

---

## 知识库更新

收到华为新月报后：
1. 将月报 PDF/MD 放入对话
2. 说「更新知识库，这是 X 月月报」
3. Skill 会自动提取新规则、案例、数据追加

---

## 版本

v1.5.0 — 2026-05-20
