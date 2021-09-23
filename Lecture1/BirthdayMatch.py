# Static Array

# the most primitive data structure native to the Word-RAM: the static array.
# A static array is simply a contiguous sequence of words reserved in memory, supporting a static sequence interface:
#       • StaticArray(n): allocate a new static array of size n initialized to 0 in Θ(n) time
#       • StaticArray.get_at(i): return the word stored at array index i in Θ(1) time
#       • StaticArray.set_at(i, x): write the word x to array index i in Θ(1) time

class StaticArray:
    def __init__(self, n):
        self.data = [None] * n

    def get_at(self, i):
        if not (0 <= i < len(self.data)):
            raise IndexError
        return self.data[i]

    def set_at(self, i, x):
        if not (0 <= i < len(self.data)):
            raise IndexError
        self.data[i] = x


# the algorithm
# Maintain an initially empty record of student names and birthdays.
# Go around the room and ask each student their name and birthday.
# After interviewing each student, check to see whether their birthday already exists in the record.
# If yes, return the names of the two students found.
# Otherwise, add their name and birthday to the record.
# If after interviewing all students no satisfying pair is found, return that no matching pair exists.

def birthday_match(students):
    """
    An algorithm that return check if there is a pair of students with the same birthday

    :param students: a list of student with each element being (name, birthday)
    :return: a pair of student name in tuple if a match exist, none otherwise
    """
    n = len(students)
    record = StaticArray(n)
    for i in range(n):
        (name1, birthday1) = students[i]
        for j in range(i):
            (name2, birthday2) = record.get_at(j)
            if birthday1 == birthday2:
                return name1, name2
        record.set_at(i, (name1, birthday1))
    return None

