#Issues Identified
#Discount Application:

#The calculate_total method is applying the discount incorrectly. The discount should be subtracted from the price before calculating the tax. The current logic incorrectly multiplies the tax by the discount.
#Discount Value:

#The discount is not treated as a percentage. For instance, a discount of 20 should be interpreted as 20%, but the current method uses it directly in calculations without converting it.
#Fixing the Code
#We'll adjust the calculate_total method to apply the discount correctly and calculate the total price as required.


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
        self.cost = 0
        self.items = []

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
        self.cost = total
        return total


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
    print(invoice_total)

#
#Explanation of the Fix
#Discount Calculation:
#We convert the discount percentage to a decimal (discount = discount / 100).
#We apply the discount to the item price before calculating the tax (discounted_price = price * (1 - discount)).
#We then add the discounted price and the tax on the discounted price to the total (total += discounted_price + discounted_price * tax).
#This ensures that the discount is applied correctly before tax is calculated, fulfilling all the requirements correctly.