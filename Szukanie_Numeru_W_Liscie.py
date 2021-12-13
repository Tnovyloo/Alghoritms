import time
def time_convert(sec):
      mins = sec // 60
      sec = sec % 60
      hours = mins // 60
      mins = mins % 60
      print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def Search(array, target):
    left = 0
    right = len(array)
    index = 0

    start_time = time.time()
    while left < right:
        index = (right + left) // 2

        if array[index] == target:
            print(index)
            end_time = time.time()
            elapsed_time = end_time - start_time
            return index, time_convert(elapsed_time)

        else:
            if array[index] < target:
                left = index + 1
            else:
                right = index
    return -1


exampleArray = [x for x in range(10000)]
target_Number = 540
Search(exampleArray, target_Number)