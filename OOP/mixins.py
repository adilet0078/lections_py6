# # mixins
# # Миксины - калссы которые используются для наследования и передачи дочерным классам определенных методов , но от них  не созжаются объекты

# # для чего: 
 
# # 1. вы хотите предоставить множество доп методов для классов 
  
# # 2. вы хотите использовать один конкретный метод во множестве разных классов
  
# class EngineMixin:
#     def start_engine(self):
#         print('Engine started')
              
# class RadioMixin:
#     def play_radio(self):
#         print('Radio is playing')

# class Car(EngineMixin, RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass

# class SmartPhone( RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass


# class FlyMixin:
#     def fly(self):
#         print('I can fly!')

# class WalkMixin:
#     def walk(self):
#         print('I can walk!')

# class SwimMixin:
#     def swim(self):
#         print('I can swim!')


# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk!')

# class Fish(SwimMixin):
#     name = 'fish'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'flying fish'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()
