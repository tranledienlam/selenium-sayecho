# AUTOMATION SAYECHO với Selenium Python

## ⚠ Lưu ý quan trọng

🔴 **Dự án này có chứa code hint.** Vui lòng tìm đến **bài ghim** trong kênh [Telegram Channel](https://t.me/+8o9ebAT9ZSFlZGNl) để kiểm tra trước khi sử dụng.

---

## 📖 Mục lục
1. [Giới thiệu](#-giới-thiệu)
2. [Video demo](#-video-demo)
3. [Chức năng chính](#-chức-năng-chính)
4. [Yêu cầu ban đầu](#-yêu-cầu-ban-đầu)
5. [Cấu trúc file](#-cấu-trúc-file)
6. [Hướng dẫn cài đặt](#-hướng-dẫn-cài-đặt)
7. [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
8. [Tùy chỉnh cấu hình](#-tùy-chỉnh-cấu-hình)
9. [Thông tin liên hệ](#-thông-tin-liên-hệ)

## 🔔 Bật thông báo để theo dõi mã nguồn khi có update

1. Đăng nhập vào GitHub.
2. Nhấn vào biểu tượng 🔔 **Watch** (góc trên bên phải của repository này).
3. Chọn **"All Activity"** để nhận tất cả thông báo hoặc **"Custom" > "Pull Requests"** để nhận thông báo khi có thay đổi trong mã nguồn.

---

## 🌐 Giới thiệu

**AUTOMATION SAYECHO** là tool tự động check-in hằng ngày.

📌 **Trang dự án**: [Harpie.io](https://www.sayecho.xyz)

<p align="center">
    <img src="intro.png" alt="Giới thiệu">
</p>

---

## 🎬 Video demo

<p align="center">
    <a href="https://www.youtube.com/watch?v=GJn3SSoGSK8">
        <img src="https://img.youtube.com/vi/GJn3SSoGSK8/0.jpg" alt="Xem video demo">
    </a>
</p>

---


## 🚀 Chức năng chính

- **Quét ví (Scan Wallet)**: Tự động check-in hằng ngày.

---

## 🔧 Yêu cầu ban đầu

- **X**: Đăng nhập tài khoản X.
- **sayecho**: Đăng nhập tài khoản acho với passkeys.

---

## 📂 Cấu trúc file

| File                           | Mô tả                                    |
| ------------------------------ | ---------------------------------------- |
| `browser_automation.py`        | Code tự động hóa trình duyệt.            |
| `utils.py`                     | Các hàm hỗ trợ chung.                    |
| `sayecho.py`                   | Chương trình chính thực hiện automation. |
| `requirements.txt`             | Danh sách các thư viện cần thiết.        |
| `intro.png`                    | Danh sách các thư viện cần thiết.        |

---

## 📌 Hướng dẫn cài đặt

### 1️ Tạo file `data.txt`

- Mỗi dòng chứa thông tin một profile theo cấu trúc:
  ```plaintext
  [tên_profile]
  ```
- Ví dụ:
  ```plaintext
  profile1
  profile2
  ```

### 2️ (Tùy chọn) Tạo file `token_tele.txt`

- Lưu **Telegram Bot Token** để chương trình gửi thông báo lỗi qua Telegram khi gặp sự cố.
- Nếu không có file này, ảnh lỗi sẽ lưu vào thư mục **snapshot**.

### 3️ Cài đặt Python & thư viện

Trước tiên, cần cài đặt Python (phiên bản 3.8 trở lên). Nếu chưa có, hãy tải và cài đặt từ [Python Official Site](https://www.python.org/downloads/).

- Kiểm tra phiên bản Python bằng lệnh:
  ```sh
  python --version
  ```
- Cài đặt thư viện yêu cầu:
  ```sh
  pip install -r requirements.txt
  ```

---

## ▶ Hướng dẫn sử dụng

### 1️ Chạy chương trình

```sh
python sayecho.py
```

### 2️ Các chế độ hoạt động

- **1. Set up**: Chạy chế độ cài đặt ban đầu và chọn profile.
- **2. Chạy Auto**: Chạy chế độ tự động theo cấu hình đã thiết lập.
- **3. Thoát**: Dừng chương trình.

**💡 Lưu ý:**

- **Lần đầu:** Chạy **Set up (1)** để thiết lập cấu hình ví, thực hiện như trong video.
- **Những lần sau:** Chạy **Auto (2)** để thực hiện automation.

---

## ⚙ Tùy chỉnh cấu hình

Mở **`sayecho.py`** và tìm dòng sau:

### 🔹 **Bật chế độ Auto không cần chọn menu**

```python
manager.run_terminal(
    profiles=PROFILES,
    auto=False,
    max_concurrent_profiles=4
)
```

Đổi `auto=False` thành `auto=True`:

```python
manager.run_terminal(
    profiles=PROFILES,
    auto=True,
    max_concurrent_profiles=4
)
```

### 🔹 **Thay đổi số lượng profile chạy cùng lúc**

Đổi số `4` thành số bất kì

```python
max_concurrent_profiles=4  
```

---

## 🔗 Thông tin liên hệ

📢 **Telegram Channel:** [Airdrop Automation](https://t.me/+8o9ebAT9ZSFlZGNl)

💰 **Ủng hộ tác giả:**

- **EVM:** `0x3b3784f7b0fed3a8ecdd46c80097a781a6afdb09`
- **SOL:** `4z3JQNeTnMSHYeg9FjRmXYrQrPHBnPg3zNKisAJjobSP`
- **TON:** `UQDKgC6TesJJU9TilGYoZfj5YYtIzePhdzSDJTctJ-Z27lkR`
- **SUI:** `0x5fb56584bf561a4a0889e35a96ef3e6595c7ebd13294be436ad61eaf04be4b09`
- **APT (APTOS):** `0x557ea46189398da1ddf817a634fa91cfb54a32cfc22cadd98bb0327c880bac19`

🙏 Nếu ủng hộ, vui lòng gửi token chính của mạng đó. Cảm ơn anh em đã hỗ trợ!

