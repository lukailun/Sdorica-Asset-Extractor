# Sdorica 资源提取器

一个用于从 Unity Asset Bundle (.ab) 文件中提取资源的 Python 工具，专为 Sdorica 游戏资源设计。此提取器专注于角色立绘资源，支持单文件和批量处理。

## 资源路径

Android/data/com.ilongyuan.sdorica.longyuan/files/AssetBundles

## 功能特性

- **智能资源过滤**：自动提取名称以 "figure" 结尾的资源
- **多种资源类型**：支持 Texture2D、Sprite、AudioClip 和 TextAsset 提取
- **批量处理**：一次性处理整个目录中的 .ab 文件
- **自动生成输出**：自动创建有序的输出目录
- **冲突预防**：添加资源包名称前缀以防止文件名冲突
- **递归搜索**：在批量处理期间查找子目录中的 .ab 文件

## 系统要求

- Python 3.6 或更高版本
- UnityPy 库

## 安装

1. 克隆或下载此仓库
2. 安装必需的依赖项：

```bash
pip install UnityPy
```

## 使用方法

提取器支持两种模式：单文件提取和批量目录处理。

### 命令行语法

```bash
python sdorica_asset_extractor.py <输入路径>
```

### 单文件模式

从单个 .ab 文件提取资源：

```bash
python sdorica_asset_extractor.py /path/to/bundle.ab
```

**输出**：在输入文件的同一位置创建名为 `<文件名>_extracted` 的目录。

### 批量目录模式

从目录中的所有 .ab 文件提取资源：

```bash
python sdorica_asset_extractor.py /path/to/Sdorica/
```

**输出**：在输入目录的同一级别创建名为 `<目录名>_extracted` 的目录。

## 使用示例

### 从单个资源包文件提取
```bash
python sdorica_asset_extractor.py character_alice.ab
# 创建：character_alice_extracted/
```

### 从游戏目录批量提取
```bash
python sdorica_asset_extractor.py /Games/Sdorica/AssetBundles/
# 创建：/Games/Sdorica/AssetBundles_extracted/
```

## 支持的资源类型

| 资源类型 | 输出格式 | 描述 |
|----------|----------|------|
| Texture2D | .png | 纹理图像 |
| Sprite | .png | 精灵图像 |
| AudioClip | .wav | 音频文件 |
| TextAsset | .txt | 文本/脚本文件 |

## 输出结构

所有提取的资源都按以下命名约定保存：
```
<资源包名称>_<资源名称>.<扩展名>
```

例如：
- `character_alice_alice_figure.png`
- `weapon_sword_sword_figure.png`

## 资源过滤

提取器专门查找名称以 "figure" 结尾的资源。此过滤功能旨在从 Sdorica 资源包中提取角色和物品立绘，同时忽略其他游戏资源。

## 错误处理

- **文件缺失**：工具会报告是否找不到资源包文件
- **损坏的资源包**：单个资源包错误不会停止批量处理
- **资源提取错误**：失败的资源提取会被记录，但不会停止处理过程
- **权限问题**：确保您对输入文件有读取权限，对输出目录有写入权限

## 故障排除

### 常见问题

1. **"找不到 .ab 文件"**
   - 确保目录包含 .ab 文件
   - 检查文件扩展名是否确切为 ".ab"（在某些系统上区分大小写）

2. **"找不到资源包文件"**
   - 验证文件路径是否正确
   - 确保您对该文件有读取权限

3. **"加载资源包时出错"**
   - .ab 文件可能已损坏或使用不支持的 Unity 版本
   - 尝试使用不同的资源包文件进行测试

4. **没有提取到资源**
   - 资源包可能不包含名称以 "figure" 结尾的资源
   - 检查控制台输出以获取处理详细信息

### 依赖项

如果遇到导入错误，请确保正确安装了 UnityPy：

```bash
pip install --upgrade UnityPy
```

## 开发

### 代码结构

- `extract_assets_from_bundle()`：处理单个资源包提取
- `batch_extract_from_directory()`：管理批量处理
- `main()`：命令行界面和路径处理

### 扩展工具

要修改资源过滤，请编辑提取循环中的条件：

```python
# 当前过滤器
if not name.endswith('figure'):
    continue

# 示例：提取所有资源
# if True:  # 移除过滤器
```

## 许可证

此工具按原样提供，仅供教育和个人使用。请尊重游戏开发者和发行商的知识产权。

## 贡献

欢迎提交问题和功能增强请求。贡献代码时，请确保与现有命令行界面的兼容性。 