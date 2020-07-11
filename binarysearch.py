def binarySearch(list, element):
  start = 0
  end = len(list)-1
  mid = (start + end)/2
  while start <= end:
    print 'Searching ' + str(element) + ' in list = ' + str(list[start:end+1])
    if start == end:
      if list[start] == element:
        print 'Element found at position = ' + str(start)
      else:
        print 'Element not found'
      return
    
    if list[mid] < element:
      start = mid+1
      mid = (start + end)/2
    elif list[mid] > element:
      end = mid-1
      mid = (start + end)/2
    else:
      print 'Found element at position = ' + str(mid)

list = [22, 12, 23, 677, 33, 1, 46]
list.sort()

print 'List = ' + str(list)
print binarySearch(list, 22)