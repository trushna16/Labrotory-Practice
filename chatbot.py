def suggest_college(cet_marks, hsc_marks):
    cet_percentage = (cet_marks / 200) * 100
    hsc_percentage = (hsc_marks / 600) * 100

    eligibility_criteria = {
        "top_colleges": {"cet_percentage": 90, "hsc_percentage": 90},
        "good_colleges": {"cet_percentage": 80, "hsc_percentage": 80},
        "average_colleges": {"cet_percentage": 70, "hsc_percentage": 70},
        "basic_colleges": {"cet_percentage": 60, "hsc_percentage": 60}
    }

    eligible_colleges = []
    for college, criteria in eligibility_criteria.items():
        if cet_percentage >= criteria["cet_percentage"] and hsc_percentage >= criteria["hsc_percentage"]:
            eligible_colleges.append(college)

    return eligible_colleges


def chat():
    print("Welcome to the College Selection Chatbot!")
    print("Please enter your CET and HSC marks to get college suggestions.")
    cet_marks = float(input("Enter your CET marks: "))
    hsc_marks = float(input("Enter your HSC marks: "))

    colleges = suggest_college(cet_marks, hsc_marks)

    if len(colleges) > 0:
        print("Based on your marks, you are eligible for the following colleges:")
        for college in colleges:
            print("- " + college)
    else:
        print("Sorry, based on your marks, you are not eligible for any colleges.")


# Run the chatbot
chat()
