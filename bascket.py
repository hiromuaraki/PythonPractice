# -*- coding: utf-8 -*-
class Bascket:
    TAX_VALUE = 10

    # カートを用意
    cart_dic = {}
    
    # カートに商品を追加
    def add(self, product):
        self.cart_dic[product.name] = product

    # カートの一覧を表示
    def show_read(self):
        print("NAME    | NUM | PRICE")

        # カートの中身が空か
        if len(self.cart_dic) == 0:
            print("カゴの中身が空です")
        else:
            # カートから商品情報を1件ずつ取り出す
            for name, product in self.cart_dic.items():
                num = int(product.num)
                price = int(product.price)
                tax_value = self.calc_tax_value(num, price)
                total_price = int((num * price) + tax_value)
                print("{0:<8}| {1:<3} | {2}".format(name, num, total_price))
    
    # 商品の合計金額の計算
    def calc_sum_dic(self):
        total_price = 0
        for product in self.cart_dic.values():
            num = int(product.num)
            price = int(product.price)
            tax_value = self.calc_tax_value(num, price)
            value = int((num * price) + tax_value)
            total_price += value
        print("TOTAL PRICE:{0}".format(total_price))

    # 商品の合計数量を計算
    def clac_cart_count(self):
        total_count = 0
        for product in self.cart_dic.values():
            total_count += int(product.num)
    
    # カートの指定した商品を削除
    def delete(self, product_name):
        try:
            delete_product = self.cart_dic.pop(product_name)
            print("{0}を買い物カゴから削除しました。".format(delete_product.name))
        except KeyError as k:
            print(k)
            print("該当商品が存在しないか、すでに削除されています。")

    # 税込金額の計算
    def calc_tax_value(self, num, price):
        tax_value = (num * price) / self.TAX_VALUE
        return tax_value

# 商品クラス
class Product:
    name  = ""
    price = 0
    num   = 0

# 商品クラスを初期化
def instance_product():
    name = input("商品名を入力してください:")
    num = int(input("数量を入力してください:"))
    price = int(input("値段を入力してください:"))
    product  = Product()
    product.name = name
    product.num = num
    product.price = price
    return product

if __name__ == "__main__":

    basket = Bascket()
    while 1:
        select_mode = int(input("1:カゴに入れる/2:一覧表示/3:合計金額/4:合計商品数/5:削除/0:買わない:"))
        if select_mode == 0: break
        if select_mode == 1:
            product = instance_product()
            basket.add(product)
        elif select_mode == 2:
            basket.show_read()
        elif select_mode == 3:
            basket.calc_sum_dic()
        elif select_mode == 4:
            basket.clac_cart_count()
        elif select_mode == 5:
            product_name = input("削除したい商品名を入力してください")
            basket.delete(product_name)

