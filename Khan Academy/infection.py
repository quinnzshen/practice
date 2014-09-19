## Quinn Z Shen
## Khan Academy Language Agnostic Project

current_version = "1.2"

class User:
    """Khan Academy Users"""
    version = "0.0"
    total_users = 0
    def __init__(self, version = None, students = [], teachers = []):
        self.students = set()
        self.teachers = set()
        self.uid = 1000 + User.total_users
        User.total_users += 1
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
        students_uid = [student.uid for student in self.students]
        teachers_uid = [teacher.uid for teacher in self.teachers]
        return "uid: " + str(self.uid) + ", version: " + self.version + \
                    ", students: " + str(students_uid) + \
                    ", teachers: " + str(teachers_uid)

class KhanNetwork:
    """Network of Khan Users"""
    existing_users = set()

    def __init__(self):
        pass

    def create_user(self, version = None, students = [], teachers = []):
        user = User(version, students, teachers)
        KhanNetwork.existing_users.add(user)
        return user

    def print_userbase(self):
        for user in KhanNetwork.existing_users:
            print user
        return True

    def total_infection(self, user):
        """ Spread the infection (i.e. the current version), beginning 
            at the given user, to the entire connected component. """
        KhanNetwork.infect(self, user, explored = set())

    def infect(self, user, explored):
        user.version = current_version
        explored.add(user)
        for student in user.students:
            if student not in explored:
                KhanNetwork.infect(self, student, explored)
        for teacher in user.teachers:
            if teacher not in explored:
                KhanNetwork.infect(self, teacher, explored)

    def limited_infection(self, user, limit):
        """ Spread the infection (i.e. the current version), beginning
            at the given user, and try to infect close to the limit 
            amount of users.  """
        pass

if __name__ == "__main__":
    network = KhanNetwork()
    a = network.create_user()
    b = network.create_user("1.0")
    c = network.create_user("1.2", [b], [])
    d = network.create_user("1.1", [a,c])
    e = network.create_user("1.1")
    f = network.create_user("1.1", [e])

    network.print_userbase()
    network.total_infection(f)
    print "--- After total infection ---"
    network.print_userbase()
