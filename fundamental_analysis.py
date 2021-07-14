class FA:
    def __init__(self):
        return
    
    def profit(self, init_value, end_value):
        return (end_value - init_value) / init_value
    
if __name__ == "__main__":
    fa = FA()
    profit = fa.profit(1000, 1084)
    print(f'{profit * 100}%')