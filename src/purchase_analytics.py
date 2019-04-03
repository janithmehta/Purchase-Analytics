import sys
import csv


def compute_product_orders(filename, header):

    product_orders = dict()
    with open(filename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        if next(data) != header:
            raise Exception('CSV Headers do not match')
        for row in data:
            if len(row) != len(header) :
                print('Number of items in the row not equal to number of items in the header', row)
                continue
            elif row[1] and row[3]:
                product_id = int(float(row[1]))
                reordered =  int(float(row[3]))
                if product_id not in product_orders:
                    product_orders[product_id] = {
                        'number_of_orders': 0,
                        'number_of_first_orders': 0,
                    }
                product_orders[product_id]['number_of_orders'] +=  1
                if reordered == 0:
                    product_orders[product_id]['number_of_first_orders'] += 1

    return product_orders


def assign_departments(filename, header, product_orders):

    department_orders = dict()
    with open(filename) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        if next(data) != header:
            raise Exception('CSV Headers do not match')
        for row in data:
            if len(row) != len(header) :
                print('Number of items in the row not equal to number of items in the header', row)
                continue
            elif row[0] and row[3] :
                product_id = int(float(row[0]))
                if product_id in product_orders:
                    department_id = int(float(row[3]))
                    product_orders[product_id]['department_id'] = department_id

    return department_orders

def group_by_department(product_orders, department_orders):

    for i in product_orders:
        if 'department_id' in product_orders[i]:
            department_id = product_orders[i]['department_id']
            if department_id in department_orders:
                department_orders[department_id]['number_of_orders'] += product_orders[i]['number_of_orders']
                department_orders[department_id]['number_of_first_orders'] += product_orders[i]['number_of_first_orders']
                department_orders[department_id]['percentage'] = round(department_orders[department_id]['number_of_first_orders']/department_orders[department_id]['number_of_orders'], 2)
            else:
                department_orders[department_id] = {
                    'number_of_orders': product_orders[i]['number_of_orders'],
                    'number_of_first_orders': product_orders[i]['number_of_first_orders'],
                    'percentage': product_orders[i]['number_of_first_orders']/product_orders[i]['number_of_orders']
                }
    return sorted(department_orders.items())


def save_output(filename, department_orders):

    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
        writer.writerow(header)
        for key, value in department_orders:
            writer.writerow([key, value['number_of_orders'], value['number_of_first_orders'], '{:.2f}'.format(value['percentage'])])

def main():


    arguments = sys.argv

    product_orders_input_filename = arguments[1]
    product_orders_input_header = ['order_id','product_id','add_to_cart_order','reordered']

    products_input_filename = arguments[2]
    products_input_header = ['product_id', 'product_name', 'aisle_id', 'department_id']

    output_filename = arguments[3]

    product_orders = compute_product_orders(product_orders_input_filename, product_orders_input_header)
    department_orders = assign_departments(products_input_filename, products_input_header, product_orders)
    department_orders = group_by_department(product_orders, department_orders)
    save_output(output_filename, department_orders)


if __name__ == "__main__":
    main()
