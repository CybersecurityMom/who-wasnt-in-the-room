import matplotlib.pyplot as plt

# WHO WASN'T IN THE ROOM?
# Human-Centered AI Evaluation Visualizer

participant_groups = []
participant_counts = []

print("\nWHO WASN'T IN THE ROOM?")
print("Human-Centered AI Evaluation Visualizer")
print("----------------------------------------")

print("\nThis tool helps visualize who participated in an AI system evaluation.")
print("It does not determine whether the participant mix was sufficient or appropriate.")

# Identify the system or evaluation
system_name = input("\nWhat system or evaluation are you reviewing? ")

# WHO WAS IN THE ROOM?
print("\nWHO WAS IN THE ROOM?")
print("----------------------------------------")

number_of_groups = int(
    input("How many participant groups were involved in the evaluation? ")
)

# Collect participant information
for i in range(number_of_groups):
    print(f"\nParticipant Group {i + 1}")

    group_name = input("Enter the participant group name: ")

    participant_count = int(
        input("Enter the number of participants: ")
    )

    participant_groups.append(group_name)
    participant_counts.append(participant_count)

# Calculate total participants
total_participants = sum(participant_counts)

# Calculate percentage representation
percentages = []

for count in participant_counts:
    percentage = (count / total_participants) * 100
    percentages.append(percentage)

# Display participant representation
print("\nPARTICIPANT REPRESENTATION")
print("----------------------------------------")
print(f"System/Evaluation: {system_name}")

for i in range(number_of_groups):
    print(
        f"{participant_groups[i]}: "
        f"{participant_counts[i]} participants "
        f"({percentages[i]:.1f}%)"
    )

print(f"\nTotal participants: {total_participants}")

# CREATE THE VISUALIZATION
plt.figure(figsize=(10, 6))

plt.barh(participant_groups, percentages)

plt.xlabel("Percentage of Evaluation Participants")
plt.ylabel("Participant Group")

plt.title(
    f"Who Was in the Room?\n{system_name}"
)

# Give the percentage labels extra room
plt.xlim(0, max(percentages) + 10)

# Add percentage labels beside the bars
for i, percentage in enumerate(percentages):
    plt.text(
        percentage + 0.5,
        i,
        f"{percentage:.1f}%",
        va="center"
    )

plt.tight_layout()

# Show the chart
plt.show()

# WHO WASN'T IN THE ROOM?
print("\nWHO WASN'T IN THE ROOM?")
print("----------------------------------------")

print("\nThe visualization shows who participated.")
print("Now consider who may have been missing from the evaluation.")

intended_users_missing = input(
    "\nWere intended users or people representative of intended users "
    "missing from the evaluation? (yes/no/unknown): "
)

affected_people_missing = input(
    "\nWere people who could be affected by the system "
    "missing from the evaluation? (yes/no/unknown): "
)

perspectives_missing = input(
    "\nWere relevant perspectives or areas of expertise "
    "missing from the evaluation? (yes/no/unknown): "
)

missing_groups = input(
    "\nWho or what perspectives may have been missing? "
)

# WHO DECIDED WHAT NEEDED TESTING?
print("\nWHO DECIDED WHAT NEEDED TESTING?")
print("----------------------------------------")

testing_decision = input(
    "\nWho helped determine what risks, behaviors, "
    "or outcomes needed to be tested? "
)

outside_development_team = input(
    "\nWere people outside the development team involved "
    "in deciding what needed testing? (yes/no/unknown): "
)

# WHAT CHANGED?
print("\nWHAT CHANGED BECAUSE PEOPLE WERE IN THE ROOM?")
print("----------------------------------------")

changes_documented = input(
    "\nIs there documentation showing that participant feedback "
    "changed the system, testing, safeguards, or deployment? "
    "(yes/no/unknown): "
)

changes_description = input(
    "\nIf known, what changed because of participant feedback? "
)

# FINAL SUMMARY
print("\nHUMAN-CENTERED EVALUATION SUMMARY")
print("========================================")

print(f"\nSystem/Evaluation: {system_name}")
print(f"Total Evaluation Participants: {total_participants}")

print("\nWHO WAS IN THE ROOM?")

for i in range(number_of_groups):
    print(
        f"- {participant_groups[i]}: "
        f"{participant_counts[i]} participants "
        f"({percentages[i]:.1f}%)"
    )

print("\nWHO WASN'T IN THE ROOM?")

print(
    f"- Intended users missing: "
    f"{intended_users_missing}"
)

print(
    f"- Affected people missing: "
    f"{affected_people_missing}"
)

print(
    f"- Relevant perspectives missing: "
    f"{perspectives_missing}"
)

print(
    f"- Missing groups or perspectives: "
    f"{missing_groups}"
)

print("\nWHO DECIDED WHAT NEEDED TESTING?")

print(
    f"- People involved: "
    f"{testing_decision}"
)

print(
    f"- People outside development team involved: "
    f"{outside_development_team}"
)

print("\nWHAT CHANGED?")

print(
    f"- Changes documented: "
    f"{changes_documented}"
)

print(
    f"- Changes described: "
    f"{changes_description}"
)

print("\n----------------------------------------")

print(
    "This tool does not assign a score or determine "
    "whether an AI system was adequately tested."
)

print(
    "It makes participation visible so humans can "
    "ask better evaluation questions."
)

print("\nA system card can tell me what you tested.")

print(
    "I also want to know who helped you understand "
    "what needed testing in the first place."
)