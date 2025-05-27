my_string = "Hello, World!"
print(my_string)

def person_lister(format_func):
    def inner(people):
        # age wise sorted list of people
        sorted_people = sorted(people, key=lambda person: int(person[2]))
        # sorted_people list age wise sorted tuples
        return [format_func(person) for person in sorted_people]
    return inner

@person_lister
def format_name(person):
    title = "Mr. " if person[3] == "M" else "Ms. "
    full_name = f"{person[0]} {person[1]}"
    return title + full_name

if __name__ == '__main__':
    n = int(input())
    # n number of people input
    people = [input().split() for _ in range(n)]
    # people list of tuples
    # people = [('John', 'Doe', '25', 'M'), ('Jane', 'Smith', '22', 'F'), ...]
    print(*format_name(people), sep='\n')







