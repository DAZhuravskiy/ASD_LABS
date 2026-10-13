import math

class Point3d:
    _total_points_count = 0

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        Point3d._total_points_count += 1

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __repr__(self):
        return f"Point3d(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"

    def distance_to(self, other):
        return math.sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2 +
            (other.z - self.z) ** 2
        )

    @staticmethod
    def distance_between(p1, p2):
        return math.sqrt(
            (p2[0] - p1[0]) ** 2 +
            (p2[1] - p1[1]) ** 2 +
            (p2[2] - p1[2]) ** 2
        )

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def clone(cls, point):
        return cls(point.x, point.y, point.z)

    @classmethod
    def from_polar(cls, r, theta_degrees, phi_degrees):
        theta_rad = math.radians(theta_degrees)
        phi_rad = math.radians(phi_degrees)

        x = r * math.cos(phi_rad) * math.cos(theta_rad)
        y = r * math.cos(phi_rad) * math.sin(theta_rad)
        z = r * math.sin(phi_rad)

        return cls(x, y, z)

class Vector3d:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __repr__(self):
        return f"Vector3d(x={self.x:.2f}, y={self.y:.2f}, z={self.z:.2f})"

    @classmethod
    def from_points(cls, start, end):
        return cls(
            end.x - start.x,
            end.y - start.y,
            end.z - start.z
        )

    def __eq__(self, other):
        if not isinstance(other, Vector3d):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __add__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector3d(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector3d(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other):
        return Vector3d(other - self.x, other - self.y, other - self.z)

    def __mul__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x * other.x, self.y * other.y, self.z * other.z)
        return Vector3d(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector3d):
            return Vector3d(self.x / other.x, self.y / other.y, self.z / other.z)
        return Vector3d(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other):
        return Vector3d(other / self.x, other / self.y, other / self.z)

    def __iadd__(self, other):
        if isinstance(other, Vector3d):
            self.x += other.x; self.y += other.y; self.z += other.z
        else:
            self.x += other; self.y += other; self.z += other
        return self

    def __isub__(self, other):
        if isinstance(other, Vector3d):
            self.x -= other.x; self.y -= other.y; self.z -= other.z
        else:
            self.x -= other; self.y -= other; self.z -= other
        return self

    def __imul__(self, other):
        if isinstance(other, Vector3d):
            self.x *= other.x; self.y *= other.y; self.z *= other.z
        else:
            self.x *= other; self.y *= other; self.z *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Vector3d):
            self.x /= other.x; self.y /= other.y; self.z /= other.z
        else:
            self.x /= other; self.y /= other; self.z /= other
        return self

    def __matmul__(self, other):
        return Vector3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def __getitem__(self, key):
        if key == 0 or key == 'x': return self.x
        if key == 1 or key == 'y': return self.y
        if key == 2 or key == 'z': return self.z
        raise IndexError("Неверный индекс или ключ компоненты")

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

if __name__ == "__main__":
    print("ДЕМОНСТРАЦИЯ КЛАССА Point3d")

    p1 = Point3d(1.23, 4.56, 7.89)
    p2 = Point3d(2.0, 3.0, 4.0)
    p_origin = Point3d.origin()
    p_polar = Point3d.from_polar(10.0, 45.0, 30.0)
    p_clone = Point3d.clone(p1)

    print(f"p1: {repr(p1)}")
    print(f"p2: {repr(p2)}")
    print(f"p_origin: {repr(p_origin)}")
    print(f"p_polar (r=10, θ=45°, φ=30°): {repr(p_polar)}")
    print(f"p_clone: {repr(p_clone)}")
    
    print(f"p1 is p_clone? {p1 is p_clone} (Ожидается False)")

    print(f"\nРасстояние от p1 до p2: {p1.distance_to(p2):.4f}")
    tuple1 = (0, 0, 0)
    tuple2 = (1, 2, 2)
    print(f"Расстояние между кортежами {tuple1} и {tuple2}: {Point3d.distance_between(tuple1, tuple2):.4f}")

    print(f"\nВсего создано объектов Point3d: {Point3d._total_points_count}")

    print("\nДЕМОНСТРАЦИЯ КЛАССА Vector3d")

    v1 = Vector3d(3, 4, 5)
    v2 = Vector3d(1, 2, 3)
    v_from_points = Vector3d.from_points(p1, p2)

    print(f"v1: {repr(v1)}")
    print(f"v2: {repr(v2)}")
    print(f"Вектор из p1 в p2: {repr(v_from_points)}")

    v_small = Vector3d(1, 1, 1)
    print(f"\nСравнение v1 > v_small: {v1 > v_small} (Ожидается True, т.к. длина v1 больше)")
    print(f"Сравнение v1 == v2: {v1 == v2} (Ожидается False)")

    print(f"\nv1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * v2 = {v1 * v2} (Покомпонентно)")
    print(f"v1 + 3 = {v1 + 3}")
    print(f"3 + v1 = {3 + v1}")
    print(f"10 - v1 = {10 - v1} (Число слева)")
    print(f"v1 * 2 = {v1 * 2}")

    v3 = Vector3d(1, 1, 1)
    print(f"\nДо изменения: v3 = {repr(v3)}, id = {id(v3)}")
    v3 += 5
    print(f"После v3 += 5: v3 = {repr(v3)}, id = {id(v3)} (id не изменился)")
    v3 *= Vector3d(2, 2, 2)
    print(f"После v3 *= Vector3d(2,2,2): v3 = {repr(v3)}, id = {id(v3)}")

    v_cross = v1 @ v2
    print(f"\nВекторное произведение v1 @ v2 = {v_cross}")

    print(f"Длина v1 (через len): {len(v1)}")
    print(f"Точная длина v1: {math.sqrt(v1.x**2 + v1.y**2 + v1.z**2):.4f}")

    print(f"\nv1[0] = {v1[0]}")
    print(f"v1['y'] = {v1['y']}")
    print("Перебор компонент v1:", end=" ")
    for comp in v1:
        print(comp, end=" ")
    print()

    print("\nПроверки")
    v_col1 = Vector3d(2, 4, 6)
    v_col2 = Vector3d(1, 2, 3)
    is_collinear = (v_col1 @ v_col2) == Vector3d(0, 0, 0)
    print(f"Векторы {v_col1} и {v_col2} коллинеарны? {is_collinear}")

    v_cop1 = Vector3d(1, 0, 0)
    v_cop2 = Vector3d(0, 1, 0)
    v_cop3 = Vector3d(1, 1, 0)
    cross_prod = v_cop1 @ v_cop2
    scalar_triple = cross_prod.x * v_cop3.x + cross_prod.y * v_cop3.y + cross_prod.z * v_cop3.z
    is_coplanar = abs(scalar_triple) < 1e-9
    print(f"Векторы {v_cop1}, {v_cop2}, {v_cop3} компланарны? {is_coplanar}")