以下是为你的下载代码编写的 `README.md` 文件，包含中英文版本：

---

# Telegram Sticker Downloader

This Python script allows you to download all stickers from a specified Telegram sticker set. The stickers are downloaded in `.webp` format and saved in a local directory named after the sticker set.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.6+
- `requests` library
- `python-telegram-bot` library

You can install the required Python packages using `pip`:

```bash
pip install requests python-telegram-bot
pip install imageio moviepy pillow imageio[ffmpeg] imageio[pyav]
```

## Usage

1. **Set Your Bot Token:**

   Replace the `token` variable in the script with your bot's token obtained from BotFather.

2. **Specify the Sticker Set:**

   Replace the `sticker_set_name` variable with the name of the sticker set you want to download.

3. **Run the Script:**

   Simply run the script using Python:

   ```bash
   python download_stickers.py
   ```

4. **Downloaded Stickers:**

   The stickers will be saved in a folder named after the sticker set. The stickers are in `.webp` format.

## Example

If your bot token is `5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk` and the sticker set name is `niubiuniu_by_WuMingv2Bot`, the script will download all stickers from this set and save them in a folder named `niubiuniu_by_WuMingv2Bot`.

---

# Telegram Sticker Downloader（中文）

此Python脚本允许您从指定的Telegram贴纸包中下载所有贴纸。贴纸将以 `.webp` 格式下载，并保存在以贴纸包名称命名的本地目录中。

## 运行环境要求

在运行此脚本之前，请确保您已安装以下内容：

- Python 3.6+
- `requests` 库
- `python-telegram-bot` 库

您可以使用 `pip` 来安装所需的Python包：

```bash
pip install requests python-telegram-bot
pip install imageio moviepy pillow imageio[ffmpeg] imageio[pyav]
```

## 使用方法

1. **设置您的机器人令牌：**

   将脚本中的 `token` 变量替换为您从 BotFather 获得的机器人的令牌。

2. **指定贴纸包：**

   将 `sticker_set_name` 变量替换为您要下载的贴纸包的名称。

3. **运行脚本：**

   使用Python运行脚本：

   ```bash
   python download_stickers.py
   ```

4. **下载的贴纸：**

   贴纸将保存在以贴纸包名称命名的文件夹中，格式为 `.webp`。

## 示例

如果您的机器人令牌是 `5640863500:AAGgnofomUMC1zn9c8CmW5CnfJQhBtX7LUk`，贴纸包名称为 `niubiuniu_by_WuMingv2Bot`，则脚本将从该贴纸包中下载所有贴纸，并将其保存在名为 `niubiuniu_by_WuMingv2Bot` 的文件夹中。

---

这个 `README.md` 文件包含了如何设置和使用脚本的详细步骤，并用中英文两种语言进行了描述，便于不同语言的用户阅读和使用。