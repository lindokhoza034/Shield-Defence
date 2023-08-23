import subprocess
import tkinter
from tkinter import messagebox
import customtkinter
import tkinter as tk
from PIL import ImageTk, Image

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

host_path = "C:\Windows\System32\drivers\etc\hosts"
ip_address = "127.0.0.1"


def show_popup(popup_message):
    messagebox.showinfo("Popup", popup_message)


class App(customtkinter.CTk):
    # image path
    logo_light_path = "1.png"
    logo_dark_path = "5.png"

    # Block website
    def block_websites(self, event=None):
        website_lists = self.entry.get()
        websites = website_lists.split(",")
        with open(host_path, "r+") as host_file:
            file_content = host_file.read()
            for web in websites:
                web = web.strip()
                if not web:
                    show_popup(f"Empty website entry is not allowed")
                    # Skip empty websites
                    continue
                if web in file_content:
                    show_popup(f"{web} is Already Blocked")
                else:
                    host_file.write(f"{ip_address} {web}\n")
                    show_popup(f"{web} is Blocked")
        self.refresh_blocked_sites()

    # def unblock_websites(self, event=None):
    #     website_lists = self.entry.get()
    #     websites = website_lists.split(",")
    #     with open(host_path, 'r+') as host_file:
    #         file_content = host_file.readlines()
    #         with open(host_path, 'w') as f:
    #             for line in file_content:
    #                 if not any(web.strip() in line for web in websites):
    #                     f.write(line)
    #                 show_popup(f"{website_lists} is Unblocked")
    #     self.refresh_blocked_sites()

    def unblock_websites(self, event=None):
        website_lists = self.entry.get()
        websites = website_lists.split(",")
        if any(not web.strip() for web in websites):
            show_popup("Empty website entry is not allowed")
            return  # Exit the function if any empty website is found
        with open(host_path, "r+") as host_file:
            file_content = host_file.readlines()
            with open(host_path, "w") as f:
                for line in file_content:
                    line_website = line.split()[-1].strip()
                    if line_website in websites:
                        continue  # Skip matching websites
                    f.write(line)
            show_popup(f"{website_lists} is Unblocked")
        self.refresh_blocked_sites()

    def unblock_all_websites(self, event=None):
        with open(host_path, "w") as f:
            f.write("")
        self.refresh_blocked_sites()
        show_popup("All websites are unblocked")

    def refresh_blocked_sites(self):
        self.entry.delete(0, "end")
        with open(host_path, "r") as host_file:
            blocked_sites = [
                line.split()[-1] for line in host_file if ip_address in line
            ]
            # Clear existing text
            self.textbox.delete("1.0", customtkinter.END)
            if blocked_sites:
                self.textbox.insert(customtkinter.END, "Blocked Websites\n")
                for site in blocked_sites:
                    self.textbox.insert(customtkinter.END, site + "\n")
            else:
                self.textbox.insert(customtkinter.END, "No Blocked Websites\n")

    def view_instructions(self):
        self.textbox.delete("1.0", customtkinter.END)  # Clear existing text
        instructions = """
        Instructions:

        1. To Block:
          - Enter a website URL in the entry field.
          - Click on the 'Block' button.

        2. To Unblock:
          - Enter a website URL in the entry field.
          - Click on the 'Unblock' button.

        3. To Unblock All:
          - Click on the 'Unblock All' button.

        4. To View Blocked:
          - Click on the 'View Blocked' button.

        5. Use the Appearance Mode dropdown to select the desired appearance mode.
        7. Use the UI Scaling dropdown to adjust the size of the user interface.
        8. Use the button on the far right to Log out.
        """
        self.textbox.insert(customtkinter.END, instructions)

    def logout(self):
        subprocess.Popen(["python", "login.py"])
        self.destroy()

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Shield Defence")
        self.geometry(
            f"{1100}x{580}+{(self.winfo_screenwidth() - 1100) // 2}+{(self.winfo_screenheight() - 580) // 2}"
        )

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Load the logo image
        logo_light_image = Image.open(self.logo_light_path)
        logo_dark_image = Image.open(self.logo_dark_path)

        # Adjust the size as per your preference
        logo_light_image = logo_light_image.resize((100, 100))
        logo_dark_image = logo_dark_image.resize((100, 100))

        self.customtkinter_logo_light = ImageTk.PhotoImage(logo_light_image)
        self.customtkinter_logo_dark = ImageTk.PhotoImage(logo_dark_image)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        # self.logo_label = customtkinter.CTkLabel(
        #     self.sidebar_frame, text="Shield Defence", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, text="Block", command=self.block_websites
        )

        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text="Unblock", command=self.unblock_websites
        )

        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Unblock All", command=self.unblock_all_websites
        )

        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_frame, text="View Blocked", command=self.refresh_blocked_sites
        )

        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(
            self.sidebar_frame, text="Instructions", command=self.view_instructions
        )

        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )

        self.main_button_6 = customtkinter.CTkButton(
            master=self,
            border_width=2,
            border_color="#DCE4EE",
            text_color=("gray10", "#DCE4EE"),
            text="Log Out",
            command=self.logout,
        )
        self.main_button_6.grid(
            row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Enter the website URL"
        )
        self.entry.grid(
            row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(
            row=1, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew"
        )

        # create tabview
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")

        self.textbox.insert(
            "0.0",
            "\n Welcome to Shield Defence\n\n\nTo get started read the instructions.\n\n"
            + "\n\n" * 20,
        )

        # inserting the image
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, image=self.customtkinter_logo_light, text=""
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog"
        )
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

        if new_appearance_mode == "Dark":
            logo_image = Image.open(self.logo_dark_path)
        else:
            logo_image = Image.open(self.logo_light_path)

        logo_image = logo_image.resize((100, 100))
        logo_photo = ImageTk.PhotoImage(logo_image)
        self.logo_label.configure(image=logo_photo)
        self.logo_label.image = logo_photo

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
