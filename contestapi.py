from faker import Faker                                                                                # type: ignore
import json

faker = Faker()

def generate_order():
    name = faker.name()
    burguer_id = faker.random_int(1,21)
    amount = faker.random_int(1,3)
    
    time_minutes = faker.random_int(0, 60)
    if(time_minutes) < 10:
        time_minutes = f"0{str(time_minutes)}"

    time_hours = faker.random_int(11, 20)
    
    time = f"{time_hours}:{time_minutes}"

    order_dict = {"name": name, "burguer_id": burguer_id, "amount":amount, "time":time}

    order_json = json.dumps(order_dict)

    return order_json



