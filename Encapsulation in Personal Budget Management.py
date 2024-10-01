class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = []

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, value):
        if isinstance(value, str) and value.strip():
            self.__category_name = value
        else:
            raise ValueError("Category Name must be a non-empty string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__allocated_budget = value
        else:
            raise ValueError("Allocated Budget must be a positive number.")

    def add_expense(self, description, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        if amount > self.__allocated_budget:
            raise ValueError("Expense exceeds allocated budget.")

        self.__allocated_budget -= amount
        self.__expenses.append({'description': description, 'amount': amount})
        print(f"Added expense: {description}, Amount: {amount}")

    def get_remaining_budget(self):
        return self.__allocated_budget

    def list_expenses(self):
        print(f"Expenses for {self.__category_name}:")
        for expense in self.__expenses:
            print(f" - {expense['description']}: {expense['amount']}")

    def display_category_summary(self):
        print(f"Budget Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.get_remaining_budget()}")
        self.list_expenses()


food_category = BudgetCategory("Food", 500)
food_category.add_expense("Groceries", 100)
food_category.display_category_summary()
