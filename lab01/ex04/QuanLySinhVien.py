from SinhVien import SinhVien
class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            if self.listSinhVien:
                 maxId = self.listSinhVien[0]._id 
                 for sv in self.listSinhVien:
                    if sv._id > maxId:
                        maxId = sv._id
                 maxId += 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if sv is not None:
            print(f"--- Cap nhat thong tin cho sinh vien ID: {ID} ---")
            name = input(f"Nhap ten moi (hien tai: {sv._name}): ") or sv._name
            sex = input(f"Nhap gioi tinh moi (hien tai: {sv._sex}): ") or sv._sex
            major = input(f"Nhap chuyen nganh moi (hien tai: {sv._major}): ") or sv._major 
            try:
                diemTB_str = input(f"Nhap diem TB moi (hien tai: {sv._diemTB}): ")
                diemTB = float(diemTB_str) if diemTB_str else sv._diemTB
            except ValueError:
                print("Diem TB khong hop le, giu nguyen gia tri cu.")
                diemTB = sv._diemTB

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cap nhat sinh vien thanh cong!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == ID:
                    searchResult = sv
                    break 
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB > 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("\n--- DANH SACH SINH VIEN ---")
        header = "{:<8} {:<18} {:<8} {:<15} {:<10} {:<10}".format(
            "ID", "Ho Ten", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc")
        print(header)
        print("-" * len(header))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<15} {:<10.2f} {:<10}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Khong co sinh vien nao trong danh sach.")
        print("-" * len(header))
        print("\n") 

    def getListSinhVien(self):
        return self.listSinhVien


if __name__ == "__main__":
    qlsv = QuanLySinhVien()

    sv1 = SinhVien(id=qlsv.generateID(), name="Nguyen Van A", sex="Nam", major="CNTT", diemTB=8.5)
    qlsv.xepLoaiHocLuc(sv1)
    qlsv.listSinhVien.append(sv1)

    sv2 = SinhVien(id=qlsv.generateID(), name="Tran Thi B", sex="Nu", major="Kinh Te", diemTB=7.0)
    qlsv.xepLoaiHocLuc(sv2)
    qlsv.listSinhVien.append(sv2)
    
    sv3 = SinhVien(id=qlsv.generateID(), name="Le Van C", sex="Nam", major="CNTT", diemTB=5.5)
    qlsv.xepLoaiHocLuc(sv3)
    qlsv.listSinhVien.append(sv3)

    sv4 = SinhVien(id=qlsv.generateID(), name="Pham Thi D", sex="Nu", major="Ngon Ngu Anh", diemTB=4.0)
    qlsv.xepLoaiHocLuc(sv4)
    qlsv.listSinhVien.append(sv4)

    print("Danh sach sinh vien ban dau:")
    qlsv.showSinhVien(qlsv.getListSinhVien())

    print("Nhap them sinh vien moi:")
    qlsv.nhapSinhVien() 
    
    print("Danh sach sinh vien sau khi them:")
    qlsv.showSinhVien(qlsv.getListSinhVien())
    
    print("Sap xep theo ten:")
    qlsv.sortByName()
    qlsv.showSinhVien(qlsv.getListSinhVien())

    print("Sap xep theo diem trung binh:")
    qlsv.sortByDiemTB()
    qlsv.showSinhVien(qlsv.getListSinhVien())

    print("Tim sinh vien theo ten 'Van':")
    found_by_name = qlsv.findByName("Van")
    qlsv.showSinhVien(found_by_name)
    
    id_to_update = 2
    print(f"Cap nhat sinh vien co ID = {id_to_update}:")
    qlsv.updateSinhVien(id_to_update) 
    qlsv.showSinhVien(qlsv.getListSinhVien())

    id_to_delete = 1
    print(f"Xoa sinh vien co ID = {id_to_delete}:")
    if qlsv.deleteByID(id_to_delete):
        print(f"Da xoa sinh vien ID {id_to_delete}.")
    else:
        print(f"Khong tim thay sinh vien ID {id_to_delete} de xoa.")
    qlsv.showSinhVien(qlsv.getListSinhVien())