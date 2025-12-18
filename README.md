# 📦 InMan - Inventory Management System

A modern, user-friendly **Inventory Management System** built with Python and CustomTkinter. Designed for organizations to efficiently manage, track, and organize inventory items assigned to employees across multiple divisions.

## ✨ Features

### Core Functionality
- **👥 Employee Management** - Add, update, and remove employee records with division assignments
- **📦 Item Management** - Comprehensive item tracking with unique identifiers and status management
- **🏢 Division Management** - Organize employees into departments/divisions
- **🔗 Item Assignment** - Assign items to employees with tracking and transfer history
- **📊 Dashboard** - Real-time overview of inventory statistics and metrics
- **🔍 Advanced Search** - Multi-type search (employees, items, divisions, unique keys) with filtering
- **📤 Export to Excel** - Export search results and reports with custom formatting
- **📝 Audit Logging** - Complete action logging for security and accountability
- **🔐 User Authentication** - Secure login system with role-based access control

### User Interface
- **Modern Design** - Contemporary UI with blue/teal color scheme
- **Dark Mode** - Eye-friendly dark theme optimized for extended use
- **Responsive Layout** - Clean sidebar navigation and organized main content area
- **Intuitive Controls** - Easy-to-use forms and dialogs for all operations

## 🚀 Quick Start

### Prerequisites
- **Python** 3.10 or higher
- **pip** package manager
- Windows, macOS, or Linux operating system

### Installation

1. **Clone or Download the Repository**
   ```bash
   cd InMan-main
   ```

2. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:
   ```bash
   pip install customtkinter xlsxwriter openpyxl sqlalchemy pandas
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## 🔑 Default Credentials

The application comes with pre-configured test user accounts:

| Username | Password | Role |
|----------|----------|------|
| `admin` | `admin123` | Admin |
| `manager1` | `manager123` | Manager |
| `manager2` | `manager123` | Manager |

## 📁 Project Structure

```
InMan/
├── main.py                          # Entry point - Application launcher
├── config.py                        # Configuration & color theme settings
├── seed_data.py                     # Dummy data for testing
├── requirements.txt                 # Python dependencies
│
├── models/
│   ├── __init__.py
│   ├── database.py                  # Database connection & initialization
│   └── models.py                    # SQLAlchemy ORM models
│
├── controllers/
│   ├── __init__.py
│   ├── auth.py                      # Authentication logic
│   └── crud.py                      # Create, Read, Update, Delete operations
│
├── gui/
│   ├── __init__.py
│   ├── ui.py                        # Main application window
│   ├── login.py                     # Login page interface
│   ├── sidebar.py                   # Navigation sidebar
│   ├── dashboard.py                 # Dashboard/home page
│   ├── inventory.py                 # Inventory display page
│   ├── manager.py                   # Manager tools interface
│   ├── utils.py                     # UI utility functions
│   └── tools/
│       ├── add_items.py             # Add new items
│       ├── add_employee.py          # Add new employees
│       ├── add_division.py          # Add new divisions
│       ├── assign_items_to_employees.py
│       ├── transfer_items.py
│       ├── update_item_details.py
│       ├── update_employee_details.py
│       ├── remove_items.py
│       ├── remove_employee.py
│       ├── remove_division.py
│       ├── view_item_details.py
│       ├── view_employee_records.py
│       ├── view_division_structure.py
│       ├── view_asset_assignment.py
│       └── bulk_employee_import.py
│
├── utils/
│   ├── __init__.py
│   ├── search.py                    # Search functionality
│   └── summary.py                   # Report generation
│
├── assets/                          # Images, icons, resources
├── __pycache__/                     # Python cache (auto-generated)
└── inventory.db                     # SQLite database (auto-created)
```

## 🗄️ Database Schema

### Tables

#### 1. **Divisions**
- `division_id` (Primary Key)
- `name` (Unique, String)

#### 2. **Employees**
- `emp_id` (Primary Key, String)
- `name` (String)
- `division_id` (Foreign Key)
- `item_count` (Integer, default: 0)
- `date_joined` (DateTime)

#### 3. **Items**
- `item_id` (Primary Key)
- `name` (Unique, String)
- `last_assigned` (DateTime)

#### 4. **EmployeeItems** (Junction Table)
- `id` (Primary Key)
- `emp_id` (Foreign Key → Employees)
- `item_id` (Foreign Key → Items)
- `unique_key` (String, nullable)
- `date_assigned` (DateTime)
- `notes` (Text)

#### 5. **EmployeeItemAttributes**
- `emp_attribute_id` (Primary Key)
- `emp_item_id` (Foreign Key)
- `name` (String)
- `value` (String)

#### 6. **Users** (System Managers)
- `user_id` (Primary Key)
- `username` (Unique, String)
- `password` (Hashed, String)
- `role` (String)

#### 7. **Logs** (Audit Trail)
- `log_id` (Primary Key)
- `action_type` (String)
- `details` (Text, nullable)
- `timestamp` (DateTime)
- `user_id` (Foreign Key, nullable)

#### 8. **ItemTransferHistory**
- `transfer_id` (Primary Key)
- `item_id` (Foreign Key)
- `from_emp_id` (Foreign Key)
- `to_emp_id` (Foreign Key)
- `transfer_date` (Date)
- `notes` (Text)

## 🎨 Color Theme

The application uses a modern **Blue/Teal color palette**:

| Element | Color | Hex Code |
|---------|-------|----------|
| Primary | Sky Blue | #0ea5e9 |
| Secondary | Cyan | #06b6d4 |
| Accent | Emerald Green | #10b981 |
| Background Primary | Dark Navy | #0f172a |
| Background Secondary | Slate 800 | #1e293b |
| Text Primary | Slate 100 | #f1f5f9 |
| Text Secondary | Slate 300 | #cbd5e1 |
| Success | Green | #10b981 |
| Warning | Amber | #f59e0b |
| Danger | Red | #ef4444 |

## 💡 Usage Guide

### 1. **Login**
   - Launch the application
   - Enter credentials (use default credentials above)
   - Click "Login" to access the system

### 2. **Dashboard**
   - View key statistics:
     - Total Employees
     - Total Items
     - Total Divisions
     - Items in Stock
   - Quick overview of system health

### 3. **Managing Employees**
   - **Add Employee**: Navigate to Manager Tools → Add Employee
   - **View Records**: Click "View Employee Records"
   - **Update Details**: Use "Update Employee Details"
   - **Remove**: Use "Remove Employee"

### 4. **Managing Items**
   - **Add Items**: Manager Tools → Add Items
   - **View Details**: Click "View Item Details"
   - **Update**: Use "Update Item Details"
   - **Remove**: Use "Remove Items"

### 5. **Item Assignment**
   - Assign items to employees
   - Track transfer history
   - Update assignment notes

### 6. **Search & Export**
   - Use the advanced search feature
   - Filter by type (employee, item, division, key)
   - Export results to Excel with formatting

### 7. **Division Management**
   - Add new divisions
   - View division structure
   - Update or remove divisions

## 📊 Dummy Data Included

The application comes pre-loaded with sample data:
- 4 Divisions (IT, HR, Finance, Operations)
- 8 Employees across divisions
- 12 Items (laptops, monitors, phones, etc.)
- 11 Employee-Item Assignments
- 2 Transfer History records
- 3 Log entries

## 🔒 Security Features

- **Password Hashing**: Salted SHA256 hashing for password storage
- **User Authentication**: Secure login verification
- **Role-Based Access**: Different permission levels
- **Audit Logging**: All actions logged with timestamps and user info
- **Data Integrity**: Database constraints and relationships

## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Backend language |
| **CustomTkinter** | Modern GUI framework |
| **SQLAlchemy** | ORM for database |
| **SQLite** | Lightweight database |
| **openpyxl** | Excel file handling |
| **xlsxwriter** | Excel report generation |
| **Pandas** | Data manipulation |

## 📋 Requirements

Create a `requirements.txt` file with:
```
customtkinter==5.2.2
xlsxwriter==3.2.9
openpyxl==3.1.5
sqlalchemy==2.0.23
pandas==2.0.3
```

Install all requirements:
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

Edit `config.py` to customize:
- **Color Theme**: Modify the `COLORS` dictionary
- **Window Size**: Adjust in `gui/ui.py`
- **Database Location**: Change `DATABASE_URL` in `models/database.py`
- **Default Credentials**: Update in `seed_data.py` and re-run

## 📝 Common Operations

### Add a New Division
1. Click "Dashboard"
2. Open Manager Tools
3. Select "Add Division"
4. Fill in division name
5. Click Add

### Assign Item to Employee
1. Navigate to "View Inventory"
2. Click "Assign Items to Employees"
3. Select employee and items
4. Set assignment details
5. Confirm assignment

### Export Search Results
1. Use Search functionality
2. Filter results as needed
3. Click "Export to Excel"
4. Choose save location
5. File downloads automatically

### View Transfer History
1. Go to "View Item Details"
2. Select an item
3. View all transfers for that item
4. See dates, from/to employees, and notes

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Install missing package
```bash
pip install [package-name]
```

### Issue: "Database locked"
**Solution**: Close all instances of the application and try again

### Issue: Login fails
**Solution**: 
- Verify username and password (case-sensitive)
- Check that seed_data ran successfully
- Reset database by deleting `inventory.db`

### Issue: GUI elements not displaying
**Solution**: 
- Update CustomTkinter: `pip install --upgrade customtkinter`
- Ensure dark mode is enabled

## 📚 API Reference

### Authentication (controllers/auth.py)
```python
authenticate_user(username: str, password: str) -> User
hash_password(password: str) -> str
```

### CRUD Operations (controllers/crud.py)
- `get_all_employees()`
- `get_all_items()`
- `get_all_divisions()`
- `create_employee(emp_id, name, division_id)`
- `update_employee(emp_id, **kwargs)`
- `delete_employee(emp_id)`

### Search (utils/search.py)
```python
search_items_by_attribute(query: str, filter_type: str) -> List
search_employees(query: str) -> List
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is provided as-is for educational and business purposes. 

## 👨‍💻 Support & Contact

For issues, questions, or suggestions:
- Check the Troubleshooting section
- Review the Project Structure
- Examine the models and controllers for implementation details

## 🎯 Future Enhancements

Planned features for upcoming versions:
- [ ] Email notifications for assignments
- [ ] Advanced reporting dashboard
- [ ] Barcode/QR code scanning
- [ ] Multi-user simultaneous access
- [ ] Cloud backup functionality
- [ ] Mobile app support
- [ ] Department-wise analytics
- [ ] Automated inventory alerts

## 📈 Version History

**v2.0** (Current)
- Complete UI redesign with modern blue/teal theme
- Login system implementation
- Dummy data seeding
- Enhanced dashboard

**v1.3** (Previous)
- Initial inventory management features
- Basic CRUD operations
- Excel export functionality

## ⭐ Key Highlights

✅ **Production-Ready** - Fully functional and tested  
✅ **User-Friendly** - Intuitive interface with clear navigation  
✅ **Scalable** - Can handle large datasets efficiently  
✅ **Secure** - Password hashing and audit logging  
✅ **Modern Design** - Professional UI with contemporary styling  
✅ **Well-Documented** - Comprehensive comments and documentation  

---

**Built with ❤️ for efficient inventory management**

*Last Updated: December 2024*
