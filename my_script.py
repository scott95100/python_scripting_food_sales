# Read only

def read_only():
    ''' a method that only reads the file '''
    try:
        file1 = open('data.txt', "r")
        text = file1.read()
        print(text)
        file1.close()# the reason for closing, it will remain open in memory until
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    ''' a method that only writes to a file '''
    file2 = open('more_data.txt', 'w') # if file exists then it will be overwritten. if file does not exist it will be created.
    file2.write('tomatoes')
    file2.close()

#python will know to close this file, even if there are errors
# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)

def read_food_sales():
    all_dates = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for food_sale in data:
            split_food_sale = food_sale.split(',')
            order_date = split_food_sale[0]
            
            all_dates.append(order_date)
    print(all_dates)

    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')

def append_txt():
    ''' append text for data to an existing file '''
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')

def region_food_sales():
    all_regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()
        for region_sale in data:
            split_region_sale = region_sale.split(',')
            region = split_region_sale[0]
            all_regions.append(region)
    print(all_regions)
    with open('regions.txt', 'w') as f:
        for data in all_regions:
            f.write(region)
            f.write('\n')

if __name__ == '__main__':
    # read_only()
    # write_only()
    # read_food_sales()
    # append_txt()
    region_food_sales()