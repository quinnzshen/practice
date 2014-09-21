"""
Quinn Z Shen
Khan Academy Language Agnostic Project
"""

import operator, unittest

class User:
    """Khan Academy Users"""

    version = "0.0"
    total_users = 0
    def __init__(self, version=None, students=[], teachers=[]):
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

    CURRENT_VERSION = "1.2"

    def __init__(self):
        self.existing_users = set()

    def create_user(self, version = None, students = [], teachers = []):
        user = User(version, students, teachers)
        self.existing_users.add(user)
        return user

    def print_userbase(self):
        for user in self.existing_users:
            print user
        return True

    def total_infection(self, user):
        """ Spread the infection (i.e. the current version), beginning 
            at the given user, to the entire connected component. Return 
            the number of users that were infected. """

        return KhanNetwork.infect_cc(self, user, explored = set())

    def infect_cc(self, user, explored):
        """ Helper function that infects the entire connected component.
            Returns the number of newly infected users in the process."""

        user.version = KhanNetwork.CURRENT_VERSION
        explored.add(user)
        infected_count = 1

        for student in user.students:
            if student not in explored:
                infected_count += KhanNetwork.infect_cc(self, student, explored)

        for teacher in user.teachers:
            if teacher not in explored:
                infected_count += KhanNetwork.infect_cc(self, teacher, explored)

        return infected_count

    def limited_infection(self, limit):
        """ Spread the infection (i.e. the current version), and try to infect 
            close to the limit amount of users. Return number of users infected. """

        # Teachers are a root_teacher if they don't have any teachers (i.e. parent nodes)
        root_teachers = [user for user in self.existing_users if not user.teachers]
        options = []
        infection_counter = 0

        for teacher in root_teachers:
            student_count = KhanNetwork.explore(self, teacher, explored = set())
            options.append((teacher, student_count))

        # Sort options by their student_count (i.e. amount of children) in decending order
        options.sort(key=operator.itemgetter(1), reverse=True)

        for teacher,count in options:
            if (infection_counter + count) <= limit:
                KhanNetwork.total_infection(self, teacher)
                infection_counter += count

        return infection_counter

    def limited_infection_exact(self, limit):
        """ Attempt to spread the infection (i.e. the current version) to the 
            exact amount of users (specified by the limit). Do nothing if not possible.
            Return number of users infected. """

        # Teachers are a root_teacher if they don't have any teachers (i.e. parent nodes)
        root_teachers = [user for user in self.existing_users if not user.teachers]
        options = []
        infection_counter = 0

        for teacher in root_teachers:
            student_count = KhanNetwork.explore(self, teacher, explored = set())
            options.append((teacher, student_count))

        # Discover which users to infect for an exact matching.
        solution_option = KhanNetwork.find_combination(self, options, limit, partial=[])

        for user in solution_option:
            infection_counter += KhanNetwork.total_infection(self, user)

        return infection_counter

    def explore(self, user, explored):
        """ Helper function that performs DFS on the students of the user. 
            Returns the size (total children under the given user). """

        explored.add(user)
        explored_count = 1

        for student in user.students:
            if student not in explored:
                explored_count += KhanNetwork.explore(self, student, explored)

        return explored_count

    def find_combination(self, options, target, partial=[]):
        """ Find a solution_option containing (teacher, student_count) tuples
            that will reach our target limit exactly. If not possible return None.
            Note: If there is more than one solution, it will return the first 
            solution that the algorithm comes across.

            >>> network = KhanNetwork()
            >>> options = [("A", 2), ("B", 3), ("C", 2), ("D", 5), ("E", 9)]
            >>> network.find_combination(options, 15, partial=[])
            []
            >>> network.find_combination(options, 13, partial=[])
            ['A', 'C', 'E']
        """

        current_count = sum([count for teacher,count in partial])
        if current_count == target:
            return [teacher for teacher,count in partial]
        elif current_count > target:
            return []
        else:
            for index in xrange(len(options)):
                option = options[index]
                remaining_options = options[index + 1:]
                answer = KhanNetwork.find_combination(self, remaining_options, target, partial + [option])
                if answer:
                    return answer
            return []

class TestInfection(unittest.TestCase):
    """ A small testing suite. """

    def setUp(self):
        self.network = KhanNetwork()
        self.a = self.network.create_user()
        self.b = self.network.create_user("1.0")
        self.c = self.network.create_user("1.0", [self.b], [])
        self.d = self.network.create_user("1.1", [self.a,self.c])
        self.e = self.network.create_user("1.1")
        self.f = self.network.create_user("1.1", [self.e])
        print "--- network at set-up ---"
        self.network.print_userbase()

    def test_test(self):
        self.assertEqual(1, 1)

    def test_total_infection_4(self):
        self.infected = self.network.total_infection(self.a)
        self.assertEqual(self.infected, 4)

    def test_total_infection_2(self):
        self.infected = self.network.total_infection(self.e)
        self.assertEqual(self.infected, 2)

    def test_limited_infection_1(self):
        self.infected = self.network.limited_infection(1)
        self.assertEqual(self.infected, 0)

    def test_limited_infection_2(self):
        self.infected = self.network.limited_infection(2)
        self.assertEqual(self.infected, 2)

    def test_limited_infection_3(self):
        self.infected = self.network.limited_infection(3)
        self.assertEqual(self.infected, 2)

    def test_limited_infection_4(self):
        self.infected = self.network.limited_infection(4)
        self.assertEqual(self.infected, 4)

    def test_limited_infection_5(self):
        self.infected = self.network.limited_infection(5)
        self.assertEqual(self.infected, 4)

    def test_limited_infection_6(self):
        self.infected = self.network.limited_infection(6)
        self.assertEqual(self.infected, 6)

    def test_exact_infection_2(self):
        self.infected = self.network.limited_infection_exact(2)
        self.assertEqual(self.infected, 2)

    def test_exact_infection_6(self):
        self.infected = self.network.limited_infection_exact(6)
        self.assertEqual(self.infected, 6)

    def test_exact_infection_5(self):
        self.infected = self.network.limited_infection_exact(5)
        self.assertEqual(self.infected, 0)     

    def tearDown(self):
        print "--- network at tear-down ---"
        self.network.print_userbase()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    unittest.main()
