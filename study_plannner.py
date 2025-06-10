def greet_user():
    print("🎓 Welcome to the Study Planner Suggester!")
    name = input("What's your name? ")
    print(f"\nHi {name}! Let's create your custom study plan. 📚\n")
    return name

def get_available_hours():
    while True:
        try:
            hours = float(input("How many hours can you study today? (e.g., 3.5): "))
            if hours <= 0:
                print("Please enter a positive number.")
                continue
            return hours
        except ValueError:
            print("Please enter a valid number.")

def get_subjects():
    subjects = input("List the subjects you want to study today, separated by commas (e.g., Maths, English, Science): ")
    subject_list = [sub.strip() for sub in subjects.split(",") if sub.strip()]
    return subject_list

def get_weak_subjects(subjects):
    weak = input("Which subjects do you feel weakest in? (separate with commas): ")
    weak_list = [w.strip() for w in weak.split(",") if w.strip()]
    return [s for s in subjects if s in weak_list]

def suggest_plan(name, hours, subjects, weak_subjects):
    print(f"\n📅 Here's your suggested study plan for today, {name}:")
    plan = {}
    if not subjects:
        print("No subjects entered. Please try again.")
        return

    base_time = hours / len(subjects)
    extra_time = 0.25 * base_time  # 25% extra to weak subjects

    total_hours = 0
    for subject in subjects:
        if subject in weak_subjects:
            study_time = base_time + extra_time
        else:
            study_time = base_time
        plan[subject] = round(study_time, 2)
        total_hours += study_time

    # Normalize if over time
    if total_hours > hours:
        ratio = hours / total_hours
        for subject in plan:
            plan[subject] = round(plan[subject] * ratio, 2)

    for subject, time in plan.items():
        print(f"📝 {subject}: {time} hours")

    print("\n✅ Tip: Take 5–10 min breaks between each subject to stay focused!\n")

# Main app
def main():
    name = greet_user()
    hours = get_available_hours()
    subjects = get_subjects()
    weak_subjects = get_weak_subjects(subjects)
    suggest_plan(name, hours, subjects, weak_subjects)

if __name__ == "__main__":
    main()