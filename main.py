# Receipt Generator 
from pyscript import display, document

def getting_total(e):
    document.getElementById('result').innerHTML = ""
    
    selected_coffee = document.querySelector(".menu-item:checked")
    
    subtotal = float(selected_coffee.value)
    vat = subtotal * 0.12
    total = subtotal + vat
    
    display(f"Subtotal: Php {subtotal}", target="result")
    display(f"Tax (12%): Php {vat}", target="result")
    display(f"<b>Total payment:<b> Php {total}", target="result")

