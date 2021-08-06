# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1
def get_product(code):
    info = products[code]
    return info

get_product("americano")


def get_property(code,property):
    value = products[code][property]
    return value

get_property("dalgona","price")

# CODE CELL
# PROBLEM 3
def main():
    txt = "CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n"
    total = 0
    lst = []
    while True:
        #have to input /, in order to break
        code,quantity = input("Input Product and Quantity: ").split(",")
        if code != "/":
            if code in lst:
                if code == "dalgona" or code == "espresso":
                    x = txt.find(code)
                    y = txt[int(x)+20]
                    z = str(int(y)+int(quantity))
                    txt = txt.replace(y,z)
                    cost = str(get_property(code,"price")*int(quantity))
                    total += float(cost)
                    a = txt[int(x)+25:-1]
                    b = str(float(a)+float(cost))
                    txt = txt.replace(a,b)
                    
                elif code == "americano":
                    x = txt.find(code)
                    y = txt[int(x)+22]
                    z = str(int(y)+int(quantity))
                    txt = txt.replace(y,z)
                    cost = str(get_property(code,"price")*int(quantity))
                    total += float(cost)
                    a = txt[int(x)+27:-1]
                    b = str(float(a)+float(cost))
                    txt = txt.replace(a,b)
                elif code == "cappuccino":
                    x = txt.find(code)
                    y = txt[int(x)+24]
                    z = str(int(y)+int(quantity))
                    txt = txt.replace(y,z)
                    cost = str(get_property(code,"price")*int(quantity))
                    total += float(cost)
                    a = txt[int(x)+29:-1]
                    b = str(float(a)+float(cost))
                    txt = txt.replace(a,b)
                elif code == "frappuccino":
                    x = txt.find(code)
                    y = txt[int(x)+26]
                    z = str(int(y)+int(quantity))
                    txt = txt.replace(y,z)
                    cost = str(get_property(code,"price")*int(quantity))
                    total += float(cost)
                    a = txt[int(x)+30:-1]
                    b = str(float(a)+float(cost))
                    txt = txt.replace(a,b)
                else:
                    x = txt.find(code)
                    y = txt[int(x)+29]
                    z = str(int(y)+int(quantity))
                    txt = txt.replace(y,z)
                    cost = str(get_property(code,"price")*int(quantity))
                    total += float(cost)
                    a = txt[int(x)+34:-1]
                    b = str(float(a)+float(cost))
                    txt = txt.replace(a,b)
            else:
                if code == "dalgona":
                    cost = str(get_property(code,"price")*int(quantity))
                    txt += f"{code}\t\t\t"
                    txt += str(get_property(code,"name"))
                    txt += f"\t\t\t{quantity}\t\t\t\t"
                    txt += f"{cost}\n"
                    total += float(cost)
                    lst.append(code)
                else:
                    cost = str(get_property(code,"price")*int(quantity))
                    txt += f"{code}\t\t"
                    txt += str(get_property(code,"name"))
                    txt += f"\t\t{quantity}\t\t\t\t"
                    txt += f"{cost}\n"
                    total += float(cost)
                    lst.append(code)
        else:
            break
    txt += f"Total:\t\t\t\t\t\t\t\t\t\t{total}"
    with open("receipt.txt","w") as f:
        f.write(txt)
    
    
    
    #print(txt)
        
    

main()    