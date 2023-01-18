
def comma(arr):
#    arr = ['{0}, '.format(element) for element in arr] #Change/ alter every elements in a list

    for index, element in enumerate(arr):
        if arr:
            if index < len(arr)-1:
                arr[index] = '{0}, '.format(element)
            else:
                arr[index] = 'and {0}'.format(element)
        else:
            print('The list is empty')


    return arr




list = ['apples', 'bananas', 'tofu', 'cat']

for element in comma(list):
    print(element, end = '')

print()









