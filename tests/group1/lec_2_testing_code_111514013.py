import add_path
import mit_ocw_data_science.lec2.menu as mit

menu = mit.Menu()
menu.build_large_menu(20, 180, 10)
menu_str = str(menu)
print(menu_str)

greedy_items = mit.greedy(menu.get_foods(), 300, mit.Food.density)
#print("Greedy items:", greedy_items[0])
greedy_items_str = mit.Menu.get_foods_str(greedy_items[0])
print(greedy_items_str)

rest = mit.max_val(menu.get_foods(), 300)

print("total price", rest[0], ":", end="\ndetails: ")
for item in rest[1]:
    print(item, end=", ")