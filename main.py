import json
import os

tasks = []

def save_tasks():
    try:
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"ไม่สามารถบันทึกไฟล์ได้: {e}")

def load_tasks():
    global tasks
    if not os.path.exists("tasks.json"):
        tasks = []
        return
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except Exception as e:
        print(f"ไม่สามารถโหลดไฟล์ได้: {e}")
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
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return
    print("รายการงานทั้งหมด:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        due = t.get("due_date") or "-"
        title = t.get("title") or "(ไม่มีชื่อ)"
        print(f"{idx}. {title}  | วันครบกำหนด: {due}  | สถานะ: {status}")
    pass

def update_task():
    if not tasks:
        print("ไม่มีงานให้แก้ไข")
        return
    print("รายการงาน:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        print(f"{idx}. [{status}] {t.get('title')} (ID: {t.get('id')})")
    sel = input("เลือกลำดับของงานที่ต้องการแก้ไข (เลข): ").strip()
    if not sel.isdigit():
        print("ดัชนีต้องเป็นตัวเลข")
        return
    idx = int(sel) - 1
    if idx < 0 or idx >= len(tasks):
        print("ดัชนีไม่ถูกต้อง")
        return
    task = tasks[idx]
    print(f"แก้ไขงาน: {task.get('title')} (ID: {task.get('id')})")
    new_title = input(f"ชื่อเรื่องใหม่ (ปล่อยว่างเพื่อไม่เปลี่ยน) [{task.get('title')}]: ").strip()
    new_description = input(f"รายละเอียดใหม่ (ปล่อยว่างเพื่อไม่เปลี่ยน) [{task.get('description')}]: ").strip()
    cur_completed = "y" if task.get("completed") else "n"
    new_completed = input(f"สถานะเสร็จแล้ว? (y/n, ปล่อยว่างเพื่อไม่เปลี่ยน) [{cur_completed}]: ").strip().lower()

    if new_title:
        task["title"] = new_title
    if new_description:
        task["description"] = new_description
    if new_completed == "y":
        task["completed"] = True
    elif new_completed == "n":
        task["completed"] = False

    print("อัปเดตงานเรียบร้อย")

def edit_task():
    # kept for compatibility (empty)
    pass

def delete_task():
    if not tasks:
        print("ไม่มีงานให้ลบ")
        return
    print("รายการงาน:")
    for idx, t in enumerate(tasks, start=1):
        status = "เสร็จแล้ว" if t.get("completed") else "ยังไม่เสร็จ"
        due = t.get("due_date") or "-"
        title = t.get("title") or "(ไม่มีชื่อ)"
        print(f"{idx}. {title}  | วันครบกำหนด: {due}  | สถานะ: {status}")
    sel = input("เลือกลำดับของงานที่ต้องการลบ (เลข): ").strip()
    if not sel.isdigit():
        print("ดัชนีต้องเป็นตัวเลข")
        return
    idx = int(sel) - 1
    if idx < 0 or idx >= len(tasks):
        print("ดัชนีไม่ถูกต้อง")
        return
    task = tasks[idx]
    print(f"งานที่เลือก: {task.get('title')} (ID: {task.get('id')})")
    confirm = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
    if confirm == "y":
        tasks.pop(idx)
        print("ลบงานเรียบร้อย")
    else:
        print("ยกเลิกการลบ")

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
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("ออกจากโปรแกรม")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

if __name__ == "__main__":
    load_tasks()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nยกเลิกโดยผู้ใช้")
    finally:
        save_tasks()
