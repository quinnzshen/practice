## Quinn Z Shen
## Khan Academy Language Agnostic Project

current_version = "1.2"

class User:
    """Khan Academy Users"""
    version = "0.0"
    def __init__(self, version = None, students = [], teachers = []): # TODO: Implement with uid
        self.students = set()
        self.teachers = set()
        if isinstance(version, basestring):
            self.version = version
        if students:
            for student in students:
                self.students.add(student)
                student.teachers.add(self) # Maintain undirected relationship.
        if teachers:
            for teacher in teachers:
                self.teachers.add(teacher)
                teacher.students.add(self) # Maintain undirected relationship.
    def __str__(self):
        return "version: " + self.version + ", students: " + \
                str(self.students) + ", teachers: " + str(self.teachers)

# class KhanNetwork:
#     """Network of Khan Users"""
#     existing_users = set()

def total_infection(user):
    """ Spread the infection (i.e. the current version), beginning 
        at the given user, to the entire connected component. """
    infect(user, explored = set())

def infect(user, explored):
    user.version = current_version
    explored.add(user)
    for student in user.students:
        if student not in explored:
            infect(student, explored)
    for teacher in user.teachers:
        if teacher not in explored:
            infect(teacher, explored)

def limited_infection():
    pass

if __name__ == "__main__":
    a = User()
    b = User("1.0")
    c = User("1.2", [], [b])
    d = User("1.1", [a,c])
    for user in [a,b,c,d]:
        print str(user)
    print "--- AFTER TOTAL INFECTION ON USER A ---"
    total_infection(a)
    for user in [a,b,c,d]:
        print str(user)
