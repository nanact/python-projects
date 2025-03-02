import tkinter as tk
from tkinter import messagebox
from tkinter import ttk   

class RestaurantOrderManagerment:
    
    def __init__(self, root):
        self.root = root
        self.root.title(
            "Restaurant Management App"
        )
        
        self.menu_items = {
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":2,
            "PIZZA MEAL":2,
            "CHEESE BURGER":2,
            "DRINK":1
        }
        
        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely = 0.5,anchor = tk.CENTER)
        
        ttk.Label(frame,text = "Restaurant Order Managerment").grid(row = 0, columnspan=3)
        self.menu_label = {}
        self.menu_quantities = {}
        
        for i, (item, price) in enumerate(self.menu_items.items(), start = 1):
            label = ttk.Label(frame, text = f"{item} (${price}):",)
            label.grid(row= i, column=0)
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row = i, column=1)
            self.menu_quantities[item] = quantity_entry
        order_button = ttk.Button(frame,text = "place order",command=self.place_order)
        
        order_button.grid(row = len(self.menu_items) + 5, columnspan = 8)
    
    def place_order(self):
        total_cost = 0
        order_summary = "order summary: \n"
    
        for item, entry in self.menu_quantities.items():
            quatity = entry.get()
            if quatity.isdigit():
                quatity = int(quatity)
                price = self.menu_items[item]
                cost = quatity * price
                total_cost += cost  
                
                if quatity > 0:
                    order_summary = f"\n total cost: {total_cost}"
                    messagebox.showinfo(
                        "order placed",
                        order_summary
                    )
            if total_cost > 0:
                order_summary = f"\n Total cost: {total_cost}"
            
            else:
                messagebox.showerror("Error", "place order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagerment(root)
    root.geometry("600x300")
    root.mainloop()
        