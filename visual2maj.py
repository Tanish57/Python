import matplotlib.pyplot as plt

# Gross Enrolment Ratio (GER) in higher education for age group 18-23 years
years = ['2019-20', '2020-21']
ger_2011 = [25.6, 27.3]
ger_2001 = [27.1, 0]
plt.bar(years, ger_2011, label='GER (2011 projection)')
plt.bar(years, ger_2001, label='GER (2001 projection)')
plt.title('Gross Enrolment Ratio (GER) in Higher Education')
plt.xlabel('Year')
plt.ylabel('GER')
plt.legend()
plt.show()

# GER by gender
labels = ['Male', 'Female']
ger_gender = [26.7, 27.9]
plt.pie(ger_gender, labels=labels, autopct='%1.1f%%')
plt.title('GER by Gender')
plt.show()

# GER by Scheduled Caste/Tribe
labels = ['Scheduled Castes', 'Scheduled Tribes']
ger_sc_st = [23.1, 18.9]
plt.pie(ger_sc_st, labels=labels, autopct='%1.1f%%')
plt.title('GER by Scheduled Caste/Tribe')
plt.show()

# Enrolment by type of institution
labels = ['Govt. Universities', 'Deemed Universities - Govt. Aided', 'Private Universities']
enrolment_type = [73.1, 0.6, 26.3]
plt.pie(enrolment_type, labels=labels, autopct='%1.1f%%')
plt.title('Enrolment by Type of Institution')
plt.show()

# Enrolment by type of college
labels = ['Govt. Colleges', 'Private (Aided) Colleges', 'Private (Unaided) Colleges']
enrolment_college = [34.5, 21.1, 44.4]
plt.pie(enrolment_college, labels=labels, autopct='%1.1f%%')
plt.title('Enrolment by Type of College')
plt.show()

# Average enrolment by type of college
labels = ['Govt. Colleges', 'Private (Aided) Colleges', 'Private (Unaided) Colleges']
avg_enrolment_college = [1097, 1057, 465]
plt.bar(labels, avg_enrolment_college)
plt.title('Average Enrolment by Type of College')
plt.xlabel('Type of College')
plt.ylabel('Average Enrolment')
plt.show()

# Enrolment by level of course
labels = ['Undergraduate', 'Postgraduate']
enrolment_level = [78.09, 11.5]
plt.pie(enrolment_level, labels=labels, autopct='%1.1f%%')
plt.title('Enrolment by Level of Course')
plt.show()

# Enrolment by field of study (Undergraduate)
labels = ['Arts', 'Science', 'Commerce', 'Engineering & Technology']
enrolment_field_ug = [33.5, 15.5, 13.9, 11.9]
plt.bar(labels, enrolment_field_ug)
plt.title('Enrolment by Field of Study (Undergraduate)')
plt.xlabel('Field of Study')
plt.ylabel('Enrolment')
plt.show()

# Enrolment by field of study (Postgraduate)
labels = ['Social Science', 'Science']
enrolment_field_pg = [20.56, 14.83]
plt.bar(labels, enrolment_field_pg)
plt.title
