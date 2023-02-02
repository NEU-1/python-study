# 클래스
class Car:
    # 클래스 변수
    wheel_count = 4 # shared by all instances of the class

    # 생성자
    def __init__(self, make, model):
        # 인스턴트 변수
        self.make = make
        self.model = model
        
    # 인스턴트 메소드
    def start(self):
        print(f"{self.make} {self.model} has started")
        
    # 클래스 메소드
    @classmethod # 데코레이터
    def wheel_info(cls):
        print(f"All cars have {cls.wheel_count} wheels")
        
    # 스태틱 메소드
    @staticmethod # 데코레이터
    def fuel_check():
        print("Fuel level is sufficient")
        
# 객체/인스턴트 생성
my_car = Car("Toyota", "Camry")

# 클래스 변수와 인스턴스 변수 호출
print(f"My car has {Car.wheel_count} wheels") # 4
print(f"My car is a {my_car.make} {my_car.model}") # Toyota Camry

# 인스턴트 메서드 호출
my_car.start() # Toyota Camry has started

# 클래스 메서드 호출
Car.wheel_info() # All cars have 4 wheels

# 스태틱 메서드 호출
Car.fuel_check() # Fuel level is sufficient
