import qrcode

def tao_qr_gg_drive(link_drive, ten_file_anh):
    # Cấu hình chi tiết cho mã QR
    qr = qrcode.QRCode(
        version=1, # Độ phức tạp của ma trận (1-40), để 1 là tự động
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Mức độ sửa lỗi cao (H = High)
        box_size=10, # Kích thước mỗi ô vuông nhỏ (pixel)
        border=4,    # Độ dày viền trắng bao quanh (mặc định là 4)
    )
    
    # Thêm dữ liệu (link) vào QR
    qr.add_data(link_drive)
    qr.make(fit=True)

    # Tạo hình ảnh (có thể đổi màu ở đây)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Lưu file
    img.save(ten_file_anh)
    print(f"✅ Thành công! Mã QR đã được lưu với tên: {ten_file_anh}")

# --- PHẦN NHẬP THÔNG TIN CỦA BẠN ---

# 1. Dán link Google Drive của bạn vào giữa hai dấu ngoặc kép dưới đây:
my_link = "https://docs.google.com/presentation/d/1h7ILBCqNOZHWIMztkNmYt9-MJOgyd06f/edit?usp=sharing&ouid=108556581633741514397&rtpof=true&sd=true" 

# 2. Đặt tên cho file ảnh QR (đuôi .png):
ten_file = "TaiLieuPowerpoint.png"

# 3. Chạy hàm
if __name__ == "__main__":
    tao_qr_gg_drive(my_link, ten_file)