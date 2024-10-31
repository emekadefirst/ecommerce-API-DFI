import uuid

def order_code():
    return f"ORD{str(uuid.uuid4())[:8]}"

print(order_code())

#py test.py
"ORD8707ff3f"