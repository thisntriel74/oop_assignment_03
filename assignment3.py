# /************************************/
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# /************************************/

class Employee:
    
    def __init__(self, emp_id="UNKNOWN", full_name="Unnamed employee", base_salary=0.0): 
        if not emp_id or not full_name:
            raise ValueError("Mã nhân sự và Họ tên không được rỗng!")
        if base_salary < 0:
            raise ValueError("Lương cơ bản không được âm!")
            
        self.id = emp_id
        self.full_name = full_name
        self.base_salary = float(base_salary)

    def increase_salary(self, value, by_percentage=False):
        if value <= 0:
            return
        if by_percentage:
            self.base_salary += self.base_salary * (value / 100)
        else:
            self.base_salary += value

    def calculate_monthly_cost(self):
        return self.base_salary

    def display_info(self):
        print(f"[{self.id}] {self.full_name} | Lương CB: {self.base_salary:,.0f} VNĐ")

    def __del__(self):
        pass


class SoftwareEngineer(Employee):
    
    def __init__(self, emp_id="UNKNOWN", full_name="Unnamed employee", base_salary=0.0, primary_language="C++", tech_allowance=0.0):
        # super() gọi hàm khởi tạo của lớp cha (Employee) để xử lý Mã, Tên, Lương
        super().__init__(emp_id, full_name, base_salary)
        
        if not primary_language:
            raise ValueError("Ngôn ngữ lập trình chính không được rỗng!")
        if tech_allowance < 0:
            raise ValueError("Phụ cấp không được âm!")
            
        self.primary_language = primary_language
        self.tech_allowance = float(tech_allowance)

    def calculate_monthly_cost(self):
        return self.base_salary + self.tech_allowance

    def display_info(self):
        print(f"[{self.id}] {self.full_name} (Dev {self.primary_language}) | Lương: {self.base_salary:,.0f} | Phụ cấp: {self.tech_allowance:,.0f}")

    def __del__(self):
        pass


class ProjectTeam:
    
    def __init__(self, project_code, project_name, leader=None):
        self.project_code = project_code
        self.project_name = project_name
        
        self.leader = None
        self.members = []
        
        if leader:
            self.add_member(leader, make_leader=True)

    def add_member(self, employee, make_leader=False):
        if not self.contains(employee.id):
            self.members.append(employee)
            
        if make_leader:
            self.leader = employee
        return True

    def remove_member(self, employee_id):
        if self.leader and self.leader.id == employee_id:
            print(f"Từ chối: Không thể xóa trưởng nhóm {employee_id} khi chưa chọn người thay thế.")
            return False
        
        for i, emp in enumerate(self.members):
            if emp.id == employee_id:
                del self.members[i]
                return True
        return False

    def change_leader(self, employee):
        if not self.contains(employee.id):
            self.add_member(employee)
        self.leader = employee

    def contains(self, employee_id):
        return any(emp.id == employee_id for emp in self.members)

    def calculate_total_monthly_cost(self):
        return sum(emp.calculate_monthly_cost() for emp in self.members)

    def display_team(self):
        print(f"\n--- DỰ ÁN: {self.project_code} - {self.project_name} ---")
        if self.leader:
            print(f"Trưởng nhóm: {self.leader.full_name}")
        else:
            print("Trưởng nhóm: Chưa có")
        
        print(f"Danh sách thành viên ({len(self.members)} người):")
        for emp in self.members:
            emp.display_info()
        print(f"Tổng chi phí dự án: {self.calculate_total_monthly_cost():,.0f} VNĐ")

    def __del__(self):
        self.members.clear()


if __name__ == "__main__":
    # --- KIỂM THỬ KỊCH BẢN ---
    
    # Tạo hai Emp bằng hai constructor khác nhau
    emp1 = Employee()
    emp2 = Employee("NV02", "Nguyen Van A", 10000000)

    # Tạo hai SoftwareEngineer bằng hai constructor khác nhau
    dev1 = SoftwareEngineer("DEV01", "Tran Van B", 15000000)
    dev2 = SoftwareEngineer("DEV02", "Le Thi C", 20000000, "Python", 5000000)

    # Tăng lương một nhân sự bằng tiền cố định
    emp2.increase_salary(2000000)

    # Tăng lương một nhân sự khác theo phần trăm
    dev2.increase_salary(10, by_percentage=True)

    # Tạo nhóm dự án không có leader
    team1 = ProjectTeam("P01", "Website A")

    # Thêm một nhân sự vào bằng addMember
    team1.add_member(emp2)

    # Thêm một kĩ sư để đặt làm leader
    team1.add_member(dev1, make_leader=True)

    # Thử thêm lại một thành viên đã tồn tại
    team1.add_member(emp2)

    # Hiển thị danh sách đa hình
    team1.display_team()

    # Tính tổng chi phí nhân sự hằng tháng
    print(f"\n[KẾT QUẢ] Tổng chi phí nhân sự hằng tháng: {team1.calculate_total_monthly_cost():,.0f} VNĐ")

    # Thử xóa trưởng nhóm hiện tại
    print("\n[THAO TÁC] Thử xóa trưởng nhóm hiện tại (DEV01):")
    team1.remove_member("DEV01")

    # Đổi trưởng nhóm sang DEV02 và xóa trưởng nhóm cũ DEV01
    team1.change_leader(dev2)
    team1.remove_member("DEV01")
    team1.display_team()
    
    # Tạo một nhóm thứ hai và thêm một nhân sự đã có ở nhóm thứ nhất
    team2 = ProjectTeam("P02", "App B")
    team2.add_member(emp2)

    # Hủy nhóm thứ hai bằng lệnh del
    del team2

    # Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại sau khi hủy nhóm
    print("\n[KẾT QUẢ] Kiểm tra sự tồn tại của nhân sự NV02 sau khi nhóm 2 bị hủy:")
    emp2.display_info()