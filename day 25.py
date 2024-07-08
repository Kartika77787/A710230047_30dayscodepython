def display_menu():
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print(f"Tugas '{task}' telah ditambahkan.")

def view_tasks(tasks):
    if not tasks:
        print("Tidak ada tugas dalam daftar.")
    else:
        print("\nDaftar Tugas:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    if not tasks:
        print("Tidak ada tugas untuk dihapus.")
    else:
        view_tasks(tasks)
        try:
            task_num = int(input("Masukkan nomor tugas yang akan dihapus: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Tugas '{removed_task}' telah dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi daftar tugas.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 4.")

if __name__ == "__main__":
    main()
