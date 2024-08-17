# Telegram Sticker Downloader

This Python script allows you to download all stickers from a specified Telegram sticker set. The stickers are downloaded in `.webp` format and can be optionally converted to `.gif` format. The stickers are saved in local directories named after the sticker set.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.6+
- `requests` library
- `python-telegram-bot` library
- `imageio` library
- `moviepy` library
- `pillow` library
- `imageio[ffmpeg]` library
- `imageio[pyav]` library

You can install the required Python packages using `pip`:

```bash
pip install requests python-telegram-bot
pip install imageio moviepy pillow imageio[ffmpeg] imageio[pyav]
```

## Usage

1. **Set Your Bot Token:**

   Replace the `bot_token` variable in the script with your bot's token obtained from BotFather.

2. **Specify the Sticker Set:**

   You can either specify a single sticker set by replacing the `sticker_set_name` variable or process multiple sticker sets by providing a file with URLs to the sticker sets.

3. **Run the Script:**

   Simply run the script using Python:

   ```bash
   python download_and_convert.py
   ```

4. **Downloaded Stickers:**

   The stickers will be saved in a folder named after the sticker set in `.webp` format. If conversion is enabled, `.gif` versions of the stickers will be saved in a separate folder named `<sticker_set_name>_gifs`.

## Example

If your bot token is `5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk` and the sticker set name is `niubiuniu_by_WuMingv2Bot`, the script will download all stickers from this set, save them in a folder named `niubiuniu_by_WuMingv2Bot`, and convert them to `.gif` format in `niubiuniu_by_WuMingv2Bot_gifs`.

## Batch Processing

If you want to download and convert multiple sticker sets, create a text file with each line containing a URL to a sticker set. Then run the script, and it will process each set in sequence.

---

# Telegram Sticker Downloader（中文）

此Python脚本允许您从指定的Telegram贴纸包中下载所有贴纸。贴纸将以 `.webp` 格式下载，并可以选择转换为 `.gif` 格式。贴纸将保存在以贴纸包名称命名的本地目录中。

## 运行环境要求

在运行此脚本之前，请确保您已安装以下内容：

- Python 3.6+
- `requests` 库
- `python-telegram-bot` 库
- `imageio` 库
- `moviepy` 库
- `pillow` 库
- `imageio[ffmpeg]` 库
- `imageio[pyav]` 库

您可以使用 `pip` 来安装所需的Python包：

```bash
pip install requests python-telegram-bot
pip install imageio moviepy pillow imageio[ffmpeg] imageio[pyav]
```

## 使用方法

1. **设置您的机器人令牌：**

   将脚本中的 `bot_token` 变量替换为您从 BotFather 获得的机器人的令牌。

2. **指定贴纸包：**

   您可以通过替换 `sticker_set_name` 变量指定单个贴纸包，或通过提供包含贴纸包链接的文件批量处理多个贴纸包。

3. **运行脚本：**

   使用Python运行脚本：

   ```bash
   python download_and_convert.py
   ```

4. **下载的贴纸：**

   贴纸将保存在以贴纸包名称命名的文件夹中，格式为 `.webp`。如果启用转换，`.gif` 版本的贴纸将保存在名为 `<sticker_set_name>_gifs` 的单独文件夹中。

## 示例

如果您的机器人令牌是 `5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk`，贴纸包名称为 `biaoqing82`，则脚本将从该贴纸包中下载所有贴纸，并将其保存在名为 `biaoqing82` 的文件夹中，并将其转换为 `.gif` 格式，保存在 `biaoqing82_gifs` 文件夹中。

## 批量处理

如果您希望下载并转换多个贴纸包，可以使用文本文件[url.txt](url.txt)，其中每行包含一个贴纸包的链接。然后运行脚本，它将按顺序处理每个贴纸包。