# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13 ,14, 15 ,16, 17, 18, 19, 20]
# left = 0
# right = len(ls) -1
# mid = len(ls) // 2
# value = 10

# while ls[mid] != value and left <= right:
#     if value < ls[mid]:
#         right = mid - 1
#     else:
#         left = mid + 1
#     mid = (left + right) // 2

# if left > right

def search_object(func):
    def wrapper(*args, **kwargs):
        self, id = args[0], args[1]
        objects_id = [x['id'] for x in self.objects] 
        left = 0
        right = len(objects_id) - 1
        mid = len(objects_id) // 2

        while objects_id[mid] != id and left <= right:
            if id < objects_id[mid]:
                right = mid - 1
            else :
                left = mid + 1
            mid = (left + right) // 2 
        
        if left > right:
            kwargs.update(object_ = None)
            return func(*args, **kwargs)
        kwargs.update(object_ = self.objects[mid])
        return func(*args, **kwargs)
    return wrapper






















