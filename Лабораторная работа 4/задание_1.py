# TODO: описать базовый класс
class ElectronicDevice:
    """Базовый класс для электронных устройств"""

    def __init__(self, brand: str, model: str, power_watts: float):
        """
        Инициализация электронного устройства

        Args:
            brand: Производитель устройства
            model: Модель устройства
            power_watts: Потребляемая мощность (в ваттах)
        """
        self._brand = brand
        self._model = model
        self.power = power_watts
        self._is_on = False  # Приватный атрибут - состояние устройства

    def turn_on(self) -> None:
        """Включить устройство"""
        if not self._is_on:
            self._is_on = True
            print(f"{self._brand} {self._model}: Устройство включено")
        else:
            print(f"{self._brand} {self._model}: Устройство уже включено")

    def turn_off(self) -> None:
        """Выключить устройство"""
        if self._is_on:
            self._is_on = False
            print(f"{self._brand} {self._model}: Устройство выключено")
        else:
            print(f"{self._brand} {self._model}: Устройство уже выключено")

    def get_power_consumption(self, hours: float) -> float:
        """
        Рассчитать потребление энергии за указанное время

        Args:
            hours: Количество часов работы

        Returns:
            Потребленная энергия в ватт-часах
        """
        return self.power * hours if self._is_on else 0.0

    def __str__(self) -> str:
        return f"{self._brand} {self._model} ({self.power} Вт)"

    def __repr__(self) -> str:
        return f"ElectronicDevice(brand='{self._brand}', model='{self._model}', power_watts={self.power})"

# TODO: описать дочерний класс


class Smartphone(ElectronicDevice):
    """Дочерний класс для смартфонов, наследуется от ElectronicDevice"""

    def __init__(self, brand: str, model: str, power_watts: float,
                 os: str, battery_mah: int):
        """
        Инициализация смартфона

        Args:
            brand: Производитель
            model: Модель
            power_watts: Потребляемая мощность (в ваттах)
            os: Операционная система
            battery_mah: Емкость батареи (в мАч)
        """
        super().__init__(brand, model, power_watts)
        self.os = os
        self._battery_mah = battery_mah  # Инкапсуляция - защита от изменения
        self._battery_level = 100  # Приватный атрибут - текущий заряд

    def charge(self, percent: int) -> None:
        """
        Зарядить батарею на указанный процент

        Args:
            percent: Процент заряда (1-100)
        """
        if not 1 <= percent <= 100:
            raise ValueError("Процент заряда должен быть от 1 до 100")

        new_level = min(100, self._battery_level + percent)
        delta = new_level - self._battery_level
        self._battery_level = new_level
        print(f"Заряд увеличен на {delta}%. Текущий уровень: {self._battery_level}%")

    def get_battery_life(self, usage_per_hour: float) -> float:
        """
        Рассчитать время работы от батареи

        Args:
            usage_per_hour: Потребление энергии в час (в процентах)

        Returns:
            Время работы в часах
        """
        if usage_per_hour <= 0:
            raise ValueError("Потребление должно быть положительным числом")
        return self._battery_level / usage_per_hour

    def turn_on(self) -> None:
        """
        Перегрузка метода turn_on с проверкой уровня заряда.
        Причина перегрузки: смартфон не должен включаться с разряженной батареей.
        """
        if self._battery_level < 5:
            print(f"{self._brand} {self._model}: Низкий заряд батареи! Включение невозможно")
            return
        super().turn_on()  # Вызов родительского метода

    def __str__(self) -> str:
        return (f"Смартфон {self._brand} {self._model} ({self.os}), "
                f"Батарея: {self._battery_mah} мАч, {self.power} Вт")

    def __repr__(self) -> str:
        return (f"Smartphone(brand='{self._brand}', model='{self._model}', "
                f"power_watts={self.power}, os='{self.os}', "
                f"battery_mah={self._battery_mah})")


# Демонстрация работы классов
if __name__ == "__main__":
    # Базовый класс
    tv = ElectronicDevice("Sony", "Bravia", 120)
    print(tv)  # Sony Bravia (120 Вт)
    tv.turn_on()  # Sony Bravia: Устройство включено
    print(f"Потребление за 5 часов: {tv.get_power_consumption(5)} Вт·ч")  # 600.0

    # Дочерний класс
    phone = Smartphone("Apple", "iPhone 15", 5, "iOS", 4000)
    print(phone)  # Смартфон Apple iPhone 15 (iOS), Батарея: 4000 мАч, 5 Вт
    phone.turn_on()  # Apple iPhone 15: Устройство включено

    phone._battery_level = 3
    phone.turn_on()  # Apple iPhone 15: Низкий заряд батареи! Включение невозможно

    phone.charge(50)  # Заряд увеличен на 50%. Текущий уровень: 53%
    print(f"Время работы: {phone.get_battery_life(10): .1f} часов")  # 5.3
