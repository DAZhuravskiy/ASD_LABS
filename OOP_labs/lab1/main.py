import math

class Point2D:
    total_points_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.total_points_count += 1

    def __str__(self):
        return f"(({self.x:.2f}, {self.y:.2f}))"

    def __repr__(self):
        return f"Point2D(x={self.x:.2f}, y={self.y:.2f})"

    def distance_to(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0)

    @classmethod
    def clone(cls, point):
        return cls(point.x, point.y)

    @classmethod
    def from_polar(cls, r, theta_degrees):
        theta_radians = math.radians(theta_degrees)
        x = r * math.cos(theta_radians)
        y = r * math.sin(theta_radians)
        return cls(x, y)

    @staticmethod
    def distance_between(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

if __name__ == "__main__":
    print("1. Создание точек")
    p1 = Point2D(1.23, 6.79)
    p2 = Point2D(4.0, 2.0)
    print(f"Созданы точки p1 и p2. Текущий счетчик: {Point2D.total_points_count}")

    print("\n2. Вывод через str() и repr()")
    print(f"str(p1):  {str(p1)}")
    print(f"repr(p1): {repr(p1)}")
    print(f"str(p2):  {str(p2)}")
    print(f"repr(p2): {repr(p2)}")

    print("\n3. Расстояние между точками")
    dist = p1.distance_to(p2)
    print(f"Расстояние от p1 до p2: {dist:.4f}")

    print("\n4. Начало координат (метод класса)")
    p_origin = Point2D.origin()
    print(f"Создана точка origin: {repr(p_origin)}")
    print(f"Текущий счетчик: {Point2D.total_points_count}")

    print("\n5. Копия точки (метод класса)")
    p_clone = Point2D.clone(p1)
    print(f"Оригинал p1: {repr(p1)}")
    print(f"Копия p_clone: {repr(p_clone)}")
    
    print(f"p1 is p_clone? {p1 is p_clone} (Должно быть False, так как это разные объекты в памяти)")
    print(f"Текущий счетчик: {Point2D.total_points_count}")

    print("\n6. Из полярных координат")
    p_polar = Point2D.from_polar(10.0, 90.0)
    print(f"Точка из полярных координат (r=10, угол=90°): {repr(p_polar)}")
    print(f"Текущий счетчик: {Point2D.total_points_count}")

    print("\n7. Расстояние между кортежами (статический метод)")
    tuple1 = (0, 0)
    tuple2 = (3, 4)
    static_dist = Point2D.distance_between(tuple1, tuple2)
    print(f"Расстояние между кортежами {tuple1} и {tuple2}: {static_dist}")
    
    print("\nИТОГОВЫЙ СЧЕТЧИК ОБЪЕКТОВ")
    print(f"Всего было создано объектов Point2D: {Point2D.total_points_count}")