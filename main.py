
tasks = []

def add_task():
    title = input("ชื่อเรื่อง: ").strip()
    description = input("รายละเอียด: ").strip()
    due_date = input("วันครบกำหนด (YYYY-MM-DD): ").strip()
    if tasks:
        new_id = max(t['id'] for t in tasks) + 1
    else:
        new_id = 1
    task = {
        "id": new_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print(f"เพิ่มงานเรียบร้อย ไอดี: {new_id}")

def view_tasks():
    # empty
    pass

def edit_task():
    # empty
    pass

def delete_task():
    # empty
    pass

def main_menu():
    while True:
        print("\nเมนูหลัก")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. แก้ไขงาน")
        print("4. ลบงาน")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกตัวเลือก (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    main_menu()
