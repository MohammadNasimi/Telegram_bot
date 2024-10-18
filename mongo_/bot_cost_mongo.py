import pymongo


class ExpenseMongoClient:
    def __init__(
            self,
            host: str,
            port: int,
            db_name: str = "telegram_bot",
            collection_name: str = "expenses",
    ):
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def add_expense(self, user_id: int, amount: int, category: str, description: str):
        # write your code here
        expense = {'user_id': user_id, 'amount': amount, 'category': category, 'description': description}
        return self.collection.insert_one(expense)

    def get_expenses(self, user_id: int) -> list:
        return list(self.collection.find({'user_id': user_id}, {'user_id': 0, '_id': 0}))

    def get_categories(self, user_id: int) -> list:
        objects = self.collection.find({'user_id': user_id}, {'user_id': 0, '_id': 0})
        return [object["category"] for object in objects]


    def get_expenses_by_category(self, user_id: int, category: str) -> list:
        return list(self.collection.find({'user_id': user_id, 'category':category}, {'user_id': 0, '_id': 0}))


    def get_total_expense(self, user_id: int):
        total  = self.collection.aggregate([{"$match":{"user_id":user_id}},{"$project":{'_id':0}},{"$group": {"_id": "$user_id", "sum": {"$sum": "$amount"}}}])
        return list(total)[0]["sum"]

    def get_total_expense_by_category(self, user_id: int):
        pipline =[{"$match":{"user_id":user_id}},{"$project":{'_id':0,'description': 0}},
                  {"$group": {"_id": "$category", "sum": {"$sum": "$amount"}}}]
        total  = self.collection.aggregate(pipline)
        return [{i["_id"]:i["sum"]} for i in total]


if __name__ == "__main__":
    expense_mongo_client = ExpenseMongoClient("localhost", 27017)
    # expense_mongo_client.add_expense(123, 100, "غذا", "ناهار")
    # expense_mongo_client.add_expense(123, 200, "غذا", "شام")
    # expense_mongo_client.add_expense(123, 300, "سفر", "پرواز")
    # expense_mongo_client.add_expense(321, 400, "غذا", "ناهار")
    # expense_mongo_client.add_expense(321, 500, "سفر", "پرواز")

    print("Expenses of 123")
    print(expense_mongo_client.get_expenses(123))

    print("Categories of 123")
    print(expense_mongo_client.get_categories(123))

    print("Total expense of 321")
    print(expense_mongo_client.get_total_expense(321))

    print("Total expense by category of 321")
    print(expense_mongo_client.get_total_expense_by_category(321))

    print("Expenses by category of 123")
    print(expense_mongo_client.get_expenses_by_category(123, "غذا"))
