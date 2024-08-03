#requirements
#1. An invoice may contain zero or more comments.
#2. Comments may be added to an existing invoice.
#3. Invoices must expose a method that returns a string representation of all their comments.

#Updated code

from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.items = []
        self.cost = 0  # Initialize cost to 0
        self.comments = []  # Initialize comments list

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }
        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # Convert discount percentage to a decimal
        discount = discount / 100
        # Determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            # Apply discount before calculating tax
            discounted_price = price * (1 - discount)
            total += discounted_price + discounted_price * tax
        
        self.cost = total  # Store the calculated total in self.cost
        return total

    def add_comment(self, comment):
        """Add a comment to the invoice."""
        self.comments.append(comment)

    def get_comments(self):
        """Return a string representation of all comments."""
        return "\n".join(self.comments)


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice_total = invoice.calculate_total(20)
    print(f"Total: {invoice_total}")

    # Add comments to the invoice
    invoice.add_comment("Charge for building construction.")
    invoice.add_comment("Additional equipment rental.")
    invoice.add_comment("Fear tax included as per local regulations.")

    # Display all comments
    print("Comments:")
    print(invoice.get_comments())

#Explanation of the Changes
#Initialization of Comments List:
#Added self.comments = [] to the constructor to initialize the comments list.

#Adding a Comment:
#Implemented add_comment(self, comment) to add a comment to the comments list.

#Returning Comments:
#Implemented get_comments(self) to return a formatted string of all comments.

#Testing the Implementation

#Adding Comments:
#Added three comments to the invoice.

#Viewing Comments:
#Printed the comments using invoice.get_comments().