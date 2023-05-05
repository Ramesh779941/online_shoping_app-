from tkinter import *

def open_demo_main_page():
    # Create a window
    window = Tk()
    window.geometry("500x500")
    window.title("Online Shopping App")

    # Create a label
    title_label = Label(window, text="Welcome to our Online Store!")
    title_label.pack()

    # Create a frame for the items
    items_frame = Frame(window)
    items_frame.pack()

    # Create some sample items
    item1_label = Label(items_frame, text="Item 1: $10")
    item1_label.pack()
    item1_button = Button(items_frame, text="Add Item 1 to Cart", command=lambda: add_to_cart("Item 1"))
    item1_button.pack()
    item2_label = Label(items_frame, text="Item 2: $20")
    item2_label.pack()
    item2_button = Button(items_frame, text="Add Item 2 to Cart", command=lambda: add_to_cart("Item 2"))
    item2_button.pack()

    # Create a label for the cart
    cart_label = Label(window, text="Your Cart")
    cart_label.pack()

    # Create a listbox for the cart
    cart_listbox = Listbox(window)
    cart_listbox.pack()





    # Create a function for adding items to the cart
    def add_to_cart(item):
        cart_listbox.insert(END, item)



    def checkout():
        window = Tk()
        window.geometry("500x500")
        window.title("checkout page")


        # Code to open the checkout page
        title_label = Label(window, text="enter your details")
        title_label.pack()



        first_name_label = Label(root, text="First Name:")
        first_name_label.pack()

        first_name_entry = Entry(root)
        first_name_entry.pack()

        last_name_label = Label(root, text="Last Name:")
        last_name_label.pack()

        last_name_entry = Entry(root)
        last_name_entry.pack()

        zip_code_label = Label(root, text="Zip Code:")
        zip_code_label.pack()

        zip_code_entry = Entry(root)
        zip_code_entry.pack()

    checkout = Button(items_frame, text="checkout", command=checkout)
    checkout.pack()

    # Run the window
    window.mainloop()
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "pass":
        # Redirect to the Demo Main Page
        root.destroy()
        open_demo_main_page()
    else:
        # Display an error message
        error_label.config(text="Sorry, your account information is incorrect.")

# Create the main window
root = Tk()
root.title("Demo Login Page")

# Create the login form
username_label = Label(root, text="Username:")
username_label.pack()

username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

# Create the login button
login_button = Button(root, text="Login", command=login)
login_button.pack()

# Create the error label
error_label = Label(root, fg="red")
error_label.pack()

checkout_label = Label(root, text="Checkout Page")
checkout_label.pack()

# Run the main loop
root.mainloop()