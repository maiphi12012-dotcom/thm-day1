# mật khẩu đúng
# bước 1 đặt mật khẩu
mat_khau_dung = input(" nhập mk: ")
# buớc 2 nhập số lần giới hạn
so_lan_sai = 0
gioi_han = 5
while so_lan_sai < gioi_han:
    mk = input("nhập mk đăng nhập: ")
    if mk == mat_khau_dung:
        print(" đăng nhập thành công")
        break
    else:
        so_lan_sai += 1
        print(" sai mật khẩu", gioi_han - so_lan_sai)
if so_lan_sai == gioi_han:
    print("ban đăng nhập sai nhiều ! tài khoản khoá>")
