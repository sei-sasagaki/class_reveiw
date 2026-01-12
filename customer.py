from inspect import AGEN_CLOSED


class Customer:
    # 各問のコードが期待通り動作するように実装
    # コンストラクタ（初期化メソッド）
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # メソッド
    # C-1. フルネームを取得できる
    def full_name(self):
        return self.first_name + " " + self.family_name

    # C-2. 年齢という概念を取得できる
    def age(self):
        return self.age

    # C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
    def entry_fee(self):
        if self.age <= 3:  # C-5. 3歳以下の入場料金の無料化
            return 0
        elif self.age < 20:
            return 1000
        elif self.age >= 20 and self.age < 65:
            return 1500
        elif self.age >= 65 and self.age < 75:
            return 1200
        elif self.age >= 75:  # C-6. 75歳以上の料金区分の追加
            return 500

    # C-4. 単一の顧客情報をCSV形式で取得できる
    def info_csv(self):
        # return self.full_name + "," + str(self.age) + "," + str(self.entry_fee())
        # C-7. 単一顧客の情報取得形式の追加その1
        # return self.full_name + "\t" + str(self.age) + "\t" + str(self.entry_fee())
        # C-8. 単一顧客の情報取得形式の追加その2
        # return self.full_name + "|" + str(self.age) + "|" + str(self.entry_fee())
        return str(self.full_name()) + "|" + str(self.age) + "|" + str(self.entry_fee())


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# 以降で各問のコードを追加していく
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力

# 応用
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
print(michelle.info_csv())
