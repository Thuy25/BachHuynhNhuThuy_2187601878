def truy_cap_phan_tu(tuple_data):
    first_el = tuple_data[0]
    last_el = tuple_data[-1]
    return first_el, last_el
input_tuple = eval(input("Nhap tuple, vi du (1 ,2 ,3): "))
first, last = truy_cap_phan_tu(input_tuple)
print ("phan tu dau tien: ", first)
print ("phan tu cuoi: ", last)