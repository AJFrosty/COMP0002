from Invoice import Invoice

ticket = Invoice("1","Olvia GUTS Tour Ticket",2,20)

ticket.setPartDescription("2x Olivia GUTS Tour Ticket & 1x Taylor Swift Era's Tour Tickets")
ticket.setPrice(360)
ticket.setPartNumber("2")
ticket.setQuantity(3)
print(f"Ticket Number: {ticket.getPartNumber()} \nItem(s): {ticket.getPartDescription()} \nPrice: ${ticket.getPrice()} \nQuantity: {ticket.getQuantity()} \nTotal: ${ticket.getInvoiceAmount()}")