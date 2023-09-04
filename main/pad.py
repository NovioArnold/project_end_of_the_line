def unload_car(self, quantity: int, product: str):
    if product == self.input_1:
        print(self.input_1)
        self.stock_input_1 = product_to_self(
            stock=self.stock_input_1,
            quantity=quantity,
            max_store=self.max_store_input_1
        )

    elif product == self.input_2:
        self.stock_output_2 = product_to_self(
            stock=self.stock_output_2,
            quantity=quantity,
            max_store=self.max_store_output_2
        )
    elif product == self.input_3:
        self.in_stock_input_3 = product_to_self(
            stock=self.in_stock_input_3,
            quantity=quantity,
            max_store=self.max_store_input_3
        )


def load_car(self, quantity: int, product: str):
    if product == self.output_1:
        self.stock_output_1 = product_from_self(
            stock=self.stock_output_1,
            quantity=quantity
        )
    elif product == self.output_2:
        self.stock_output_2 = product_from_self(
            stock=self.stock_output_2,
            quantity=quantity,
        )