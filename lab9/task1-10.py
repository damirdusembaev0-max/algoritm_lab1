# Задача 1: Класс Node (Узел) 
class Node:
    def __init__(self, data):
        self.data = data  # Поле для хранения данных [cite: 29, 30]
        self.next = None  # Ссылка на следующий элемент [cite: 29, 31]

# Задача 2: Класс LinkedList 
class LinkedList:
    def __init__(self):
        self.head = None  # Инициализация пустого списка (ссылка head) [cite: 34, 35]

    # Задача 3: Добавление элемента в начало списка [cite: 36, 37]
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Задача 4: Добавление элемента в конец списка [cite: 40, 41]
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Задача 5: Вывод всех элементов списка [cite: 44, 45]
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Список пуст")

    # Задача 6: Поиск элемента в списке [cite: 48, 49]
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True  # Элемент найден [cite: 52]
            current = current.next
        return False  # Элемент отсутствует [cite: 53]

    # Задача 7: Удаление первого элемента списка [cite: 54, 55]
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    # Задача 8: Подсчёт количества элементов [cite: 61, 62]
    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Задача 9: Реализация программы 
def main():
    llist = LinkedList()
    
    # 1. Считывает 5 чисел от пользователя [cite: 67]
    print("Введите 5 чисел для добавления в список:")
    for i in range(5):
        num = int(input(f"Число {i+1}: "))
        llist.append(num) # 2. Добавляет их в связный список [cite: 68]
    
    # 3. Выводит список [cite: 69]
    print("\nВаш связный список:")
    llist.display()
    
    # Проверка дополнительных функций
    print(f"Всего элементов: {llist.count_elements()}")
    
    # Демонстрация разворота (Задача 10)
    print("\nРазворот списка...")
    llist.reverse()
    llist.display()

if __name__ == "__main__":
    main()
    
    # Задача 10: Разворот связного списка (повышенная сложность) [cite: 70, 71]
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next # Сохраняем ссылку на следующий узел
            current.next = prev      # Разворачиваем текущий узел
            prev = current           # Сдвигаем prev вперед
            current = next_node      # Сдвигаем current вперед
        self.head = prev