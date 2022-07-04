from function import create_query

app_name = input("Select app name listed from below:\nZamit, Ronstring, Biodex, Treeflex, Regrant, Namfix, Domainer, Tree, Voyatouch \nEnter app name: ")

location_name = input("Select location name from listed below:\nMwaya, Tokyo, Mora, Itu, Port Antonio, Bendo, Guider, Ruuki, Guider, Setro, Jiangmen \nEnter location name: ")

print(create_query(app_name, location_name))