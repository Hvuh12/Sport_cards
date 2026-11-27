HVCARDS V1.6 — Advanced Collection & Performance

CẬP NHẬT
1. Giải nén ZIP. Tại thư mục gốc repo Sport_cards, upload index.html, cards.json và nguyên folder thumbnails/.
2. assets/ là bản nhận diện V1.5 được đính kèm để dự phòng; giữ bản trên GitHub nếu đã upload.
3. Giữ nguyên SportCards/ — ảnh JPG gốc không bị thay đổi. Không upload cả thư mục HVCARDS_V1.6 bao ngoài.
4. Commit changes, mở lại web và Ctrl+F5. Kiểm tra DevTools > Network > Img với cùng viewport và Disable cache.

DỮ LIỆU
- Giữ 19 card, giá, trạng thái, tên, hãng, mùa thẻ và các thông tin featured do bạn cung cấp.
- Rio: /99, The Rising Star; tagline cập nhật cho đồng nhất.
- team: đội/CLB trên card, không phải đội hiện tại của cầu thủ. Fabinho chưa xác định rõ nên để Unspecified. Kiểm tra lại team/type nếu cần.
- type: danh sách tag (có thể nhiều tag). Other dùng khi chưa đủ thông tin.
- id: mã cố định; không đổi sau khi chia sẻ link. Link auto cũ vẫn hoạt động nếu đường dẫn ảnh cũ được giữ nguyên. Có thể thêm aliases nếu đổi ảnh.
- Sửa Mo-Salah-01-back.jpg thành Mo-Salah-Back-01.jpg theo file thực tế trong RAR.
- Rhys Williams và Dominik Szoboszlai: RAR thiếu ảnh mặt sau nên đã bỏ thuộc tính back để tránh nút ảnh lỗi. Nếu GitHub vẫn có ảnh đó, thêm lại back đúng đường dẫn. Florian Wirtz vốn không có back.
- Mức giá min/max chỉ áp dụng cho card FOR SALE bằng VND.
- Sold Archive là chế độ lọc riêng trong Explore Collection; ALL vẫn giữ toàn bộ 19 card.

THÊM CARD MỚI
- Tiếp tục thêm ảnh vào SportCards/ và khai báo img, back (nếu có), name, price, sport, brand, season, id, team, type, dateAdded trong cards.json.
- Tạo thumbnail cùng basename với ảnh mặt trước, đuôi .webp trong thumbnails/. Không bắt buộc khai báo thumbnail nếu dùng cấu trúc chuẩn. Nếu không có ảnh thumbnail, web sẽ thử tải JPG gốc.
- Để tự động tạo: đặt create_thumbnails.py cạnh cards.json trong bản repo trên máy tính, chạy python -m pip install Pillow, sau đó python create_thumbnails.py. Upload folder thumbnails/ và cards.json mới. Không cần upload script lên web.

KIỂM THỬ
- JavaScript syntax, JSON, đường dẫn ảnh trong RAR, 19 ID, 19 thumbnail đã kiểm tra.
- Chromium DOM với dữ liệu cục bộ: 5 bộ lọc, tìm kiếm, reset, archive, related cards, popup và chiều rộng 360px đã chạy qua.
- Trình duyệt môi trường thử nghiệm chặn truy cập URL, nên chưa xác nhận request network thực tế, clipboard hoặc direct link trên GitHub Pages. Chưa stress test 20 người.
