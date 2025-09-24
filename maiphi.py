#tạo dictionary lưu thông   
ban_than = { "ten" : "phi",
             "tuoi" : 18,
             "so_thich" : "đá bóng"
}
print(ban_than)
# viết chương trình thêm một môn học và điểm
hoc_sinh = { "tên" : "phi", "lớp": "12a1"}
#thêm vào list
hoc_sinh["toán"] = 9 
print(hoc_sinh)
# cho distionary
diem = {"an": 8, "bình":9, "chi":7}
print("tên hs:", list(diem.keys())) 
tb = sum(diem.values()) / len(diem)
print(tb)
