import matplotlib.pyplot as plt

# Data
years = ['2014-15', '2018-19', '2019-20', '2020-21']
total_enrolment = [29375281, 37167947, 38576953, 41258144]
male_enrolment = [14777370, 18121192, 19574312, 21152125]
female_enrolment = [14597911, 19046755, 19002641, 20106019]
sc_enrolment = [4894795, 6135899, 6575575, 5879563]
st_enrolment = [1611547, 1925371, 2160539, 2409372]
obc_enrolment = [11203930, 14429270, 14227131, 14825871]
other_enrolment = [6730009, 7842460, 7916344, 8593356]
top_states = ['Uttar Pradesh', 'Maharashtra', 'Tamil Nadu', 'Madhya Pradesh', 'Karnataka', 'Rajasthan']
top_states_enrolment = [10393048, 6954473, 5044353, 3790451, 3539855, 3524819]

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Total enrolment
axes[0, 0].plot(years, total_enrolment, 'o-', label='Total')
axes[0, 0].set_title('Total Enrolment in Higher Education')
axes[0, 0].set_xlabel('Academic Year')
axes[0, 0].set_ylabel('Number of Students (in crores)')
axes[0, 0].legend()

# Gender enrolment
axes[0, 1].plot(years, male_enrolment, 'o-', label='Male')
axes[0, 1].plot(years, female_enrolment, 'o-', label='Female')
axes[0, 1].set_title('Gender-wise Enrolment in Higher Education')
axes[0, 1].set_xlabel('Academic Year')
axes[0, 1].set_ylabel('Number of Students (in crores)')
axes[0, 1].legend()

# Community enrolment
axes[1, 0].plot(years, sc_enrolment, 'o-', label='SC')
axes[1, 0].plot(years, st_enrolment, 'o-', label='ST')
axes[1, 0].plot(years, obc_enrolment, 'o-', label='OBC')
axes[1, 0].plot(years, other_enrolment, 'o-', label='Others')
axes[1, 0].set_title('Community-wise Enrolment in Higher Education')
axes[1, 0].set_xlabel('Academic Year')
axes[1, 0].set_ylabel('Number of Students (in crores)')
axes[1, 0].legend()

# Top states enrolment
axes[1, 1].barh(top_states, top_states_enrolment)
axes[1, 1].set_title('Top 6 States in Student Enrolment')
axes[1, 1].set_xlabel('Number of Students (in crores)')
axes[1, 1].set_ylabel('State')

plt.tight_layout()
plt.show()
