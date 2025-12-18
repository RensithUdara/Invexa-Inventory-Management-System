# gui/login.py
import customtkinter as ctk
from config import COLORS
from gui.manager import ManagerTools
from controllers import authenticate_user
from tkinter import messagebox

class LoginPage:
    def __init__(self, main_frame, app):
        self.main_frame = main_frame
        self.app = app
        self.entries = {}
        
    def display(self):
        self.clear_main_frame()
        
        # Set main frame background
        self.main_frame.configure(fg_color=COLORS['bg_primary'])
        
        # Create a container frame for centering the login form
        container = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Logo and Welcome text
        logo_frame = ctk.CTkFrame(container, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=20, pady=(20, 40))
        
        # InMan logo with modern colors
        in_label = ctk.CTkLabel(
            logo_frame,
            text="In",
            font=ctk.CTkFont(size=56, weight="bold", family="Helvetica"),
            text_color=COLORS["primary"]
        )
        in_label.grid(row=0, column=0)
        
        man_label = ctk.CTkLabel(
            logo_frame,
            text="Man",
            font=ctk.CTkFont(size=56, weight="bold", family="Helvetica"),
            text_color=COLORS["accent"]
        )
        man_label.grid(row=0, column=1)
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            container,
            text="Inventory Management System",
            font=ctk.CTkFont(size=14, weight="normal", family="Helvetica"),
            text_color=COLORS["text_secondary"]
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 30))
        
        welcome_label = ctk.CTkLabel(
            container,
            text="Welcome Back",
            font=ctk.CTkFont(size=20, weight="bold", family="Helvetica"),
            text_color=COLORS["text_primary"]
        )
        welcome_label.grid(row=2, column=0, pady=(0, 25))
        
        # Login form frame with modern design
        form_frame = ctk.CTkFrame(
            container,
            fg_color=COLORS["bg_secondary"],
            corner_radius=20,
            border_width=2,
            border_color=COLORS["border"]
        )
        form_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        
        # Username field
        username_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        username_frame.grid(row=0, column=0, padx=40, pady=(30, 20), sticky="ew")
        
        username_label = ctk.CTkLabel(
            username_frame,
            text="Username",
            font=ctk.CTkFont(size=13, weight="bold", family="Helvetica"),
            text_color=COLORS["text_primary"]
        )
        username_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.entries["username"] = ctk.CTkEntry(
            username_frame,
            width=320,
            height=45,
            placeholder_text="Enter your username",
            border_color=COLORS["border_light"],
            fg_color=COLORS["bg_tertiary"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=10,
            border_width=2
        )
        self.entries["username"].grid(row=1, column=0)
        
        # Password field
        password_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        password_frame.grid(row=1, column=0, padx=40, pady=20, sticky="ew")
        
        password_label = ctk.CTkLabel(
            password_frame,
            text="Password",
            font=ctk.CTkFont(size=13, weight="bold", family="Helvetica"),
            text_color=COLORS["text_primary"]
        )
        password_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.entries["password"] = ctk.CTkEntry(
            password_frame,
            width=320,
            height=45,
            placeholder_text="Enter your password",
            show="•",
            border_color=COLORS["border_light"],
            fg_color=COLORS["bg_tertiary"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=10,
            border_width=2
        )
        self.entries["password"].grid(row=1, column=0)
        
        # Login button with modern gradient-like effect
        login_button = ctk.CTkButton(
            form_frame,
            text="Login",
            command=self.handle_login,
            width=320,
            height=48,
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_dark"],
            text_color=COLORS["text_primary"],
            font=ctk.CTkFont(size=15, weight="bold", family="Helvetica"),
            corner_radius=10,
            border_width=0
        )
        login_button.grid(row=2, column=0, padx=40, pady=(20, 40))
        
        # Error label
        self.error_label = ctk.CTkLabel(
            form_frame,
            text="",
            font=ctk.CTkFont(size=12, family="Helvetica"),
            text_color=COLORS["danger"]
        )
        self.error_label.grid(row=3, column=0, pady=(0, 20))

    def handle_login(self):
        username = self.entries["username"].get()
        password = self.entries["password"].get()
        
        self.error_label.configure(text="")
        
        if not username or not password:
            self.error_label.configure(text="Please fill in all fields")
            return

        user = authenticate_user(username, password)
        if user:
            self.main_frame.master.winfo_children()[0].winfo_children()[2].configure(text="Manager Tools")
            self.main_frame.master.winfo_children()[0].winfo_children()[2].configure(command=self.show_manager_tools)
            self.clear_main_frame()
            self.show_manager_tools()
        else:
            self.error_label.configure(text="Invalid username or password")

    def show_manager_tools(self):
        self.clear_main_frame()
        ManagerTools(self.main_frame, self.app).display()
              
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()