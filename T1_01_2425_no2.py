class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambahAntrian(self, nama):
        node = Node(nama)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def layaniAntrian(self):
        if not self.head:
            return "Antrian Kosong"
        node = self.head
        self.head = self.head.next
        return node.nama
    
    def lihatAntrian(self):
        if (not self.isempty()):
            temp = self.head
            while temp:
                print(temp.nama, end=" -> ")
                temp = temp.next
        else:
            print("Antrian Kosong")

    def isempty(self):
        return not self.head

if __name__ == "__main__":
    daftarReg = LinkedList()
    daftarVIP = LinkedList()

    print("MENU")
    pil=0
    vip=0

    daftarVIP.tambahAntrian('a1')
    daftarVIP.tambahAntrian('a2')
    daftarVIP.tambahAntrian('a3')
    daftarReg.tambahAntrian('b1')
    daftarReg.tambahAntrian('b2')
    daftarReg.tambahAntrian('b3')
    daftarReg.tambahAntrian('b4')
    daftarReg.tambahAntrian('b5')

    while (pil != '4'):
        print("1. Tambah Pasien")
        print("2. Layani Pasien")
        print("3. Lihat Antrian")
        print("4. Keluar")
        print()
        pil = input("Masukkan pilihan : ")
        if pil=='1':
            nama = input("Masukkan Nama : ")
            vipreg = input("VIP(1) / Regular(0) : ")
            if (vipreg=='1'):
                daftarVIP.tambahAntrian(nama)
            elif (vipreg=='0'):
                daftarReg.tambahAntrian(nama)
        elif pil=='2':
            if (vip<2):
                if (not daftarVIP.isempty()):
                    print(f"{daftarVIP.layaniAntrian()} (VIP)")
                    vip+=1
                else:
                    if (not daftarReg.isempty()):
                        print(f"{daftarReg.layaniAntrian()} (REG)")
                    else:
                        print("Antrian Kosong")
            else:
                if (not daftarReg.isempty()):
                    print(f"{daftarReg.layaniAntrian()} (REG)")
                else:
                    print("Antrian Kosong")
                vip=0
        elif pil=='3':
            print ("Daftar VIP :", end="")
            print(daftarVIP.lihatAntrian())
            print ("Daftar REG :", end="")
            print(daftarReg.lihatAntrian())
        elif pil == '4':
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

