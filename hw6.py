def display_line_product_set(start, end):
    for sub_num in range(1, 10):
        for main_num in range(start, end + 1):
            product = main_num * sub_num
            print(f'{main_num} x {sub_num} = ', end='')
            print(str(product).rjust(2), end='     ')
        print()

# main

display_line_product_set(2, 5)
print()
display_line_product_set(6, 9)
