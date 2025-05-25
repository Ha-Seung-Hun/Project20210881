class PaymentGateway:
    def process_payment(self, amount):
        print(f"[결제 시스템] {amount}원 결제 완료.")
        return True

class Restaurant:
    def receive_order(self, order):
        print(f"[레스토랑] 주문 접수: {order}")
        return "조리 중입니다."

class Server:
    def __init__(self):
        self.restaurants = ["김밥천국", "한솥", "BBQ"]
        self.menus = {
            "김밥천국": ["김밥", "라면"],
            "한솥": ["도시락", "제육"],
            "BBQ": ["후라이드치킨", "양념치킨"]
        }

    def get_restaurants(self):
        return self.restaurants

    def get_menu(self, name):
        return self.menus.get(name, [])

    def send_order(self, restaurant, order):
        return Restaurant().receive_order(order)

class BaeminApp:
    def __init__(self):
        self.server = Server()
        self.payment = PaymentGateway()

    def show_restaurants(self):
        stores = self.server.get_restaurants()
        print("📍 주변 음식점:", stores)
        return stores

    def show_menu(self, store_name):
        menu = self.server.get_menu(store_name)
        print(f"🍴 {store_name} 메뉴:", menu)
        return menu

    def order_food(self, store_name, menu_item, price):
        if self.payment.process_payment(price):
            result = self.server.send_order(store_name, menu_item)
            print("✅ 주문 결과:", result)

# 실행 예시
app = BaeminApp()
stores = app.show_restaurants()
menu = app.show_menu("김밥천국")
app.order_food("김밥천국", "김밥", 3500)
