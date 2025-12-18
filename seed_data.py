"""Seed script to populate dummy data for testing"""
import hashlib
import os
from models.database import session_scope, is_database_initialized
from models.models import (
    Division, Employee, Item, EmployeeItem, User, Log, ItemTransferHistory,
    EmployeeItemAttribute
)
from datetime import datetime, timedelta

def hash_password(password: str) -> str:
    """Hash password using SHA256 with salt"""
    salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + ":" + hashed

def seed_database():
    """Populate the database with dummy data"""
    
    # Check if data already exists
    with session_scope() as session:
        existing_users = session.query(User).count()
        if existing_users > 0:
            print("Database already has data. Skipping seed.")
            return
    
    with session_scope() as session:
        # Create Divisions
        divisions_data = [
            Division(name="IT Department"),
            Division(name="HR Department"),
            Division(name="Finance Department"),
            Division(name="Operations Department"),
        ]
        session.add_all(divisions_data)
        session.flush()
        
        # Create Users (for login)
        users_data = [
            User(username="admin", password=hash_password("admin123"), role="admin"),
            User(username="manager1", password=hash_password("manager123"), role="manager"),
            User(username="manager2", password=hash_password("manager123"), role="manager"),
        ]
        session.add_all(users_data)
        session.flush()
        
        # Create Employees
        employees_data = [
            Employee(emp_id="EMP001", name="John Doe", division_id=1, date_joined=datetime.now() - timedelta(days=365)),
            Employee(emp_id="EMP002", name="Jane Smith", division_id=1, date_joined=datetime.now() - timedelta(days=300)),
            Employee(emp_id="EMP003", name="Robert Johnson", division_id=2, date_joined=datetime.now() - timedelta(days=250)),
            Employee(emp_id="EMP004", name="Sarah Williams", division_id=2, date_joined=datetime.now() - timedelta(days=200)),
            Employee(emp_id="EMP005", name="Michael Brown", division_id=3, date_joined=datetime.now() - timedelta(days=180)),
            Employee(emp_id="EMP006", name="Emily Davis", division_id=3, date_joined=datetime.now() - timedelta(days=150)),
            Employee(emp_id="EMP007", name="David Miller", division_id=4, date_joined=datetime.now() - timedelta(days=120)),
            Employee(emp_id="EMP008", name="Lisa Anderson", division_id=4, date_joined=datetime.now() - timedelta(days=90)),
        ]
        session.add_all(employees_data)
        session.flush()
        
        # Create Items
        items_data = [
            Item(name="Laptop Dell XPS 13", last_assigned=datetime.now()),
            Item(name="Monitor LG 27 Inch", last_assigned=datetime.now()),
            Item(name="Keyboard Mechanical RGB", last_assigned=datetime.now()),
            Item(name="Mouse Logitech MX Master", last_assigned=datetime.now()),
            Item(name="USB-C Hub", last_assigned=datetime.now()),
            Item(name="Webcam Logitech C920", last_assigned=datetime.now()),
            Item(name="Headphones Sony WH1000XM4", last_assigned=datetime.now()),
            Item(name="Desk Chair Ergonomic", last_assigned=datetime.now()),
            Item(name="Standing Desk Electric", last_assigned=datetime.now()),
            Item(name="Monitor Arm Dual", last_assigned=datetime.now()),
            Item(name="Phone iPhone 14", last_assigned=datetime.now()),
            Item(name="Tablet iPad Pro", last_assigned=datetime.now()),
        ]
        session.add_all(items_data)
        session.flush()
        
        # Create EmployeeItem assignments
        employee_items_data = [
            EmployeeItem(emp_id="EMP001", item_id=1, unique_key="DELL-XPS-001", date_assigned=datetime.now() - timedelta(days=300), notes="Main work laptop"),
            EmployeeItem(emp_id="EMP001", item_id=2, unique_key="LG-MON-001", date_assigned=datetime.now() - timedelta(days=300), notes="Secondary monitor"),
            EmployeeItem(emp_id="EMP001", item_id=3, unique_key="KEY-RGB-001", date_assigned=datetime.now() - timedelta(days=200), notes="Mechanical keyboard"),
            EmployeeItem(emp_id="EMP002", item_id=1, unique_key="DELL-XPS-002", date_assigned=datetime.now() - timedelta(days=280), notes="Main work laptop"),
            EmployeeItem(emp_id="EMP002", item_id=4, unique_key="MOUSE-MX-001", date_assigned=datetime.now() - timedelta(days=250), notes="Wireless mouse"),
            EmployeeItem(emp_id="EMP003", item_id=11, unique_key="IPHONE-001", date_assigned=datetime.now() - timedelta(days=180), notes="Work phone"),
            EmployeeItem(emp_id="EMP004", item_id=12, unique_key="IPAD-001", date_assigned=datetime.now() - timedelta(days=160), notes="Work tablet"),
            EmployeeItem(emp_id="EMP005", item_id=1, unique_key="DELL-XPS-003", date_assigned=datetime.now() - timedelta(days=150), notes="Main work laptop"),
            EmployeeItem(emp_id="EMP006", item_id=7, unique_key="HEADPHONE-001", date_assigned=datetime.now() - timedelta(days=140), notes="Premium headphones"),
            EmployeeItem(emp_id="EMP007", item_id=8, unique_key="CHAIR-001", date_assigned=datetime.now() - timedelta(days=120), notes="Office chair"),
            EmployeeItem(emp_id="EMP008", item_id=9, unique_key="DESK-001", date_assigned=datetime.now() - timedelta(days=100), notes="Standing desk"),
        ]
        session.add_all(employee_items_data)
        session.flush()
        
        # Create Item Transfer History
        transfer_history_data = [
            ItemTransferHistory(item_id=1, from_emp_id="EMP001", to_emp_id="EMP002", transfer_date=datetime.now().date() - timedelta(days=50), notes="Laptop upgrade"),
            ItemTransferHistory(item_id=4, from_emp_id="EMP002", to_emp_id="EMP005", transfer_date=datetime.now().date() - timedelta(days=30), notes="Mouse replacement"),
        ]
        session.add_all(transfer_history_data)
        session.flush()
        
        # Create Logs
        logs_data = [
            Log(action_type="LOGIN", details="User admin logged in", timestamp=datetime.now() - timedelta(hours=2), user_id=1),
            Log(action_type="EMPLOYEE_ADDED", details="Added employee EMP001", timestamp=datetime.now() - timedelta(hours=1), user_id=1),
            Log(action_type="ITEM_ASSIGNED", details="Assigned item to employee", timestamp=datetime.now() - timedelta(minutes=30), user_id=2),
        ]
        session.add_all(logs_data)
        
        print("✓ Dummy data seeded successfully!")
        print("  - 4 Divisions")
        print("  - 3 Users (admin, manager1, manager2)")
        print("  - 8 Employees")
        print("  - 12 Items")
        print("  - 11 Employee-Item Assignments")
        print("  - 2 Transfer History Records")
        print("  - 3 Log Entries")
        print("\nDefault Credentials:")
        print("  Username: admin, Password: admin123")
        print("  Username: manager1, Password: manager123")
        print("  Username: manager2, Password: manager123")
