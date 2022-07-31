from utils import AuthRequests, ProductRequests, NutritionRequests

auth = AuthRequests()

product_request = ProductRequests()

nutrition_request = NutritionRequests()




auth_response = auth.login(00000000, "password")

access = auth_response.json()["access"]

product = {"name": "Papas Fritas", "country": "Argentina", 'brand': "Lays"}

product_response = product_request.add_product(product, access)
#print(product_response.json())
product_data = product_response.json()

nutrition = {
  "product": "52e0d814-9027-400c-b4bf-6541128570df",
  "product_measure": "string",
  "sugar": 0,
  "fiber": 0,
  "monounsaturated_fats": 0,
  "polyunsaturated_fats": 10,
  "saturated_fats": 0,
  "trans_fats": 0,
  "total_fats": 0,
  "carbohydrates": 0,
  "energy": 0,
  "sodium": 0,
  "cholesterol": 0,
  "protein": 0
}

nutrition_response = nutrition_request.add_nutrition(nutrition, access)

nutrition_data = nutrition_response.json()