example_list = [1, 2, 3, 4]

example_list.append(5)
print(example_list)

example_list.remove(5)
print(example_list)


orders = ["daisies", "periwinkle"]
print(orders)

orders.append("tulips")
orders.append("roses")

print(orders)


shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = (shopping_list[5])
print(last_element)

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
print(garden_waitlist)
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] =  "Alex"
print(garden_waitlist)


order_list= ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)


heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]


class_name_test= [["Jenny", 90], ["Alexus", 85.5],["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score=  class_name_test[2][1]
print(sams_score)

ellies_score= class_name_test[-1][-1]
print(ellies_score)


incoming_class= [["Kenny",	"American",	9],["Tanya", "Russian",	9], ["Madison",	"Indian",	7]]
print(incoming_class)

incoming_class[2][2]= 8
print(incoming_class)

incoming_class[-3][-3]= "Ken"
print(incoming_class)


first_names= ["Ainsley","Ben", "Chani","Depak"]
preferred_size= ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data= [["Ainsley",	"Small",	True], ["Ben",	"Large",	False], ["Chani",	"Medium",	True], ["Depak",	"Medium",	False]]
print(customer_data)

customer_data[2][-1]= False
print(customer_data)

customer_data[1].remove("Large")
print(customer_data)

customer_data_final= customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
