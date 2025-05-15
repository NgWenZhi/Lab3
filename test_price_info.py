import price_info as PInfo

def test_cost_of_fruit():
    fruit_name = 'watermelon'
    fruit_quantity = 5
    expected_result = 32.5  # Assuming the price of watermelon is 6.50
    test_result = PInfo.cost_of_fruits(fruit_name, fruit_quantity)
    assert test_result == expected_result

    #assert (Pinfo.cost_of_fruits('apple', 10) == 12.0)  # Assuming the price of apple is 1.20

def test_total_cost_shopping():
    expected_result = 46.75
    test_result = PInfo.total_cost_shopping()
    assert test_result == expected_result
    

